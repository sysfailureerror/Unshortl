# UnShoRtL

<!--OBS: Se estiver lendo pelo celular coloque no modo desktop, algumas palavras podem aparecer diferente do que realmente é. -->

Use este programa escrito em Python 3.x, para encurtar ou encontrar a url original, caso ela esteja encurtada.

## Install
----------------------------------------

### Instalação Principal
----------------------------------------
```
1. git clone https://github.com/Z4h4rd/Unshortl.git

2. cd Unshortl

3. pip install -r requirements.txt  

4. python3 unshortl.py

```
----------------------------------------
### <s>Instalação com install_opcional.sh</s> (Ainda em verificação, use a instalação principal)
----------------------------------------
Essa instalação estar configurado como padrão o diretório */bin/* do aplicativo **Termux** para android, se você quer usá-lo para **outro OS**, **mude** para o caminho correto do seu diretório bin/ do seu OS neste script, *install_opcional.sh*.

Obs: Com essa forma de instalação você poderar executar o script somente digitando **unshortl**.
```
1. git clone https://github.com/Z4h4rd/Unshortl.git

2. cd Unshortl

3. chmod +x install_opcional.sh 

4. ./install_opcional.sh
 
```
--------------------------------------
**P.S.**: Se estiver pensando em apagar(*completamente..*) o programa depois, sugiro ir pela Instalação principal, será menos trabalhoso desinstalar.

--------------------------------------
# Em Caso de Erros nas Bibliotecas
-----------------------------------
Se ocorrer algum erro na instalação das bibliotecas (*requests* e *beautifulsoup*), mesmo depois de executar o *requirements.txt*, recomendo tentar instalar elas manualmente.
```
pip3 install beautifulsoup4
pip3 install requests
```
   **OU**
```
apt-get install python3-bs4 -y
apt-get install python3-requests -y
```
------------------------------------
