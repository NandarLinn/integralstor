git clone ..../integralstor.git

sudo rm -rf /opt/integralstor/integralstor
sudo cp -r integralstor/ /opt/integralstor/
sudo cp -r integralstor/site-packages/integralstor /usr/local/lib/python3.5/dist-packages/

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
