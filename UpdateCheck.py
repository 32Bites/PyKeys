import random
import os
import sys
import json
import requests
import time
import PyKeyModule
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

    if (update == "true"):
        if (int(lremoteversion[0]) > int(lversion[0]) or int(lremoteversion[2]) > int(lversion[2]) or int(lremoteversion[4]) > int(lversion[4])):
            print(Fore.GREEN + "Update Available!" + Fore.RESET)
        else:
            print(Fore.GREEN + "No Updates Available." + Fore.RESET)

    else:
        print(Fore.RED + "Update Checks disabled." + Fore.RESET)


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


def load():
    with open('info.json') as f:
        info = json.load(f)

    version = info['version']
    update = info['update']
    return update

def inititalize() :
        global gupdate
        gupdate = load()
