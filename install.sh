g="${b}\033[1;30m"
b="\033[0m"
b1="$b\033[1;37m"
r="${b}\033[1;31m"
r1="${b}\033[31m"
A="${b}\033[1;34m"
A1="${b}\033[34m"
ac="${b}\e[1;36m"
ac1="${b}\e[36m"
v="${b}\033[1;32m"
v1="${b}\033[32m"
m="$b\033[1;35m"
m1="$b\033[35m"
a="$b\033[1;33m"
a1="$b\033[33m"
cy="$b\033[38;2;23;147;209m"

clear
echo -e "${r}
          ..--
          @@######
            @@######
              @@######
              --######..
mm::          ########MM
MM##++        ########@@
  ####++  ############::
  ######################
  --######################
    ::######################
        mm####mm##############..
                  ##############
                    ##############
                      ##############
                        ##############
                          ##############
                            ##############
                              ##############
                                ##############..
                                  ##############..
                                    ##############
                                      ######    ##
                                        ####    ##
                                          ########
${b}"
echo -e "[${r1}+${b}] Detecting environment...\n"

OS=$(uname -o)
if [ "$OS" == "Android" ]; then
  echo -e "[${v1}+${b}] Termux environment detected.\n"
  
  if apt update && apt install -y libjpeg-turbo pcre libpng zlib; then
    echo -e "\n[${v1}+${b}] Dependencies installed successfully in Termux."
  else
    echo -e "\n[${r1}+${b}] Failed to install dependencies in Termux. Please try manually."
    exit 1
  fi
elif [ "$OS" == "GNU/Linux" ]; then
  echo -e "[${v1}+${b}] Kali Linux environment detected.\n"
  
  if sudo apt update && sudo apt install -y libjpeg-dev libpng-dev zlib1g-dev; then
    echo -e "\n[${v1}+${b}] Dependencies installed successfully in Kali Linux."
  else
    echo -e "\n[${r1}+${b}] Failed to install dependencies in Kali Linux. Please try manually."
    exit 1
  fi
else
  echo -e "[${r1}+${b}] Unknown environment. Exiting..."
  exit 1
fi

if pip install rich pystyle pillow piexif InquirerPy; then
  echo -e "\n[${v1}+${b}] Good news, the packages were installed successfully."
  sleep 2
  echo -e "\nStark will start automatically in a few seconds, if you want to start it again, just go to the repository and type ${r}python3 Stark.py${b}"
  sleep 3
  echo -e "\nStarting in...\n"
  sleep 1
  echo "5"
  sleep 1
  echo "4"
  sleep 1
  echo "3"
  sleep 1
  echo "2"
  sleep 1
  echo "1"
  sleep 1
  clear
  python3 Stark.py
else
  echo "[${r1}+${b}] Bad news, we were unable to install the packages on your machine, please try again later."
fi
