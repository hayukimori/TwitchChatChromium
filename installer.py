# -*- coding: utf-8 -*-

#installer.py

import os


HOME 		= os.path.expanduser('~')
PATH 		= f'{HOME}/.local/bin/'

b_name 	= os.listdir('bin/')

BIN_NAME	= BIN_NAME[0]


def install():
	try:
		print("Instalando...")
		os.system(f"chmod +x bin/{BIN_NAME}")
		os.system(f"cp ./bin/{BIN_NAME} {PATH}")

		v = os.path.exists(f"{PATH}{BIN_NAME}")

		if v == True:
			print("Instalado com sucesso")
		else:
			print("Não foi possível instalar, mas você pode copiar o bin para ~/.local/bin/")


	except Exception as e:
		with open('err_log.txt', 'w') as f:
			f.write(str(e))

		print("Ocorreu um erro durante a instalação, para mais informações, visualize o arquivo err_log.txt")


def uninstall():
	try:
		os.system(f'rm {PATH}{BIN_NAME}')

	except Exception as e:
		print(f"Não foi possível remover o arquivo em {PATH}")
		raise e


if __name__ == '__main__':

	if_installed = os.path.exists(f"{PATH}{BIN_NAME}")

	if if_installed == True:
		verif = input(f"{BIN_NAME} já está instalado em {PATH}. Desinstalar? (Y/n)")

		if verif.lower() == 'n':
			sys.exit()
		else:
			print("Ok, desinstalando...")
			uninstall()

	else:
		install()