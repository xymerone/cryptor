import  re
import progressbar
from cryptography.fernet import Fernet
from os.path import join, dirname, basename, isdir, isfile
from os import listdir, mkdir, remove
from shutil import copyfile

ROOT = dirname(__file__)
CRYPT_DIR = join(ROOT, 'cprypt_files')
CHARSET = 'utf-8'
CRYPT_FORMAT = 'crypt'
PROFILE_WORK = ['encrypt', 'decrypt']
b = lambda x: bytes(x, encoding=CHARSET)

FERNET_KEY = b(input("Key crypt: ").strip())
FERNET = Fernet(FERNET_KEY)


list_file = [join(CRYPT_DIR, file) for file in listdir(CRYPT_DIR)]

def get_format_file(file):
	if isfile(file):
		return re.search(r'\.([\d\w]+?)$', file).group(1)
	elif isdir(file):
		return ''
	else:
		raise ValueError("Incorect! This not file or folder!")
	pass

def scan_file(dir, type_crypt='encrypt'):
	res = []
	for file in listdir(dir):
		if type_crypt == 'encrypt' and get_format_file(join(dir, file)) != CRYPT_FORMAT:
			res.append(join(dir, file))
		elif type_crypt == 'decrypt' and get_format_file(join(dir,file)) == CRYPT_FORMAT:
			res.append(join(dir, file))
	return res
	return [join(dir, file) for file in listdir(dir)]

def crypt_file(list_file, type_crypt='encrypt', delete_file=False):
	for i,file in enumerate( list_file):
		if type_crypt == 'encrypt':
			file_name_crypt = file+'.'+CRYPT_FORMAT
		elif type_crypt == 'decrypt':
			file_name_crypt = file.replace('.'+CRYPT_FORMAT, '')
			delete_file = True
		with open(file, 'rb') as read_file:
			data_file = read_file.read()
		with open(file_name_crypt, 'wb') as crypt_file:
			print_file_name = basename(file_name_crypt)
			print_mess = 'encryptded'
			if type_crypt == 'decrypt':
				print_mess = 'decryptded'
				data_file = FERNET.decrypt(data_file)
			elif type_crypt == 'encrypt':
				data_file = FERNET.encrypt(data_file)
			else:
				raise ValueError("Error type ctyptor")
			crypt_file.write(data_file)
		idc = str(i+1)
		if delete_file: remove(file)
		yield f"{idc}. {print_file_name} -> {print_mess} ..ok!"
		#return result
def profile():
	for i,v in enumerate(PROFILE_WORK):
		i = str(i+1)
		print(f"{i}. {v}")
	i = input("Id profile (default 1): ")
	i = 1 if len(i) == 0 else int(i)
	i = 1 if len(PROFILE_WORK) < i else i-1
	return PROFILE_WORK[i]

if __name__ == "__main__":
	profile = profile()
	delete = bool( input('Delete file (degalut NO): ').strip()) if profile == 'encrypt' else True
	print(profile)
	files = scan_file(CRYPT_DIR, profile)
	bar = progressbar.ProgressBar(max_value=len(files))
	i = 0
	for res in crypt_file(files, profile, delete):
		#print(res)
		bar.update(i)
		i += 1
