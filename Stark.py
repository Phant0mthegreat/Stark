import os, cores as c, banners, util
from pystyle import Colorate, Colors

try:
  os.system('clear')
  util.plataforma()
except KeyboardInterrupt:
  print('\n[#] Program interrupted')
