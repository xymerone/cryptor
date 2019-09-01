# cryptor
This script is designed to encrypt and decrypt files in the specified cprypt_files folder.

The following modules are needed for the script to work:
             - progressbar
             - cryptography
 We drop the files we want to encrypt into the folder 'cprypt_files' and run the script.
To work, you need an encryption key, you can get it like this:
>>> from cryptography.fernet import Fernet
>>> print(Fernet.generate_jey())

