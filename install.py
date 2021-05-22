import os

def update():
    # Update systm first
    os.system("python3 update.py")

update()

# Now lets start install apt software
packages = [
    'variety',
    'gnome-tweaks',
    'ubuntu-restricted-extras',
    'geany',
    'vlc',
    'gimp',
    'git',
    'python3-pip',
    'virtualbox',
    'virtualbox-dkms',
    'gthumb', ]

to_install = ""
for package in packages:
    to_install += package + " "

os.system(f"sudo apt install {to_install} -y")


# Now lets install snap packages
packages = [
    'chromium --classic',
    'code --classic',]

for package in packages:
    os.system(f"sudo snap install {package}")


# Lets install any .deb files
for file in os.listdir(os.getcwd()):
    if file.endswith('.deb'):
        os.system(f"sudo dpkg -i {file}")

# Run another update in case deb files are out of date
update()

restart = input("All done, would you like to restart the machine? ")
if restart.lower() == 'y':
    os.system("sudo reboot")
