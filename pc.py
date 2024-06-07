import os
import cores as c
import banners
from pystyle import Colorate, Colors
from rich.panel import Panel
from rich.console import Console
import sys
import util
console = Console()

try:
  util.loading_pc()
  while True:
    os.system('clear')
    print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
    console.print(Panel.fit("""{[yellow]1[white]} Hide message in an image\n\n{[yellow]2[white]} Scan image\n\n{[yellow]3[white]} Information\n\n{[yellow]4[white]} Exit""",padding=(0, 40), title="🔎"))
    respost = input(f'Enter your choice {c.byellow}>{c.white}')
    if respost == '1':
      os.system('clear')
      print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
      image_path = input(f"{c.bwhite}[{c.byellow}>{c.bwhite}]{c.white} Enter the path to the image: ")
      message_to_hide = input(f"{c.bwhite}[{c.byellow}>{c.bwhite}]{c.white} Enter the message to be hidden in the image: ")
      if util.hide_message(image_path, message_to_hide):
        print(f"\n{c.green}Message successfully hidden in {image_path} !{c.white}")
        input(f"\n{c.white}Press {c.bwhite}[ENTER]{c.white} to continue")
    elif respost == '2':
      os.system('clear')
      print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
      image_path = input(f"{c.bwhite}[{c.byellow}>{c.bwhite}]{c.white} Enter the path of the image with the hidden message: ")
      message_recovered = util.scan_image_metadata(image_path)
      if message_recovered:
       print(f'\n{message_recovered}')
       input(f"\n{c.white}Press {c.bwhite}[ENTER]{c.white} to continue")
    elif respost == '3':
      os.system('clear')
      print(Colorate.Vertical(Colors.yellow_to_red, banners.banner2))
      print(f'''{c.bwhite}[{c.byellow}About 📖{c.bwhite}] {c.white}Stark is a tool focused on steganography and image analysis, with varied purposes.\n\n{c.bwhite}[{c.bcyan}Creator Discord 👔{c.bwhite}] {c.white}@phant0mthegreat''')
      input(f"\n{c.white}Press {c.bwhite}[ENTER]{c.white} to continue")
    elif respost == '4':
      os.system('clear')
      print(Colorate.Vertical(Colors.yellow_to_red, banners.banner3))
      print(f'{c.byellow}Thank you for using Stark')
      sys.exit()
except KeyboardInterrupt:
  print('\n[#] Program interrupted')
