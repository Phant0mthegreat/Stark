import os
import cores as c
import banners
import util
from pystyle import Colorate, Colors

try:
  os.system('clear')
  util.plataform()
except KeyboardInterrupt:
  print('\n[#] Program interrupted')
