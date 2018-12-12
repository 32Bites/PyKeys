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


'''
--- Written By Noah @CorruptByte
--- Use's ipsw.me's API, thanks Neal.
______________________________________________

-- This script will be improved over time


'''

global identifier

global buildid

def mainmenu():
    validimages = ['AppleLogo', 'RecoveryMode', 'BatteryLow1', 'BatteryLow0', 'BatteryFull', 'BatteryCharging0',
                   'BatteryCharging1', 'LLB', 'iBoot', 'iBEC', 'iBSS', 'DeviceTree', 'GlyphPlugin', 'RootFS', 'UpdateRamdisk', 'RestoreRamdisk']

    menu = ConsoleMenu("PyKeys", "Firmware Key Grabber.")
    # Menu Options
    applelogom = FunctionItem(validimages[0], PyKeyModule.getkeys, [validimages[0], identifier, buildid])
    recoverymodem = FunctionItem(validimages[1], PyKeyModule.getkeys, [validimages[1], identifier, buildid])
    batlow1m = FunctionItem(validimages[2], PyKeyModule.getkeys, [validimages[2], identifier, buildid])
    batlow0m = FunctionItem(validimages[3], PyKeyModule.getkeys, [validimages[3], identifier, buildid])
    batchar1m = FunctionItem(validimages[4], PyKeyModule.getkeys, [validimages[4], identifier, buildid])
    llbm = FunctionItem(validimages[5], PyKeyModule.getkeys, [validimages[5], identifier, buildid])
    ibootm = FunctionItem(validimages[6], PyKeyModule.getkeys, [validimages[6], identifier, buildid])
    ibecm = FunctionItem(validimages[7], PyKeyModule.getkeys, [validimages[7], identifier, buildid])
    ibssm = FunctionItem(validimages[8], PyKeyModule.getkeys, [validimages[8], identifier, buildid])
    devtreem = FunctionItem(validimages[9], PyKeyModule.getkeys, [validimages[9], identifier, buildid])
    glyphplugm = FunctionItem(validimages[10], PyKeyModule.getkeys, [validimages[10], identifier, buildid])
    rtfsm = FunctionItem(validimages[11], PyKeyModule.getkeys, [validimages[11], identifier, buildid])
    updramm = FunctionItem(validimages[12], PyKeyModule.getkeys, [validimages[12], identifier, buildid])
    resramm = FunctionItem(validimages[13], PyKeyModule.getkeys, [validimages[13], identifier, buildid])
    # Add Options to menu
    menu.append_item(applelogom)
    menu.append_item(recoverymodem)
    menu.append_item(batlow1m)
    menu.append_item(batlow0m)
    menu.append_item(batchar1m)
    menu.append_item(llbm)
    menu.append_item(ibootm)
    menu.append_item(ibecm)
    menu.append_item(ibssm)
    menu.append_item(devtreem)
    menu.append_item(glyphplugm)
    menu.append_item(rtfsm)
    menu.append_item(updramm)
    menu.append_item(resramm)
    # Show menu
    menu.show()


# Standard Python Stuff
if __name__ == "__main__":
    init()
    idt = input("Device Identifier (For example: iPhone3,3)" +
                Fore.YELLOW + " ! " + Fore.RESET)
    identifier = idt
    bdid = input("Build ID (For example: 11D257)" +
                 Fore.YELLOW + " ! " + Fore.RESET)
    buildid = bdid
    #print(identifier + " " + buildid)
    mainmenu()
