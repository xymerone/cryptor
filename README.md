# Cruptor v1.0
## This script is designed to encrypt and decrypt files in the specified cprypt_files folder.

The following modules are needed for the script to work: - progressbar - cryptography We drop the files we want to encrypt into the folder 'cprypt_files' and run the script. To work, you need an encryption key, you can get it like this:

` from cryptography.fernet import Fernet

 print(Fernet.generate_key())`

> Please note that the key is generated in bytes format; to use it, you need to turn it into a string.

`from cryptography.fernet import Fernet`

`print(Fernet.generate_key().decode('utf-8'))`

Once you have created the key, you can perform encryption - decrypt files.
We enter your key into the "Key crypt" request (the key must be beaten in string format), then we enter the command number (encrypt or decrypt) and press enter, you will see the progress bar of the work. It is also possible to ask whether to delete
if yes, enter "D" source files, if you do not want to delete, just press Enter, when decrypting, encryption files are deleted automatically!




