import os
import subproccess

def apt_get_install(what):
    os.system('sudo apt-get install %s' % (what))

def cmd_exists(cmd):
    # this is from http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
    return subprocess.call("type " + cmd, shell=True, 
        stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

def ensure_installed(what, how):
    if 'how' == 'apt-get':
        if not cmd_exists(what):
            apt_get_install(what)

items_to_ensure_installed = []
items_to_ensure_installed.append({'what': 'git', 'how': 'apt-get'})

for item in ensure_installed:
    ensure_installed(**item)