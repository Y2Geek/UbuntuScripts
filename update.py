import os

if os.system("sudo apt update") == 0:
	os.system("sudo apt dist-upgrade -y")
	os.system("sudo apt autoremove -y")

