import random
import os
import sys
import json
import requests
import time
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

def mainmenu() :
    validimages = ['AppleLogo', 'RecoveryMode', 'BatteryLow1', 'BatteryLow0', 'BatteryFull', 'BatteryCharging0', 'BatteryCharging1', 'LLB', 'iBoot', 'iBEC', 'iBSS', 'DeviceTree', 'GlyphPlugin', 'RootFS', 'UpdateRamdisk', 'RestoreRamdisk']

    menu = ConsoleMenu("PyKeys", "Firmware Key Grabber." )
    #Menu Options
    applelogom = FunctionItem(validimages[0], getkeys, [validimages[0]])
    recoverymodem = FunctionItem(validimages[1], getkeys, [validimages[1]])
    batlow1m = FunctionItem(validimages[2], getkeys, [validimages[2]])
    batlow0m = FunctionItem(validimages[3], getkeys, [validimages[3]])
    batchar1m = FunctionItem(validimages[4], getkeys, [validimages[4]])
    llbm = FunctionItem(validimages[5], getkeys, [validimages[5]])
    ibootm = FunctionItem(validimages[6], getkeys, [validimages[6]])
    ibecm = FunctionItem(validimages[7], getkeys, [validimages[7]])
    ibssm = FunctionItem(validimages[8], getkeys, [validimages[8]])
    devtreem = FunctionItem(validimages[9], getkeys, [validimages[9]])
    glyphplugm = FunctionItem(validimages[10], getkeys, [validimages[10]])
    rtfsm = FunctionItem(validimages[11], getkeys, [validimages[11]])
    updramm = FunctionItem(validimages[12], getkeys, [validimages[12]])
    resramm = FunctionItem(validimages[13], getkeys, [validimages[13]])
    #Add Options to menu
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
    #Show menu
    menu.show()



def getkeys(imagefile) :
    url = 'https://api.ipsw.me/v4/keys/ipsw/' + identifier + '/' + buildid
    #url = 'https://api.ipsw.me/v4/keys/ipsw/iphone3,3/11D257'

    response = requests.get(url)

    try:
        data = json.loads(response.content)

    #This is incase it fails to decode the json if the json is invalid.
    except json.decoder.JSONDecodeError: 
        KeyErrorFunc()

    itemlen = 0
    try:
        itemlen = len(data['keys'])
    except KeyError:
        KeyErrorFunc()



    except:
        print(Fore.RED + "Unkown Error Occured.")
        print("\n\nError Type: " + Fore.LIGHTRED_EX + str(sys.exc_info()) + Fore.RESET)
        print("Exiting.")
        exit()

    #print(itemlen)
    #print(data)
    print("Using URL: " + Fore.LIGHTCYAN_EX + url + Fore.RESET)


    #Get AppleLogo Number from JSON
    try:
        for i in range(0, itemlen, 1) :
            if data['keys'][i]['image'] == "AppleLogo" :
                AppleLogo = i
                
        #Get LLB Number from JSON
        for i in range(0, itemlen, 1) :
            if data['keys'][i]['image'] == "LLB" :
               iLLB = i
               
        #Get iBEC Number from JSON
        for i in range(0, itemlen, 1) :
            if data['keys'][i]['image'] == "iBEC" :
                iBEC = i
                
        #Get iBoot Number from JSON
        for i in range(0, itemlen, 1) :
            if data['keys'][i]['image'] == "iBoot" :
                iBoot = i
                
        #Get iBSS Number from JSON
        for i in range(0, itemlen, 1) :
            if data['keys'][i]['image'] == "iBSS" :
                iBSS = i
                
        #Get RecoveryMode Number from JSON
        for i in range(0, itemlen, 1) :
            if data['keys'][i]['image'] == "RecoveryMode" :
                RecoveryMode = i
                
        #Get BatteryLow0 Number from JSON
        for i in range(0, itemlen, 1) :
            if data['keys'][i]['image'] == "BatteryLow0" :
                BatteryLow0 = i
                
        #Get BatteryLow1 Number from JSON
        for i in range(0, itemlen, 1) :
            if data['keys'][i]['image'] == "BatteryLow1" :
                BatteryLow1 = i
                
        #Get BatteryFull Number from JSON
        for i in range(0, itemlen, 1) :
            if data['keys'][i]['image'] == "BatteryFull" :
                BatteryFull = i
                
        #Get BatteryCharging1 Number from JSON
        for i in range(0, itemlen, 1) :
            if data['keys'][i]['image'] == "BatteryCharging1" :
                BatteryCharging1 = i
                
        #Get DeviceTree Number from JSON
        for i in range(0, itemlen, 1) :
            if data['keys'][i]['image'] == "DeviceTree" :
                DeviceTree = i
                
        #Get BatteryCharging0 Number from JSON
        for i in range(0, itemlen, 1) :
            if data['keys'][i]['image'] == "BatteryCharging0" :
                BatteryCharging0 = i
                
        #Get KernelCache Number from JSON
        for i in range(0, itemlen, 1) :
            if data['keys'][i]['image'] == "KernelCache" :
                KernelCache = i
                
        #Get GlyphPlugin Number from JSON
        for i in range(0, itemlen, 1) :
            if data['keys'][i]['image'] == "GlyphPlugin" :
                GlyphPlugin = i
                
        #Get UpdateRamdisk Number from JSON
        for i in range(0, itemlen, 1) :
            if data['keys'][i]['image'] == "UpdateRamdisk" :
                UpdateRamdisk = i
                
        #Get RestoreRamdisk Number from JSON
        for i in range(0, itemlen, 1) :
            if data['keys'][i]['image'] == "RestoreRamdisk" :
                RestoreRamdisk = i
                
        #Get RootFS Number from JSON
        for i in range(0, itemlen, 1) :
            if data['keys'][i]['image'] == "RootFS" :
                RootFS = i
    
    except TypeError: 
        KeyErrorFunc()

    except:
        print(Fore.MAGENTA + "Unknown Error, outputting Variables:")
        print(Fore.LIGHTBLUE_EX + str(url))
        print(Fore.RED + str(data))
        print(Fore.BLUE + "\n\nError Type: " + Fore.LIGHTRED_EX + str(sys.exc_info()) + Fore.RESET)
        print("Exiting.")
        exit()
    

    #Output
    if imagefile == "AppleLogo" :
        print(Fore.RESET + "Filename: " + Fore.GREEN + data['keys'][AppleLogo]['filename'])
        print(Fore.RESET + "Key: " + Fore.GREEN + data['keys'][AppleLogo]['key'])
        print(Fore.RESET + "IV: " + Fore.GREEN + data['keys'][AppleLogo]['iv'])
    elif imagefile == "BatteryFull" :
        print(Fore.RESET + "Filename: " + Fore.GREEN + data['keys'][BatteryFull]['filename'])
        print(Fore.RESET + "Key: " + Fore.GREEN + data['keys'][BatteryFull]['key'])
        print(Fore.RESET + "IV: " + Fore.GREEN + data['keys'][BatteryFull]['iv'])
    elif imagefile == "BatteryCharging0" :
        print(Fore.RESET + "Filename: " + Fore.GREEN + data['keys'][BatteryCharging0]['filename'])
        print(Fore.RESET + "Key: " + Fore.GREEN + data['keys'][BatteryCharging0]['key'])
        print(Fore.RESET + "IV: " + Fore.GREEN + data['keys'][BatteryCharging0]['iv'])
    elif imagefile == "BatteryCharging1" :
        print(Fore.RESET + "Filename: " + Fore.GREEN + data['keys'][BatteryCharging1]['filename'])
        print(Fore.RESET + "Key: " + Fore.GREEN + data['keys'][BatteryCharging1]['key'])
        print(Fore.RESET + "IV: " + Fore.GREEN + data['keys'][BatteryCharging1]['iv'])
    elif imagefile == "BatteryLow0" :
        print(Fore.RESET + "Filename: " + Fore.GREEN + data['keys'][BatteryLow0]['filename'])
        print(Fore.RESET + "Key: " + Fore.GREEN + data['keys'][BatteryLow0]['key'])
        print(Fore.RESET + "IV: " + Fore.GREEN + data['keys'][BatteryLow0]['iv'])
    elif imagefile == "BatteryLow1" :
        print(Fore.RESET + "Filename: " + Fore.GREEN + data['keys'][BatteryLow1]['filename'])
        print(Fore.RESET + "Key: " + Fore.GREEN + data['keys'][BatteryLow1]['key'])
        print(Fore.RESET + "IV: " + Fore.GREEN + data['keys'][BatteryLow1]['iv'])
    elif imagefile == "LLB" :
        print(Fore.RESET + "Filename: " + Fore.GREEN + data['keys'][iLLB]['filename'])
        print(Fore.RESET + "Key: " + Fore.GREEN + data['keys'][iLLB]['key'])
        print(Fore.RESET + "IV: " + Fore.GREEN + data['keys'][iLLB]['iv'])
    elif imagefile == "iBoot" :
        print(Fore.RESET + "Filename: " + Fore.GREEN + data['keys'][iBoot]['filename'])
        print(Fore.RESET + "Key: " + Fore.GREEN + data['keys'][iBoot]['key'])
        print(Fore.RESET + "IV: " + Fore.GREEN + data['keys'][iBoot]['iv'])
    elif imagefile == "iBEC" :
        print(Fore.RESET + "Filename: " + Fore.GREEN + data['keys'][iBEC]['filename'])
        print(Fore.RESET + "Key: " + Fore.GREEN + data['keys'][iBEC]['key'])
        print(Fore.RESET + "IV: " + Fore.GREEN + data['keys'][iBEC]['iv'])
    elif imagefile == "iBSS" :
        print(Fore.RESET + "Filename: " + Fore.GREEN + data['keys'][iBSS]['filename'])
        print(Fore.RESET + "Key: " + Fore.GREEN + data['keys'][iBSS]['key'])
        print(Fore.RESET + "IV: " + Fore.GREEN + data['keys'][iBSS]['iv'])
    elif imagefile == "DeviceTree" :
        print(Fore.RESET + "Filename: " + Fore.GREEN + data['keys'][DeviceTree]['filename'])
        print(Fore.RESET + "Key: " + Fore.GREEN + data['keys'][DeviceTree]['key'])
        print(Fore.RESET + "IV: " + Fore.GREEN + data['keys'][DeviceTree]['iv'])
    elif imagefile == "RecoveryMode" :
        print(Fore.RESET + "Filename: " + Fore.GREEN + data['keys'][RecoveryMode]['filename'])
        print(Fore.RESET + "Key: " + Fore.GREEN + data['keys'][RecoveryMode]['key'])
        print(Fore.RESET + "IV: " + Fore.GREEN + data['keys'][RecoveryMode]['iv'])
    elif imagefile == "GlyphPlugin" :
        print(Fore.RESET + "Filename: " + Fore.GREEN + data['keys'][GlyphPlugin]['filename'])
        print(Fore.RESET + "Key: " + Fore.GREEN + data['keys'][GlyphPlugin]['key'])
        print(Fore.RESET + "IV: " + Fore.GREEN + data['keys'][GlyphPlugin]['iv'])
    elif imagefile == "UpdateRamdisk" :
        print(Fore.RESET + "Filename: " + Fore.GREEN + data['keys'][UpdateRamdisk]['filename'])
        print(Fore.RESET + "Key: " + Fore.GREEN + data['keys'][UpdateRamdisk]['key'])
        print(Fore.RESET + "IV: " + Fore.GREEN + data['keys'][UpdateRamdisk]['iv'])
    elif imagefile == "RestoreRamdisk" :
        print(Fore.RESET + "Filename: " + Fore.GREEN + data['keys'][RestoreRamdisk]['filename'])
        print(Fore.RESET + "Key: " + Fore.GREEN + data['keys'][RestoreRamdisk]['key'])
        print(Fore.RESET + "IV: " + Fore.GREEN + data['keys'][RestoreRamdisk]['iv'])
    elif imagefile == "RootFS" :
        print(Fore.RESET + "Filename: " + Fore.GREEN + data['keys'][RootFS]['filename'])
        print(Fore.RESET + "Key: " + Fore.GREEN + data['keys'][RootFS]['key'])
    exit()

    

def KeyErrorFunc() :
    print(Fore.RED + "Error Processing:")
    print(Fore.MAGENTA + "The information provided is invalid.")
    print("Look at them below:")


        #Checks to see if any of the vars are empty, if so output a message and exit.
    if (len(identifier) == 0 and len(buildid) == 0) :
        print("Some of the input you provided is empty:")
        print(Fore.BLUE + "Identifier: " + Fore.LIGHTBLUE_EX + identifier)
        print(Fore.BLUE + "Buildid: " + Fore.LIGHTBLUE_EX + identifier + Fore.RESET)
        exit()

    print(Fore.BLUE + "Identifier: " + Fore.LIGHTBLUE_EX + identifier)
    print(Fore.BLUE + "Buildid: " + Fore.LIGHTBLUE_EX + identifier + Fore.RESET)
    print("Exiting.")
    exit()



#Standard Python Stuff
if __name__ == "__main__" :
    init()
    idt = input("Device Identifier (For example: iPhone3,3)" + Fore.YELLOW + " ! " + Fore.RESET)
    identifier = idt
    bdid = input("Build ID (For example: 11D257)" + Fore.YELLOW + " ! " + Fore.RESET)
    buildid = bdid
    #print(identifier + " " + buildid)
    mainmenu()
