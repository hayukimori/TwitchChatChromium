# -*- coding: UTF-8 -*-

import sys
import os

args = sys.argv[1:]
channel = ' '.join(args)


print(f"channel:" ,channel)
if ('https://' in channel.lower()):
	print("Por favor, use apenas o nome do canal")




else:
	try:
		os.system(f"chromium --chrome-frame --window-size=400,640 --app=https://www.twitch.tv/popout/{channel}/chat")
	except:
		print(" \n\n Não foi possível abrir o chat deste canal\n Verifique se tem o chromium instalado")



