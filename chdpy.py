from bs4 import BeautifulSoup as b
from colorama import Fore, Style, init
import requests, sys, os, time
e='  '
############ COLORES ##############
WHITE=f'{Fore.WHITE}{Style.BRIGHT}'
GREEN=f'{Fore.GREEN}{Style.BRIGHT}'
RED=f'{Fore.RED}{Style.BRIGHT}'
RESET=f'{Style.RESET_ALL}'
###################################
init(autoreset=True)
os.system('cls' if os.name == 'nt' else 'clear')
ip=input(f"{e}Introduzca la direccion IP > ")
port=input(f"{e}Introduzca el Puerto > ")
url=f'http://{ip}:{port}'
alm='almacenamiento'
files=[]
print("")
def enter():
 print(f"\n{e}{WHITE}Presione [ENTER] Para Continuar....", end=""); input()

def salir(x0):
 if x0 == 'exit' or x0 == 'exit()':
  sys.exit()
 else:
  pass

def download_files(x0):
 if x0 in files:
  r=requests.get(f"{url}/{x0}")
  status=r.status_code
  if status == 200:
   if not os.path.exists(alm):
    os.makedirs(alm)
   with open(f"{alm}/{x0}", 'wb') as f:
    f.write(r.content)
    f.close()
   if os.path.exists(f"{alm}/{x0}"):
    print(f"{e}{WHITE} DESCARGADO{GREEN} [{x0}]")
   else:
    print(f"{RED}{e}{x0}ERROR {WHITE}[{x0}]")
  else:
   pass
while True:
 try:
  n=1
  try:
   bq=url.find('/*.')
   if url[-4:] == '/pwd':
    url=url[:-4]
   elif url[-3:] == '/..' or url[-3:] == '/ls':
    url=url[:-3]
   elif url[-6:] == '/cd ..' or url[-5:] == '/cd..':
    url='/'.join(url.split('/')[:-2])
   elif url[-2:] == '/*':
    url=url[:-2]
   if bq != -1:
    url=os.path.dirname(url)
   r=requests.get(url)
   st=r.status_code
   if st == 200:
    files.clear()
    pass
   else:
    print(f"{e}{RED}ERROR {WHITE}[{st}]", end=''); input()
    url=os.path.dirname(url)
  except:
   print(f"{e}{WHITE}HA OCURRIDO UN {RED}[ERROR]{WHITE} INESPERADO\n{e}VERIFICA SI TU SERVIDOR PYTHON ESTA ACTIVO")
   break
  soup=b(r.content, 'html.parser')
  buscar=soup.find_all('li')
  print(f"{e}[{GREEN}{url}{RESET}]\n")
  for i in buscar:
   fdirectory=i.text
   listar=f"{WHITE}{e}[{n}]{GREEN} " + fdirectory
   bw=listar[-1]
   if bw == '/':
    print(listar[:-1])
   else:
    print(f"{WHITE}{e}[{n}]{RESET} " + fdirectory)
    files.append(fdirectory)
   n=n+1
  command='/' + input(f'\n{e}===> ')
  x0=(command[1:])
  print("")
  buscar=x0.count('.')
  searchext=x0.find('*.')
  salir(x0)
  if x0 in files:
   download_files(x0)
   files.clear()
   enter()
   continue
  if x0 == '..':
   url='/'.join(url.split('/')[:-1]).replace('/..', '')
  elif x0 == 'pwd':
   print(f"{e}{url}")
   enter()
  elif x0 == '*':
   for zz in files:
    download_files(zz)
   files.clear()
   enter()
  if searchext == 0:
   for i in files:
    extension=x0[1:]
    bext=i.find(extension)
    if bext != -1:
     download_files(i)
   enter()
   files.clear()
  url=f"{url}/{x0}"
 except:
  print(f"\n{e}HASTA LUEGO AMIGO...")
  time.sleep(2)
  salir(x0)

