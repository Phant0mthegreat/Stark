from PIL import Image, PngImagePlugin
import piexif
import time, os, banners, cores as c, sys
from pystyle import Colorate, Colors

def cargm():
    os.system('clear')
    print(Colorate.Vertical(Colors.yellow_to_red, banners.banner3))
    print(f'Starting {c.byellow}Stark{c.white} on your cell phone...')
    time.sleep(2)

def cargp():
    os.system('clear')
    print(Colorate.Vertical(Colors.yellow_to_red, banners.banner3))
    print(f'Starting {c.byellow}Stark{c.white} on your PC...')
    time.sleep(2)

def esconder(caminho_da_imagem, mensagem):
    try:
        if caminho_da_imagem.endswith(".png"):
            img = Image.open(caminho_da_imagem)
            metadata = PngImagePlugin.PngInfo()
            metadata.add_text("Mensagem Oculta", mensagem)
            img.save(caminho_da_imagem, pnginfo=metadata)
        elif caminho_da_imagem.endswith((".jpg", ".jpeg")):
            exif_dict = {"0th": {piexif.ImageIFD.Software: mensagem}}
            exif_bytes = piexif.dump(exif_dict)
            piexif.insert(exif_bytes, caminho_da_imagem)
        else:
            print(f"\n{c.red}[!] Invalid file format")
            input(f"\n{c.white}Press {c.bwhite}[ENTER]{c.white} to continue")
            return

        print(f'\n{c.green}Hidden message successfully added to {caminho_da_imagem}!')
        input(f"\n{c.white}Press {c.bwhite}[ENTER]{c.white} to continue")
    except FileNotFoundError:
        print(f"\n{c.red}[!] File not found")
        input(f"\n{c.white}Press {c.bwhite}[ENTER]{c.white} to continue")
    except Exception as e:
        print(f"\n{c.red}[!] An error occurred (report this error to the creator): {e}")
        input(f"\n{c.white}Press {c.bwhite}[ENTER]{c.white} to continue")

def acessar(caminho_da_imagem):
    try:
        if caminho_da_imagem.endswith(".png"):
            img = Image.open(caminho_da_imagem)
            metadata = img.info
            if "Mensagem Oculta" in metadata:
                return f'{c.green}Message found: {metadata["Mensagem Oculta"]}'
            else:
                return f"{c.red}Message not found."
        elif caminho_da_imagem.endswith((".jpg", ".jpeg")):
            exif_dict = piexif.load(caminho_da_imagem)
            if exif_dict and "0th" in exif_dict and piexif.ImageIFD.Software in exif_dict["0th"]:
                mensagem_bytes = exif_dict["0th"][piexif.ImageIFD.Software]
                mensagem_decodificada = mensagem_bytes.decode("utf-8")
                return f'{c.green}Message found: {mensagem_decodificada}'
            else:
                return f"{c.red}Message not found."
        else:
            print(f"\n{c.red}[!] Invalid file format")
            input(f"\n{c.white}Press {c.bwhite}[ENTER]{c.white} to continue")
            return
    except FileNotFoundError:
        print(f"\n{c.red}[!] File not found")
        input(f"\n{c.white}Press {c.bwhite}[ENTER]{c.white} to continue")
    except Exception as e:
        print(f"\n{c.red}[!] An error occurred (report this error to the creator): {e}")
        input(f"\n{c.white}Press {c.bwhite}[ENTER]{c.white} to continue")

def plataforma():
    try:
        with open("save.txt", "r") as arquivo:
            conteudo = arquivo.read().strip()
            if conteudo == "1":
                os.system('python3 pc.py')
            elif conteudo == "2":
                os.system('python3 mobile.py')
            else:
                print(Colorate.Vertical(Colors.yellow_to_red, banners.banner5))
                escolha = input(f"\nAre you using Stark on a PC {c.bwhite}(1){c.white} or mobile phone{c.bwhite} (2){c.white}?{c.yellow}:{c.white}  ")
                while escolha not in ["1", "2"]:
                    escolha = input(f"\nChoose between 1 and 2 (1 for PC and 2 for mobile){c.yellow}:{c.white} ")
                with open("save.txt", "w") as arquivo:
                    arquivo.write(escolha)
                if escolha == "2":
                    os.system('python3 mobile.py')
                else:
                    os.system('python3 pc.py')
    except FileNotFoundError:
        with open("save.txt", "w") as arquivo:
            print(Colorate.Vertical(Colors.yellow_to_red, banners.banner5))
            escolha = input(f"\nAre you using Stark on a PC {c.bwhite}(1){c.white} or mobile phone{c.bwhite} (2){c.white}?{c.yellow}:{c.white}  ")
            while escolha not in ["1", "2"]:
                escolha = input(f"\nChoose between 1 and 2 (1 for PC and 2 for mobile){c.yellow}:{c.white}  ")
            arquivo.write(escolha)
        if escolha == "2":
            os.system('python3 mobile.py')
        else:
            os.system('python3 pc.py')
