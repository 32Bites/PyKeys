import random
import os
import sys
import json
import requests
import time
import PyKeyModule
import zipfile
import shutil
from consolemenu import *
from consolemenu.items import FunctionItem, SubmenuItem, CommandItem
from colorama import init
from colorama import Fore, Back, Style


def getLocalVersion():
    with open('info.json') as f:
        info = json.load(f)

    version = info['version']
    update = info['update']
    getRemoteVersion(update, version)


def getRemoteVersion(update, version):
    url = "https://raw.githubusercontent.com/32Bites/PyKeys/master/info.json"
    response = requests.get(url)
    remoteinfo = json.loads(response.content)
    remoteversion = remoteinfo['version']
    compareVersions(remoteversion, update, version)


def compareVersions(remoteversion, update, version):
    lversion = list(version)
    lremoteversion = list(remoteversion)
    updateavailable = False

    if (update == "true" or update == "update"):
        if (int(lremoteversion[0]) > int(lversion[0]) or int(lremoteversion[2]) > int(lversion[2]) or int(lremoteversion[4]) > int(lversion[4])):
            print(Fore.GREEN + "Update Available!" + Fore.RESET)
            updateavailable = True
            updateAvailableFunc()
        else:
            print(Fore.GREEN + "No Updates Available." + Fore.RESET)

    else:
        print(Fore.RED + "Update Checks disabled." + Fore.RESET)
    return updateavailable


def enableUpdate():
    with open('info.json', 'r+') as f:
        info = json.load(f)
        info['update'] = "true"
        f.truncate(0)
        f.seek(0)
        json.dump(info, f, indent=4)


def disableUpdate():
    with open('info.json', 'r+') as f:
        info = json.load(f)
        info['update'] = "false"
        f.truncate(0)
        f.seek(0)
        json.dump(info, f, indent=4)


def updateAvailableFunc():
    with open('info.json', 'r+') as f:
        info = json.load(f)
        info['update'] = "update"
        f.truncate(0)
        f.seek(0)
        json.dump(info, f, indent=4)


def load():
    with open('info.json') as f:
        info = json.load(f)

    version = info['version']
    update = info['update']
    return update


def inititalize():
    global gupdate
    gupdate = load()
    global updateavailable
    updateavailable = False
    global version
    version = "null"
    global rversion
    rversion = "null"


def downloadUpdate():
    url = "https://github.com/32Bites/PyKeys/archive/master.zip"
    r = requests.get(url, allow_redirects=True)
    open('Updated.zip', 'wb').write(r.content)
    zipfilePath = ("./Updated.zip")
    zip = zipfile.ZipFile(zipfilePath)
    zip.extractall(".")
    zip.close()

    try:
        os.rename('PyKeys-master', 'Update')
        os.remove('./Updated.zip')
        print(Fore.GREEN + "Downloaded Update." + Fore.RESET)

    except OSError:
        shutil.rmtree('PyKeys-master')

    dest = "./"
    src = "./Update"
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if (os.path.isfile(full_file_name)):
            shutil.copy(full_file_name, dest)
    shutil.rmtree("Update")
    print(Fore.MAGENTA + "Done." + Fore.RESET)
    exit()
    # Download File
    # Unzip File
    # Delete Zip File
    # Write Message
    # Exit
