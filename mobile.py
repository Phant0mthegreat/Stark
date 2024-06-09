import os
import cores as c
import banners
from pystyle import Colorate, Colors
from rich.panel import Panel
from rich.console import Console
from InquirerPy import prompt
from InquirerPy.base.control import Choice
from rich.style import Style
import sys
import util

console = Console()

question_style = Style(color="red", bold=True)
choice_style = Style(color="red")
pointer_style = Style(color="red")
selected_style = Style(color="red", bold=True)

questions = [
    {
        "type": "list",
        "name": "choice",
        "message": ("What do you want?"),
        "choices": [
            ("1. Hide message in an image"),
            ("2. Scan image"),
            ("3. Information"),
            ("4. Exit"),
        ],
    }
]


try:
  util.loading_mobile()
  while True:
    os.system('clear')
    print(Colorate.Vertical(Colors.yellow_to_red, banners.banner4))
    answers = prompt(questions, style={
            "question": "fg:ansired bold",
            "pointer": "fg:ansired",
            "highlight": "fg:ansired bold",
            "answer": "fg:ansired bold",
        })
    respost = answers['choice']

    if "1" in respost:
      os.system('clear')
      print(Colorate.Vertical(Colors.yellow_to_red, banners.banner4))
      image_path = input(f"{c.bwhite}[{c.byellow}>{c.bwhite}]{c.white} Enter the path to the image: ")
      message_to_hide = input(f"{c.bwhite}[{c.byellow}>{c.bwhite}]{c.white} Enter the message to be hidden in the image: ")
      if util.hide_message(image_path, message_to_hide):
        print(f"\n{c.green}Message successfully hidden in {image_path} !{c.white}")
        input(f"\n{c.white}Press {c.bwhite}[ENTER]{c.white} to continue")
    elif "2" in respost:
      os.system('clear')
      print(Colorate.Vertical(Colors.yellow_to_red, banners.banner4))
      image_path = input(f"{c.bwhite}[{c.byellow}>{c.bwhite}]{c.white} Enter the path of the image with the hidden message: ")
      message_recovered = util.scan_image_metadata(image_path)
      if message_recovered:
       print(f'\n{message_recovered}')
       input(f"\n{c.white}Press {c.bwhite}[ENTER]{c.white} to continue")
    elif "3" in respost:
      os.system('clear')
      print(Colorate.Vertical(Colors.yellow_to_red, banners.banner2))
      print(f'''{c.bwhite}[{c.byellow}About 📖{c.bwhite}] {c.white}Stark is a tool focused on steganography and image analysis, with varied purposes.\n\n{c.bwhite}[{c.bcyan}Creator Discord 👔{c.bwhite}] {c.white}@phant0mthegreat''')
      input(f"\n{c.white}Press {c.bwhite}[ENTER]{c.white} to continue")
    elif "4" in respost:
      os.system('clear')
      print(Colorate.Vertical(Colors.yellow_to_red, banners.banner3))
      print(f'{c.byellow}Thank you for using Stark')
      sys.exit()
except KeyboardInterrupt:
  print('\n[#] Program interrupted')
