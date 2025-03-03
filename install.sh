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
echo -e "${r}\nDetecting environment...\n"

OS=$(uname -o)
DISTRO=""
if [ "$OS" == "Android" ]; then
    echo -e "${b}[${v1}+${b}] Termux environment detected.\n"
    DISTRO="Termux"
elif [ -f /etc/os-release ]; then
    . /etc/os-release
    if [[ "$ID" == "kali" ]]; then
        echo -e "${b}[${v1}+${b}] Kali Linux environment detected.\n"
        DISTRO="Kali"
    elif [[ "$ID" == "ubuntu" ]]; then
        echo -e "${b}[${v1}+${b}] Ubuntu environment detected.\n"
        DISTRO="Ubuntu"
    else
        echo -e "${b}[${r1}+${b}] Unknown Linux distribution: $ID. Exiting..."
        exit 1
    fi
else
    echo -e "${b}[${r1}+${b}] Unknown environment. Exiting..."
    exit 1
fi

if [ "$DISTRO" == "Termux" ]; then
    pkg update -y && pkg install -y libjpeg-turbo pcre libpng zlib python
elif [ "$DISTRO" == "Kali" ]; then
    sudo apt update -y && sudo apt install -y libjpeg-dev libpng-dev zlib1g-dev python3-pip
elif [ "$DISTRO" == "Ubuntu" ]; then
    sudo apt update -y && sudo apt install -y libjpeg-dev libpng-dev zlib1g-dev python3-pip python3-venv
    python3 -m venv stark_env
    source stark_env/bin/activate
else
    echo -e "${b}[${r1}+${b}] Unsupported environment. Exiting..."
    exit 1
fi

if pip install rich pystyle pillow piexif InquirerPy; then
    echo -e "\n${b}[${v1}+${b}] Dependencies installed successfully."
    sleep 2
    echo -e "\n[${v1}+${b}] Starting Stark in 5 seconds..."
    for i in {5..1}; do
        echo "$i"
        sleep 1
    done
    python3 Stark.py
else
    echo -e "\n${b}[${v1}+${b}] Failed to install Python packages. Try again later."
    exit 1
fi
