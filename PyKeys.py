import random
import os
import sys
import json
import requests
import time
import PyKeyModule
import UpdateCheck
import zipfile
import argparse
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
global iosversion
menu = ConsoleMenu("PyKeys", "Firmware Key Grabber.")


parser = argparse.ArgumentParser()
#parser.prog = 'PyKeys'
parser.description = "Grab Firmware Keys from ipsw.me's API."
parser.epilog = "If you like my software, Follow Me on Github (32Bites) and Twitter (@TheNoahParty)."
parser.add_argument('-i', '--iosversion', help="iOS version. (ex, 7.1.2)")
parser.add_argument('-f', '--imagefile', help="Image file for keys. (ex, RootFS, AppleLogo, BatteryCharging0, etc.) CASESENSITIVE")
parser.add_argument('-d', '--identifier', help="The device identifier. (ex, iPhone3,3)")
parser.add_argument('-m', '--menu', help='Use the interactive menu.', action='store_true')
#parser.parse_args(['--help'])
namespace = parser.parse_args(sys.argv[1:])


def showmenu(applelogom, recoverymodem, batlow1m, batlow0m, batchar1m, llbm, ibootm, ibecm, ibssm, devtreem, glyphplugm, rtfsm, updramm, resramm, glyphchargingm):
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
    menu.append_item(glyphchargingm)
    # Show menu
    menu.show()


def mainmenu():
    #UpdateCheck.inititalize()
    #UpdateCheck.getLocalVersion()
    idt = input("Device Identifier (For example: iPhone3,3)" + Fore.YELLOW + " ! " + Fore.RESET)
    identifier = idt
    iver = input("iOS Version (For example: 7.1.2)" + Fore.YELLOW + " ! " + Fore.RESET)
    iosversion = iver


    validimages = ['AppleLogo', 'RecoveryMode', 'BatteryLow1', 'BatteryLow0', 'BatteryFull', 'BatteryCharging0',
                   'BatteryCharging1', 'LLB', 'iBoot', 'iBEC', 'iBSS', 'DeviceTree', 'GlyphPlugin', 'RootFS', 'UpdateRamdisk', 'RestoreRamdisk', 'GlyphCharging']

    updateStuff = ['Enable Update Check', 'Disable Update Check']

    # Menu Options
    applelogom = FunctionItem(validimages[0], PyKeyModule.getkeys, [
                              validimages[0], identifier, iosversion])
    recoverymodem = FunctionItem(validimages[1], PyKeyModule.getkeys, [
                                 validimages[1], identifier, iosversion])
    batlow1m = FunctionItem(validimages[2], PyKeyModule.getkeys, [
                            validimages[2], identifier, iosversion])
    batlow0m = FunctionItem(validimages[3], PyKeyModule.getkeys, [
                            validimages[3], identifier, iosversion])
    batchar1m = FunctionItem(validimages[4], PyKeyModule.getkeys, [
                             validimages[4], identifier, iosversion])
    llbm = FunctionItem(validimages[5], PyKeyModule.getkeys, [
                        validimages[5], identifier, iosversion])
    ibootm = FunctionItem(validimages[6], PyKeyModule.getkeys, [
                          validimages[6], identifier, iosversion])
    ibecm = FunctionItem(validimages[7], PyKeyModule.getkeys, [
                         validimages[7], identifier, iosversion])
    ibssm = FunctionItem(validimages[8], PyKeyModule.getkeys, [
                         validimages[8], identifier, iosversion])
    devtreem = FunctionItem(validimages[9], PyKeyModule.getkeys, [
                            validimages[9], identifier, iosversion])
    glyphplugm = FunctionItem(validimages[10], PyKeyModule.getkeys, [
                              validimages[10], identifier, iosversion])
    rtfsm = FunctionItem(validimages[11], PyKeyModule.getkeys, [
                         validimages[11], identifier, iosversion])
    updramm = FunctionItem(validimages[12], PyKeyModule.getkeys, [
                           validimages[12], identifier, iosversion])
    resramm = FunctionItem(validimages[13], PyKeyModule.getkeys, [
                           validimages[13], identifier, iosversion])
    glyphchargingm = FunctionItem(validimages[14], PyKeyModule.getkeys, [validimages[14], identifier, iosversion])

    if (UpdateCheck.gupdate == "false"):
        updatecheckm = FunctionItem(updateStuff[0], UpdateCheck.enableUpdate)
        menu.append_item(updatecheckm)
        showmenu(applelogom, recoverymodem, batlow1m, batlow0m, batchar1m, llbm,
                 ibootm, ibecm, ibssm, devtreem, glyphplugm, rtfsm, updramm, resramm, glyphchargingm)

    elif (UpdateCheck.gupdate == "true"):
        updatecheckm = FunctionItem(updateStuff[1], UpdateCheck.disableUpdate)
        menu.append_item(updatecheckm)
        showmenu(applelogom, recoverymodem, batlow1m, batlow0m, batchar1m, llbm,
                 ibootm, ibecm, ibssm, devtreem, glyphplugm, rtfsm, updramm, resramm, glyphchargingm)

    elif (UpdateCheck.gupdate == "update"):
        updatecheckm = FunctionItem(updateStuff[1], UpdateCheck.disableUpdate)
        menu.append_item(updatecheckm)
        updatedownloadm = FunctionItem(
            "Download Update", UpdateCheck.downloadUpdate)
        menu.append_item(updatedownloadm)
        showmenu(applelogom, recoverymodem, batlow1m, batlow0m, batchar1m, llbm,
                 ibootm, ibecm, ibssm, devtreem, glyphplugm, rtfsm, updramm, resramm, glyphchargingm)

    else:
        showmenu(applelogom, recoverymodem, batlow1m, batlow0m, batchar1m, llbm,
                 ibootm, ibecm, ibssm, devtreem, glyphplugm, rtfsm, updramm, resramm, glyphchargingm)


# Standard Python Stuff
if __name__ == "__main__":
    UpdateCheck.inititalize()
    UpdateCheck.getLocalVersion()
    init()

    if(namespace.menu) :
        mainmenu()
    elif (namespace.menu == False and len(sys.argv) > 1) :
        PyKeyModule.getkeys(namespace.imagefile, namespace.identifier, namespace.iosversion)
    else:
        print("No arguments passed.\nExited.")
