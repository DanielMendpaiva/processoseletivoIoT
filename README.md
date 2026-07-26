# Processo Seletivo – Intensivo Maker | IoT

## Etapa Prática – Sistemas Embarcados

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker | IoT**.

Esta atividade tem como objetivo avaliar suas competências em **Sistemas Embarcados**, com foco em **organização de projeto, lógica de firmware e simulação de hardware**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> **Objetivo principal**  
> Avaliar sua capacidade de **planejar, estruturar e desenvolver** uma solução funcional de sistemas embarcados, seguindo boas práticas de engenharia.

---

## Antes de Tudo

Se você **nunca utilizou Git ou GitHub**, não se preocupe.  
Siga atentamente os passos abaixo.

---

### 1 - Criação de Conta no GitHub

1. Acesse: <https://github.com>
2. Clique em **Sign up**
3. Crie sua conta gratuita seguindo as instruções da plataforma

> O GitHub será utilizado para:
>
> - Envio do seu projeto
> - Versionamento do código
> - Correção e validação automática via GitHub Actions

---

### 2 - Instalação do Git

O **Git** é a ferramenta responsável pelo controle de versões do seu código.

### Windows

Baixe e instale o **Git Bash**:  
<https://git-scm.com/downloads>

### Linux / macOS

Verifique se o Git já está instalado:

```bash
git --version
```

> Caso não esteja, instale pelo gerenciador de pacotes do seu sistema.

## Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório no seu GitHub.

### 1 - Fork do Repositório

No canto superior direito desta página, clique em Fork

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />

Uma cópia do repositório será criada no seu perfil do GitHub

> O Fork permite que você trabalhe de forma independente, sem alterar o repositório original do processo seletivo.

### 2 - Clone do Repositório

No repositório do seu Fork, clique em **<> Code**

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Copie a URL e execute no terminal:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

> O comando git clone cria uma cópia local do repositório para desenvolvimento.

### 3 - Preparação do Ambiente de Execução

Você pode executar o projeto de duas formas. Escolha apenas uma.

#### Opção A – Ambiente Python Local

**Requisitos:**

- Python 3.10 ou 3.11
- pip

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

#### Opção B – Dev Container (Recomendado)

Este repositório inclui um Dev Container, garantindo um ambiente padronizado.

**Requisitos:**

- VS Code
- Docker instalado
- Extensão Dev Containers

**Passos:**

1. Abra o repositório no VS Code
2. Clique em “Reopen in Container”
3. Aguarde a criação automática do ambiente

> Todas as dependências serão instaladas automaticamente.

## Criando sua API Key do Wokwi

A simulação do projeto será executada automaticamente via GitHub Actions, utilizando o Wokwi CLI.

Para isso, você precisa gerar uma API Key.

1. Acesse: <https://wokwi.com/dashboard/ci>
2. Faça login (Google ou GitHub)
3. Clique em Generate API Token
4. Copie a chave gerada (exemplo: wokwi-xxxxxxxx)

> Importante

- Nunca faça commit dessa chave
- Ela deve ser armazenada apenas como secret no GitHub

## Configurando a API Key no GitHub (Secrets)

**No repositório do seu Fork:**

1. Vá em Settings
2. Acesse Secrets and variables → Actions
3. Clique em New repository secret
4. Nome: WOKWI_CLI_TOKEN
5. Valor: sua chave gerada
6. Salve

> As GitHub Actions do template já estão preparadas para usar essa variável automaticamente.

## Desafio Técnico

Você deverá desenvolver um projeto de sistemas embarcados simulados, utilizando Python e Wokwi.

### Estrutura mínima esperada

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

> Você pode expandir essa estrutura se desejar, desde que mantenha os arquivos essenciais.

### Escolha do cenário

No diretório "scenarios" existem arquivos .md e pastas referentes a diferentes desafios. Selecione apenas um deles e mantenha apenas a pasta e .md referente ao desafio a ser desenvolvido, deletando os demais. Isso fará com o que o fluxo de testes automáticos selecione o fluxo de acordo com o desafio escolhido.

### Como Desenvolver seu Projeto

O desenvolvimento acontece principalmente nos arquivos abaixo:

#### src/main.py

- Código Python executado na simulação
- Implementa a lógica do sistema embarcado
- Exemplos: controle de LEDs, leitura de sensores, estados, temporizações, etc.

#### diagram.json

- Define o hardware virtual do projeto
- Componentes como:
  - LEDs
  - Botões
  - Sensores
  - Placa microcontroladora

#### wokwi.toml

- Configura a simulação:
  - Tipo de placa
  - Framework
  - Dependências adicionais
 
#### Rodando localmente

Para executar o seu projeto locamente, é necesário preparar a imagem docker local, e após isso
utiliza-la para gerar o arquivo que conterá o seu código para o projeto, para isso, execute os 
seguintes códigos:

1. Prepara a imagem docker (Necessário rodar apenas 1 vez)

```bash
docker build -t esp32-builder -f Dockerfile .
```

2. Prepara o arquivo de memória fs.bin (Necessário a cada iteração)

```bash
docker run --rm -v "$(pwd)/src:/mnt/src" -v "$(pwd):/mnt/out" esp32-builder bash -c "mkdir -p /tmp/fs && cp -r /mnt/src/* /tmp/fs/ && /mklittlefs/mklittlefs -c /tmp/fs -b 4096 -p 256 -s 0x200000 /mnt/out/fs.bin"
```

#### Commit e Push

Após suas alterações:

```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push
```

### Execução Automática (GitHub Actions)

A cada push, o GitHub Actions irá automaticamente:

- Executar o pipeline de build
- Rodar a simulação via Wokwi CLI
- Validar que o projeto executa sem erros

### Caso algo falhe

- Vá até a aba Actions
- Analise os logs da execução
- Corrija e envie novamente

## Critérios de Avaliação

Esta etapa será avaliada considerando:

- Funcionamento correto da simulação
- Código organizado e legível
- Estrutura de arquivos correta
- Uso adequado do Wokwi
- Commits claros e bem descritos
- Projeto executando sem falhas nas Actions

---

## Submissão Final

Após concluir o desenvolvimento:

1. Verifique se o projeto **executa sem erros** nas GitHub Actions
2. Confirme que todos os arquivos obrigatórios estão presentes
3. Copie o link do **seu repositório no GitHub**

Envie o link conforme as orientações do processo seletivo na plataforma do **PNAAT**.

---

## Relatório do Candidato

O arquivo **`README.md` do seu repositório** deve ser utilizado como o  
**relatório final do desafio técnico**.

Preencha todas as seções abaixo de forma **clara, objetiva e técnica**.

> **Dica importante**  
> Não é necessário um relatório extenso.  
> O principal critério é demonstrar **clareza nas decisões técnicas**, organização e entendimento do sistema embarcado desenvolvido.
> Não mantenha os demais conteúdos escritos nesse arquivo README, aqui devem ser concentradas apenas informações referentes ao projeto desenvolvido.

---

### Identificação do Candidato

- **Nome completo:** Daniel Mendonça Paiva
- **GitHub:** https://github.com/DanielMendpaiva/processoseletivoIoT.git

---

## Visão Geral da Solução

Descreva, em poucas palavras:

- Qual é o objetivo do seu projeto
- O que o sistema embarcado simulado faz
- Como o usuário interage com ele (se aplicável)

O objetivo deste projeto é desenvolver uma solução embarcada de baixo custo para controle de qualidade e auditoria em ambientes com temperatura controlada (ex.: câmaras frigoríficas, estufas de incubação ou painéis elétricos industriais). 

O sistema monitora a integridade do isolamento térmico e físico prevenindo a degradação de insumos sensíveis ou o sobreaquecimento de componentes através de duas lógicas de segurança operadas concorrentemente:

1. **Monitoramento do Tempo de Exposição (Porta Aberta):** Detecção contínua do estado físico da porta/tampa e disparo de alarme caso o tempo de abertura exceda o limite parametrizado constante x = 5000ms.

2. **Monitoramento de Variação Térmica Abrupta ($\Delta T$):** Monitoramento do gradiente térmico da câmara em relação à temperatura de referência estável, disparando alarme caso o incremento ultrapasse a tolerância Y = 3°C.

3. **Restauração e Normalização de Estado:** Recuperação automática do estado seguro apenas quando **ambas** as condições de risco cessarem simultaneamente.

---

## Arquitetura do Sistema Embarcado

Explique a arquitetura lógica do seu projeto, abordando:

- Fluxo principal do programa (`main.py`)
- Estrutura de estados, loops ou temporizações
- Como os componentes interagem entre si

Se desejar, utilize tópicos ou um pequeno diagrama em texto.

┌────────────────────────────────────────────────────────────────────────┐
│                          PERIFÉRICOS DE HARDWARE                       │
│  ┌───────────────────────┐              ┌───────────────────────────┐  │
│  │ MPU6050 Sensor (imu1) │              │ Sensor de Porta (btn1)    │  │
│  │ Barramento I2C (0x68) │              │ Pino Digital GPIO4        │  │
│  └───────────┬───────────┘              └─────────────┬─────────────┘  │
└──────────────┼────────────────────────────────────────┼────────────────┘
               │ (Temp em °C)                           │ (Estado 0/1)
               ▼                                        ▼
┌────────────────────────────────────────────────────────────────────────┐
│                      FLUXO PRINCIPAL (src/main.py)                     │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │ Class SmartCoolerMonitor (POO)                                   │  │
│  │                                                                  │  │
│  │  1. Temporizador Não-Bloqueante: time.ticks_ms()                 │  │
│  │  2. Cálculo de Gradiente: Delta T = Temp_atual - Temp_referencia │  │
│  │  3. Monitor de Exposição: Elapsed = time.ticks_diff(now, start)  │  │
│  └──────────────────────────────┬───────────────────────────────────┘  │
└─────────────────────────────────┼──────────────────────────────────────┘
                                  │ (Logs UART 115200 baud)
                                  ▼
┌────────────────────────────────────────────────────────────────────────┐
│                          SAÍDA SERIAL / WOKWI CI                       │
│  • "Sistema de Monitoramento Inicializado"                             │
│  • "ALERTA: Porta aberta por muito tempo!"                             │
│  • "ALERTA: Degradacao termica detectada!"                             │
│  • "Status: Sistema Normalizado."                                      │
└────────────────────────────────────────────────────────────────────────┘

1. Fluxo Principal do Programa (src/main.py)
Inicialização: A função main() instancia o objeto SmartCoolerMonitor(). O construtor configura o pino digital GPIO4, acorda o MPU6050 enviando o byte 0x00 para o registrador PWR_MGMT_1 (0x6B), armazena a temperatura inicial estável como referência (baseline_temp) e imprime no terminal a mensagem obrigatória: "Sistema de Monitoramento Inicializado".

Loop Principal (Polling Loop): O loop while True monitora continuamente o tempo interno do microcontrolador via time.ticks_ms(). A cada 100ms, o método process_cycle() é invocado de forma assíncrona para reavaliar os sensores.

2. Estrutura de Estados, Loops e Temporizações
Máquina de Estados Finitos (FSM): O sistema opera alternando entre quatro estados lógicos principais: Normal, Alerta de Porta Aberta, Alerta de Elevação Térmica e Normalizado.

Concorrência Não-Bloqueante: Toda a temporização utiliza a função time.ticks_diff(now_ms, start_ms) em vez de time.sleep(). Isso garante que o microcontrolador permaneça reativo a mudanças bruscas de sinais sem congelar a execução da CPU.

Monitor de Tempo de Porta (X = 5000 ms)
Se o botão btn1 for solto (pressed: 0), o relógio marca o instante inicial. Caso a porta continue aberta por 5000 ms contínuos, a flag alarm_door_active é ativada e o alerta de exposição é emitido.

Monitor de Variação Térmica (ΔT >= 3°C)
A cada ciclo, calcula-se a variação térmica através da fórmula: ΔT = Tatual - Treferência. Se a variação atingir ou superar 3.0 °C, a flag alarm_temp_active é acionada.

Normalização Automática
Se o sistema estiver em estado de alarme, mas o botão for pressionado (btn1: 1 - porta fechada) E a variação de temperatura cair abaixo de 3.0 °C, o sistema emite a mensagem "Status: Sistema Normalizado." e redefine a temperatura de referência.


3. Interação entre Componentes

MPU6050 para ESP32 (I2C)
A comunicação I2C lê os registradores de alta e baixa ordem (0x41 e 0x42), convertendo o valor numérico de 16 bits assinado para graus Celsius através da relação física:
T = (raw / 340.0) + 36.53

Pushbutton btn1 para ESP32 (GPIO)
O pino digital GPIO4 lê a mudança de nível lógico correspondente ao estado físico da porta/tampa (0 para aberta, 1 para fechada).

ESP32 para Wokwi CI (UART Serial)
Todas as mudanças relevantes de estado imprimem mensagens padronizadas no barramento serial TX/RX, permitindo que a esteira automatizada do GitHub Actions valide o cumprimento das regras do edital.

---

## Componentes Utilizados na Simulação

Liste os principais componentes definidos no `diagram.json`, por exemplo:

- Tipo de placa utilizada
- LEDs, botões, sensores, atuadores, etc.
- Função de cada componente no sistema

A arquitetura de hardware virtual do projeto foi projetada e mapeada no arquivo diagram.json utilizando o ecossistema de simulação do Wokwi. O sistema é construído em torno da placa microcontroladora ESP32 DevKit C v4, integrando um sensor inercial e de temperatura MPU6050 via barramento de comunicação I2C e um botão mecânico de fim de curso configurado como sensor digital de porta. O monitor serial embutido na interface UART é utilizado como o periférico de saída de telemetria, permitindo que os logs operacionais e os alarmes de segurança sejam transmitidos e validados pela esteira de integração contínua (CI).

1. Microcontrolador Principal: ESP32 DevKit C v4 (id: "esp")
Tipo de componente: board-esp32-devkit-c-v4
Função no sistema: Atua como a Unidade Central de Processamento do sistema embarcado. Executa o firmware em MicroPython, gerencia a temporização assíncrona de hardware, processa a comunicação I2C com o sensor de temperatura, monitora o estado lógico do pino da porta e transmite os eventos de status via comunicação serial UART.

2. Sensor de Temperatura Ambiente: MPU6050 IMU (id: "imu1")
Tipo de componente: wokwi-mpu6050
Conexões de pino: Alimentado em 3V3 e GND; conectado aos pinos de comunicação I2C do ESP32 (GPIO21 - SDA / GPIO22 - SCL).
Função no sistema: Responsável pelo monitoramento térmico contínuo do ambiente interno (câmara refrigerada ou estufa). Fornece as leituras brutas dos registradores de temperatura via endereço I2C 0x68, permitindo ao firmware calcular o gradiente de variação térmica (ΔT) em relação à temperatura de referência estável.

3. Sensor Físico de Porta: Pushbutton Fim de Curso (id: "btn1")
Tipo de componente: wokwi-pushbutton
Conexões de pino: Pino 1.A conectado ao GPIO4 e pino 2.A conectado ao 3V3 do ESP32.
Função no sistema: Atua como o sensor de posição/abertura da porta. Quando a porta está fechada, o botão permanece pressionado (pressed: 1), mantendo o pino GPIO4 em nível lógico alto (1). Quando a porta é aberta, o botão é solto (pressed: 0), alterando o pino para nível lógico baixo (0) e disparando a contagem do temporizador de exposição.

4. Interface de Telemetria e Saída: Monitor Serial UART (id: "$serialMonitor")
Tipo de componente: Terminal de Comunicação Serial (TX/RX)
Conexões de pino: Interconectado aos pinos de transmissão de dados do ESP32 (esp:TX e esp:RX).
Função no sistema: Canal de saída responsável pela transmissão dos logs de eventos em tempo real (inicialização, alertas de porta aberta, degradação térmica e restauração de status) com taxa de transmissão de 115200 baud, permitindo a validação automática pela esteira Wokwi CI.

---

## Decisões Técnicas Relevantes

Explique brevemente decisões importantes tomadas durante o desenvolvimento, como:

- Organização do código
- Uso de funções, estados ou constantes
- Estratégias para temporização ou controle lógico

1. Programação Orientada a Objetos (POO): Encapsulamento de toda a lógica na classe SmartCoolerMonitor, eliminando variáveis globais soltas e isolando o escopo de estado do sistema.

2. Temporização Não-Bloqueante (Zero time.sleep()): Uso exclusivo de time.ticks_ms() e time.ticks_diff(), garantindo que a CPU do ESP32 leia sensores e botões sem travar a execução.

3. Constantes Declarativas (Clean Code): Eliminação de "números mágicos", agrupando todos os pinos, limiares de segurança (5000ms
e 3°C) e mensagens no topo do código.

4. Máquina de Estados (FSM) e Gestão de Logs: Controle por flags booleanas (alarm_door_active e alarm_temp_active), evitando duplicação de mensagens seriais e garantindo emissão única nos eventos de alarme e normalização.

---

## Resultados Obtidos

Descreva o comportamento final do sistema:

- O que funciona corretamente
- Quais requisitos foram atendidos
- Resultado observado na simulação do Wokwi

1. Desempenho Funcional e Validação dos Alarmes:

Inicialização Limpa: Ao energizar a placa ESP32, o firmware configura o barramento I2C, retira o sensor MPU6050 do modo de repouso e imprime a mensagem exata de boot no terminal: "Sistema de Monitoramento Inicializado".
Detecção de Porta Aberta (Caso de Teste 1): Quando a porta é aberta (botão btn1 solto), o temporizador interno é iniciado. Ao completar exatamente 5000 ms (5 segundos) contínuos sem o fechamento da porta, o sistema emite o log "ALERTA: Porta aberta por muito tempo!". Testes intermediários com tempos menores (ex: 3 segundos de exposição) comprovaram que o alarme não dispara precocemente.
Monitoramento de Variação Térmica (Caso de Teste 2): Enquanto a porta permanece fechada, o sistema armazena a temperatura de referência inicial (ex: 20 °C). Ao simular uma subida brusca para 24 °C (variação de Delta T igual a 4.0 °C, superando o limite de 3.0 °C), o algoritmo identifica a anomalia no ciclo de amostragem de 100ms e dispara o log "ALERTA: Degradacao termica detectada!".
Restauração e Normalização de Status (Caso de Teste 3): Estando o sistema em estado de alarme, a simulação do fechamento da porta (botão btn1 pressionado) combinada à temperatura estável aciona a rotina de recuperação. O firmware emite a mensagem "Status: Sistema Normalizado.", limpa os sinalizadores de erro e atualiza a temperatura de referência para o novo valor ambiente.

2. Confiabilidade e Comportamento na Esteira Wokwi CI:

Aprovação Integral: Obteve-se status PASS (100% de aprovação) em todos os três cenários de testes automatizados (test_1.yaml, test_2.yaml e test_3.yaml).
Fidelidade de Caracteres: A saída na interface UART (115200 baud) respondeu com precisão estrita de maiúsculas, minúsculas e pontuação exigida pelo validador, sem emitir mensagens duplicadas a cada ciclo de relógio.
Reatividade da CPU: O uso de temporizadores assíncronos baseados no relógio de hardware (ticks_ms) garantiu uma taxa de amostragem estável a cada 100ms, eliminando qualquer risco de travamento do processador ou perda de leitura de eventos.

---

## Comentários Adicionais (Opcional)

Utilize este espaço para comentar, se desejar:

- Dificuldades encontradas
- Limitações da solução
- Melhorias que você faria com mais tempo
- Principais aprendizados durante o desafio

---

> Este relatório faz parte da avaliação técnica.  
> Clareza, objetividade e organização são tão importantes quanto o funcionamento do código.

---

## Especificação dos Testes Automatizados (Wokwi CI)

Para que o projeto seja validado com sucesso na esteira de integração contínua (CI), o firmware escrito em MicroPython deve interagir corretamente com as leituras dos sensores descritos em cada cenário e enviar as mensagens de status exatas.

### Requisitos Críticos de Implementação

1. **Casamento Exato de Strings:** O Wokwi CI faz uma verificação estrita caractere por caractere. Se houver divergência em maiúsculas/minúsculas, acentuação ou falta de pontuação, o teste irá falhar.
2. **Arquitetura Não-Bloqueante:** Evite o uso de funções bloqueantes. Elas podem fazer com que o firmware perca a janela de tempo em que o simulador altera o peso, quebrando a sincronia do teste automatizado.

---

## Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores
