import platform
import os
import time
from PIL import Image, PngImagePlugin
import piexif
import banners
import cores as c
from pystyle import Colorate, Colors

VERSION = "2.0.3"

def loading_mobile():
    os.system('clear')
    print(Colorate.Vertical(Colors.yellow_to_red, banners.banner3))
    print(f'Starting {c.byellow}Stark{c.white} on your cell phone...')
    time.sleep(2)

def loading_pc():
    os.system('clear')
    print(Colorate.Vertical(Colors.yellow_to_red, banners.banner3))
    print(f'Starting {c.byellow}Stark{c.white} on your PC...')
    time.sleep(2)

def hide_message(caminho_da_imagem, mensagem):
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
        elif caminho_da_imagem.endswith(".webp"):
            img = Image.open(caminho_da_imagem)
            metadata = PngImagePlugin.PngInfo()
            metadata.add_text("Mensagem Oculta", mensagem)
            img.save(caminho_da_imagem, "WEBP", pnginfo=metadata)
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

def decode_exif(exif_bytes):
    exif_data = piexif.load(exif_bytes)
    exif_info = {}
    for ifd in exif_data:
        if exif_data[ifd] is not None:
            for tag in exif_data[ifd]:
                tag_name = piexif.TAGS[ifd][tag]["name"]
                value = exif_data[ifd][tag]
                if isinstance(value, bytes):
                    try:
                        value = value.decode("utf-8", errors="ignore")
                    except UnicodeDecodeError:
                        value = value.decode("latin1", errors="ignore")
                exif_info[tag_name] = value
    return exif_info

def scan_image_metadata(caminho_da_imagem):
    if not os.path.isfile(caminho_da_imagem):
        print(f"\n{c.red}[!] The path provided is not a file.")
        input(f"\n{c.white}Press {c.bwhite}[ENTER]{c.white} to continue")
        return

    if not caminho_da_imagem.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        print(f"\n{c.red}[!] Unsupported file format")
        input(f"\n{c.white}Press {c.bwhite}[ENTER]{c.white} to continue")
        return

    try:
        file_info = os.stat(caminho_da_imagem)
        file_size = file_info.st_size
        last_modified = time.ctime(file_info.st_mtime)
        absolute_path = os.path.abspath(caminho_da_imagem)

        print(f"\n{c.yellow}File Information:")
        print(f"{c.white}Path: {absolute_path}")
        print(f"Size: {file_size} bytes")
        print(f"Last Modified: {last_modified}")

        img = Image.open(caminho_da_imagem)
        width, height = img.size
        color_mode = img.mode

        print(f"Dimensions: {width} x {height} pixels")
        print(f"Color Mode: {color_mode}")

        if caminho_da_imagem.endswith(".png"):
            metadata = img.info
            print(f"\n{c.yellow}Metadata:")
            for key, value in metadata.items():
                print(f"{c.white}{key}: {value}")

            if "Mensagem Oculta" in metadata:
                print(f"\n{c.green}Message found: {metadata['Mensagem Oculta']}")
            else:
                print(f"\n{c.red}Message not found.")

        elif caminho_da_imagem.endswith((".jpg", ".jpeg")):
            exif_data = img.info.get("exif")
            if exif_data:
                exif_dict = piexif.load(exif_data)
                print(f"\n{c.yellow}EXIF Data:")
                for ifd in exif_dict:
                    if exif_dict[ifd] is not None:
                        for tag in exif_dict[ifd]:
                            tag_name = piexif.TAGS[ifd].get(tag, {"name": tag})["name"]
                            value = exif_dict[ifd][tag]
                            if isinstance(value, bytes):
                                try:
                                    value = value.decode("utf-8", errors="ignore")
                                except UnicodeDecodeError:
                                    value = value.decode("latin1", errors="ignore")
                            print(f"{c.white}{tag_name}: {value}")

                if "0th" in exif_dict and piexif.ImageIFD.Software in exif_dict["0th"]:
                    mensagem_bytes = exif_dict["0th"][piexif.ImageIFD.Software]
                    if isinstance(mensagem_bytes, bytes):
                        mensagem_decodificada = mensagem_bytes.decode("utf-8", errors="ignore")
                    else:
                        mensagem_decodificada = mensagem_bytes
                    print(f"\n{c.green}Message found: {mensagem_decodificada}")
                else:
                    print(f"\n{c.red}Message not found.")
            else:
                print(f"\n{c.red}No EXIF data found.")

        elif caminho_da_imagem.endswith(".webp"):
            metadata = img.info
            print(f"\n{c.yellow}Metadata:")
            for key, value in metadata.items():
                if key == "exif":
                    exif_info = decode_exif(value)
                    for tag_name, tag_value in exif_info.items():
                        print(f"{c.white}{tag_name}: {tag_value}")
                else:
                    print(f"{c.white}{key}: {value}")

            if "Mensagem Oculta" in metadata:
                print(f"\n{c.green}Message found: {metadata['Mensagem Oculta']}")
            else:
                print(f"\n{c.red}Message not found.")

        else:
            print(f"\n{c.red}[!] Invalid file format")
            input(f"\n{c.white}Press {c.bwhite}[ENTER]{c.white} to continue")
            return

        input(f"\n{c.white}Press {c.bwhite}[ENTER]{c.white} to continue")
    except FileNotFoundError:
        print(f"\n{c.red}[!] File not found")
        input(f"\n{c.white}Press {c.bwhite}[ENTER]{c.white} to continue")
    except Exception as e:
        print(f"\n{c.red}[!] An error occurred (report this error to the creator): {e}")
        input(f"\n{c.white}Press {c.bwhite}[ENTER]{c.white} to continue")

def plataform():
    try:
        with open("save.txt", "r") as arquivo:
            conteudo = arquivo.read().strip()
    except FileNotFoundError:
        conteudo = None

    if conteudo not in ["1", "2"]:
        os_name = platform.system().lower()
        if "TERMUX_VERSION" in os.environ or "android" in os_name or "ios" in os_name:
            escolha = "2"
        else:
            escolha = "1"

        with open("save.txt", "w") as arquivo:
            arquivo.write(escolha)
    else:
        escolha = conteudo

    if escolha == "2":
        os.system('python3 mobile.py')
    else:
        os.system('python3 pc.py')
