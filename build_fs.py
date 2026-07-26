from littlefs import LittleFS
import os

print("Criando imagem fs.bin com LittleFS via Python nativo...")

# Configuração da partição LittleFS do ESP32 (4096 * 512 = 2MB = 0x200000)
fs = LittleFS(block_size=4096, block_count=512)

for filename in os.listdir("src"):
    filepath = os.path.join("src", filename)
    if os.path.isfile(filepath):
        with open(filepath, "rb") as f:
            content = f.read()
        with fs.open(filename, "wb") as f:
            f.write(content)
        print(f"  + {filename}")

with open("fs.bin", "wb") as f:
    f.write(fs.context.buffer)

print("fs.bin gerado e atualizado com sucesso sem precisar do Docker!")
