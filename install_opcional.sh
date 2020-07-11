#!/bin/bash

echo "Instalando Requirimentos"

pip install -r requirements.txt

if [[ $? -eq 0 ]];then
	echo "Requerimentos instalados"
else
	echo "Não foi possivel executar requirements.txt"
	echo "Nova tentativa.."
	apt update -y
	apt upgrade -y
	apt-get remove --purge python-pip -y
	apt-get autoremove -y
	apt-get remove --purge python3-pip -y
	apt-get autoremove -y
	apt update -y
	apt upgrade -y
	apt install python -y
	apt install python3 -y
	apt-get install pyhton-pip -y
	apt-get install python3-pip -y
	apt-get install python3-bs4 -y
	apt-get install python3-requests -y
	pip3 install beautifulsoup4
	pip install requests
	pip3 install requests

	if [[ $? -eq 1 ]]; then
		echo "CAsO PeRdIdO.."
	fi
fi

echo "Criando atalho"

chmod +x unshortl.py

ln -s /data/data/com.termux/files/home/Unshortl/unshortl.py mv unshortl $PREFIX/bin

if [[ $? -eq 0 ]];then

	echo "Atalho criado"
else:
	echo "Ocorreu algum erro, não foi possivel criar um atalho."
fi

echo "Instalação completa"
