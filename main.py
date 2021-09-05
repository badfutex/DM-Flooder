# Cria DM's "infinitas" (na verdade é até o discord te bloquear)

# @badfutex | github.com/badfutex

import requests
import colorama

colorama.init()

API1= 'https://discord.com/channels/'
API2 = 'https://discord.com/api/v9/channels/'

print ('''
\033[0;36m
	 _____  __  __   ______ _                 _           
	 |  __ \|  \/  | |  ____| |               | |          
	 | |  | | \  / | | |__  | | ___   ___   __| | ___ _ __ 
	 | |  | | |\/| | |  __| | |/ _ \ / _ \ / _` |/ _ \ '__|
	 | |__| | |  | | | |    | | (_) | (_) | (_| |  __/ |   
	 |_____/|_|  |_| |_|    |_|\___/ \___/ \__,_|\___|_| 

              Feito por @badfutex | github.com/badfutex
              OBS: O 1° ID tem que ser o ID que fica apos o @me
              O programa faz apenas 20 DM's para evitar que a conta seja desativada 
              ''')
print ('\033[1;97m')
token = input('TOKEN: ')
id1 = input('ID 1: ')
id2 = input('ID 2: ')
full = '881281025475506207/recipients/853023796385546261'

headers = {

    'Host': 'discord.com',
    'Content-Length': '0',
    'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="92"',
    'Accept-Language': 'pt-BR',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Authorization': token,
    'Accept': '*/*',
    'Origin': 'https://discord.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': API1 + id1,
    'Accept-Encoding': 'gzip, deflate'



}

contador = 0
while (contador < 20):
    r = requests.put(API2 + id1 + '/recipients/' + id2,headers=headers)
    contador = contador + 1
