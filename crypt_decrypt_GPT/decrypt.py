import os
import ftplib

# Conexão com o servidor ftp
ftp = ftplib.FTP("files.000webhost.com")
ftp.login("cloudpurplecomp", "jZnJYuN28T(trfUFbMDL")

# Baixando o arquivo keyfile.key
with open("keyfile.key", "wb") as f:
    ftp.retrbinary("RETR keyfile.key", f.write)

ftp.quit()

# Lendo a chave do arquivo keyfile.key
with open("keyfile.key", "rb") as f:
    key = f.read()

# Identificando as pastas criptografadas no sistema
encrypted_folders = []
for root, dirs, files in os.walk("/"):
    for dir in dirs:
        if dir == "encrypted":
            encrypted_folders.append(os.path.join(root, dir))

# Descriptografar as pastas encontradas
for folder in encrypted_folders:
    os.system("encfs -u {} decrypted".format(folder))

# Delete keyfile.key do disco local
os.remove("keyfile.key")
