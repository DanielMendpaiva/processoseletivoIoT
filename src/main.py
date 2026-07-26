"""
Processo Seletivo – Intensivo Maker | IoT
Projeto: Sistema de Monitoramento de Temperatura e Abertura de Porta (Smart Cooler / Estufa)
Cenário: TEMPERATURE
"""

import time
from machine import I2C, Pin  # type: ignore

# Constantes de configuração de firmware
I2C_SDA_PIN = 21
I2C_SCL_PIN = 22
MPU6050_I2C_ADDR = 0x68
MPU6050_PWR_MGMT_1 = 0x6B
MPU6050_TEMP_REG = 0x41

DOOR_BUTTON_PIN = 4

# Limiares de Segurança
DOOR_OPEN_TIMEOUT_MS = 5000  # Limite X: 5 segundos de exposição
TEMP_DELTA_THRESHOLD = 3.0   # Limite Y: 3.0°C de variação térmica
POLL_INTERVAL_MS = 100       # Intervalo de amostragem não-bloqueante de 100ms

# Mensagens Padronizadas da Serial (Exigência estrita da esteira Wokwi CI)
MSG_INIT = "Sistema de Monitoramento Inicializado"
MSG_ALARM_DOOR = "ALERTA: Porta aberta por muito tempo!"
MSG_ALARM_TEMP = "ALERTA: Degradacao termica detectada!"
MSG_NORMALIZED = "Status: Sistema Normalizado."


class SmartCoolerMonitor:
    """
    Classe responsável pelo gerenciamento de estado e controle
    de sensores do sistema de monitoramento de temperatura e porta.
    """

    def __init__(self):
        # Configuração do pino da porta (Botão btn1: pressed=1 -> Fechada, 0 -> Aberta)
        self.btn_door = Pin(DOOR_BUTTON_PIN, Pin.IN, Pin.PULL_DOWN)

        # Configuração da comunicação I2C com o sensor MPU6050
        self.i2c = I2C(0, sda=Pin(I2C_SDA_PIN), scl=Pin(I2C_SCL_PIN), freq=400000)
        self._init_mpu6050()

        # Variáveis de Estado
        self.baseline_temp = self.read_temperature()
        self.door_open_start_ms = None

        # Flags de Alarme
        self.alarm_door_active = False
        self.alarm_temp_active = False

        # Sinalização de Inicialização Obrigatória
        print(MSG_INIT)

    def _init_mpu6050(self):
        """Inicializa e desperta o MPU6050 do modo de repouso."""
        try:
            self.i2c.writeto_mem(MPU6050_I2C_ADDR, MPU6050_PWR_MGMT_1, bytes([0x00]))
        except Exception:
            pass

    def read_temperature(self):
        """
        Lê e converte os registradores de temperatura do MPU6050 para Celsius (°C).
        Fórmula MPU6050: Temp_degC = (raw_temp / 340.0) + 36.53
        """
        try:
            data = self.i2c.readfrom_mem(MPU6050_I2C_ADDR, MPU6050_TEMP_REG, 2)
            raw_temp = (data[0] << 8) | data[1]
            if raw_temp >= 0x8000:
                raw_temp -= 0x10000
            return (raw_temp / 340.0) + 36.53
        except Exception:
            return 20.0

    def is_door_closed(self):
        """
        Verifica o estado da porta:
        Retorna True se btn1 estiver pressionado (pressed=1), indicando porta FECHADA.
        Retorna False se btn1 estiver solto (pressed=0), indicando porta ABERTA.
        """
        return self.btn_door.value() == 1

    def process_cycle(self, now_ms):
        """
        Executa um ciclo da Máquina de Estados Finitos (FSM) de forma não-bloqueante.
        """
        door_closed = self.is_door_closed()
        current_temp = self.read_temperature()

        # 1. Gerenciamento do Temporizador de Porta Aberta
        if not door_closed:
            if self.door_open_start_ms is None:
                self.door_open_start_ms = now_ms

            elapsed_door_ms = time.ticks_diff(now_ms, self.door_open_start_ms)
            if elapsed_door_ms >= DOOR_OPEN_TIMEOUT_MS and not self.alarm_door_active:
                print(MSG_ALARM_DOOR)
                self.alarm_door_active = True
        else:
            self.door_open_start_ms = None

        # 2. Gerenciamento de Variação Térmica (Delta T)
        delta_t = current_temp - self.baseline_temp

        if delta_t >= TEMP_DELTA_THRESHOLD and not self.alarm_temp_active:
            print(MSG_ALARM_TEMP)
            self.alarm_temp_active = True

        # 3. Lógica de Restauração e Normalização do Sistema
        in_alarm = self.alarm_door_active or self.alarm_temp_active
        if in_alarm and door_closed and (current_temp - self.baseline_temp < TEMP_DELTA_THRESHOLD):
            print(MSG_NORMALIZED)
            self.alarm_door_active = False
            self.alarm_temp_active = False
            self.baseline_temp = current_temp


def main():
    monitor = SmartCoolerMonitor()
    last_poll_ms = time.ticks_ms()

    # Loop Principal Não-Bloqueante
    while True:
        now_ms = time.ticks_ms()
        if time.ticks_diff(now_ms, last_poll_ms) >= POLL_INTERVAL_MS:
            last_poll_ms = now_ms
            monitor.process_cycle(now_ms)


if __name__ == "__main__":
    main()