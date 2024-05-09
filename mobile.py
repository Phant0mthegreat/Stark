import os, cores as c, banners
from pystyle import Colorate, Colors
from rich.panel import Panel
from rich.console import Console
import sys
import util
console = Console()

try:
  util.cargm()
  while True:
    os.system('clear')
    print(Colorate.Vertical(Colors.yellow_to_red, banners.banner4))
    console.print(Panel.fit("""{[yellow]1[white]} Hide message in an image\n\n{[yellow]2[white]} Search for messages in an image\n\n{[yellow]3[white]} Information\n\n{[yellow]4[white]} Exit""", title="🔎"))
    respost = input(f'Enter your choice {c.byellow}>{c.white}')
    if respost == '1':
      os.system('clear')
      print(Colorate.Vertical(Colors.yellow_to_red, banners.banner4))
      caminho_da_imagem = input(f"{c.bwhite}[{c.byellow}>{c.bwhite}]{c.white} Enter the path to the image: ")
      mensagem_para_esconder = input(f"{c.bwhite}[{c.byellow}>{c.bwhite}]{c.white} Enter the message to be hidden in the image: ")
      if util.esconder(caminho_da_imagem, mensagem_para_esconder):
        print(f"\n{c.green}Message successfully hidden in {caminho_da_imagem} !{c.white}")
        input(f"\n{c.white}Press {c.bwhite}[ENTER]{c.white} to continue")
    elif respost == '2':
      os.system('clear')
      print(Colorate.Vertical(Colors.yellow_to_red, banners.banner4))
      caminho_da_imagem = input(f"{c.bwhite}[{c.byellow}>{c.bwhite}]{c.white} Enter the path of the image with the hidden message: ")
      mensagem_recuperada = util.acessar(caminho_da_imagem)
      if mensagem_recuperada:
       print(f'\n{mensagem_recuperada}')
       input(f"\n{c.white}Press {c.bwhite}[ENTER]{c.white} to continue")
    elif respost == '3':
      os.system('clear')
      print(Colorate.Vertical(Colors.yellow_to_red, banners.banner2))
      print(f'''{c.bwhite}[{c.byellow}About 📖{c.bwhite}] {c.white}Stark is a tool that uses the metadata steganography method to hide your messages in PNG, JPG and JPEG images. It can be used for encrypted communication, hiding confidential information, etc.
Stark is widely used and you can use it for different purposes, such as hiding your passwords, for example, and even secretly chatting with someone you know.\n\n{c.bwhite}[{c.bcyan}Creator Discord 👔{c.bwhite}] {c.white}@phant0mthegreat''')
      input(f"\n{c.white}Press {c.bwhite}[ENTER]{c.white} to continue")
    elif respost == '4':
      os.system('clear')
      print(Colorate.Vertical(Colors.yellow_to_red, banners.banner3))
      print(f'{c.byellow}Thank you for using Stark')
      sys.exit()
except KeyboardInterrupt:
  print('\n[#] Program interrupted')
