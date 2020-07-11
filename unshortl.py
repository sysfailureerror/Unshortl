#By SysFailureError
# -*- coding: utf-8 -*-
import requests
import os
from bs4 import BeautifulSoup
#------------------------------------------------------------------------
#------------------------------Menu & Opções-----------------------------
def menu():
	print("URL-Manip")
	print("1 - Encurtar url")
	print("2 - Mostrar url original")
	print("0 - Sair")
	opc = input("Escolha uma da opções: ")
	opcao(opc)

def opcao(opc):
	try:
		int(opc)
	except ValueError:
		os.system("clear")
		print("Escolha o numero das opções..")
		menu()
	if opc == '1':
		opcao1()
	elif opc == '2':
		opcao2()
	elif opc == '0':
		exit('0')
	else:
		os.system("clear")
		print("Escolha uma opção valida.")
		menu()
#-------------------------Desencurtar---------------------------
def opcao2():
	url_unshorten = input("Digite a url que você deseja revelar:\n")
	verif_url = requests.get(url_unshorten)
	print(unshorten(url_unshorten))

def unshorten(url_unshorten):
	session = requests.Session()  #Mantem uma sessão, caso não seja possivel na primeira tentativa, continua send requests
	url_origin = session.head('{0}'.format(url_unshorten), allow_redirects=True)
	return url_origin.url
#-------------------------Encurtar------------------------------	
def opcao1():
	url_shorten = input("Digite a url que você deseja encurtar:\n")
	print(shorten(url_shorten))

def shorten(url_shorten):
	timeout = 10
	#headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
	url = 'https://is.gd/create.php'
	session = requests.Session()
	parametros = {'url': url_shorten}#name="" OR id="" object dentro das aspas
	acessa = session.get(url, params = parametros, timeout = timeout, verify = True) # headers = headers
	soup = BeautifulSoup(acessa.text, 'html.parser')#Atribuir aninhamento a variavel soup do objeto-Response-acessa
	for link in soup.find_all(id="short_url"):
		url_encurtada = link.get('value')
	if acessa.status_code == 200: #Se o requests foi executado com sucesso(200) retorna url_encurtada 
		return url_encurtada
	else:
		print("Não foi possivel encurtar a url. Erro ", acessa.status_code)
#---------------------------------------------------------------
if __name__=='__main__':
	menu()

#Possíveis erros na resposta do site: 2xx Sucesso, 3xx Redirecionamento, 4xx Erro de cliente, 5xx outros erros / Erro do sevidor

