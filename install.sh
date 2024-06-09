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
echo -e "[${r1}+${b}] Installing packages...\n"
if pip install rich && pip install pystyle && pip install pillow && pip install piexif && pip install InquirerPy; then
  echo -e "\n[${v1}+${b}] Good news, the packages were installed successfully"
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
  echo "[${r}+${b}] Bad news, we were unable to install the packages on your machine, please try again later."
fi
