import os
import subprocess
import os.path

def apt_get_install(fname):
    with open(fname, 'r') as f:
        items = f.readlines()
    for item in items:
        if item.strip():
            os.system('sudo apt-get install -y %s' % (item))

def npm_global_install(fname):
    with open(fname, 'r') as f:
        items = f.readlines()
    for item in items:
        if item.strip():
            os.system('sudo npm -g install %s' % (item))

def pip_install(fname):
    with open(fname, 'r') as f:
        items = f.readlines()
    for item in items:
        if item.strip():
            os.system('sudo -H pip install %s' % (item))

def cmd_exists(cmd):
    # this is from http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
    return subprocess.call("type " + cmd, shell=True, 
        stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

functions_to_handle_requirements = {}
functions_to_handle_requirements['apt_get'] = apt_get_install
functions_to_handle_requirements['npm'] = npm_global_install
functions_to_handle_requirements['pip'] = pip_install

order_of_files_to_handle = ['apt_get_requirements.txt', 'npm_requirements.txt', 'pip_requirements.txt']

for fname in order_of_files_to_handle:
    if os.path.isfile(fname):
        # assume fname endswith _requirements.txt
        l = len('_requirements.txt')
        fname_first_part = fname[:-l]
        functions_to_handle_requirements[fname_first_part](fname)
        
if os.path.isfile('install.sh'):
    os.system('sh install.sh')