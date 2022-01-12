OLD ZIP FILE IS PLACED AS /opt/integralstor/integralstor2

git clone ..../integralstor.git

## change in integralstor/site-packages/config.py
change current running path
# in get_branding_root function
change /opt/integralstor/integralstor2/....... to /opt/integralstor/integralstor22

#in integralstor/integral_view/wsgi.py
sys.path.append('/var/integralstor/integralstor') to sys.path.append('/var/integralstor/integralstor2')


sudo cp -r integralstor/ /opt/integralstor/integralstor22
sudo cp -r integralstor/site-packages/integralstor /usr/local/lib/python3.8/dist-packages/

sudo chmod -R 777 /opt/integralstor/integralstor22

python3 /opt/integralstor/integralstor22/manage.py runserver 0.0.0.0:8000

////////////

install packages
cd integralstor/ 
pip3 -r requiements.txt

/// test start
from integralstor import config
import imp
print('integralstor is found')
platform_root, err = config.get_platform_root()
print('Done .....', platform_root)
print(imp.find_module('integralstor'))
////test end

if OK , then ..

cd integralstor/
python3 manage.py migrate
python3 manage.py runserver

////

Extra installation

sudo apt install smartmontools
sudo apt install zfsutils-linux

zfs-pools
----------
sudo nano /etc/sudoers
linn    ALL=(ALL)    NOPASSWD: ALL

create zfs pool

install samba
------
sudo apt install samba smbclient
sudo smbpasswd -a kbuzdar
https://linuxways.net/ubuntu/install-samba-on-ubuntu-20-04-and-share-files-on-linux-and-windows/



/////

