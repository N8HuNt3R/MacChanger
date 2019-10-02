#!usr/bin/python
import subprocess
from termcolor import colored


print(" _         _____                     _       _________ ______   _______ ")
print("( (    /| / ___ \ |\     /||\     /|( (    /|\__   __// ___  \ (  ____ )")
print("|  \  ( |( (___) )| )   ( || )   ( ||  \  ( |   ) (   \/   \  \| (    )|")
print("|   \ | | \     / | (___) || |   | ||   \ | |   | |      ___) /| (____)|")
print("| (\ \) | / ___ \ |  ___  || |   | || (\ \) |   | |     (___ ( |     __)")
print("| | \   |( (   ) )| (   ) || |   | || | \   |   | |         ) \| (\ (   ")
print("| )  \  |( (___) )| )   ( || (___) || )  \  |   | |   /\___/  /| ) \ \__")
print("|/    )_) \_____/ |/     \|(_______)|/    )_)   )_(   \______/ |/   \__/")
                                                                        

def change_mac_address(interface,mac):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac])
    subprocess.call(["ifconfig",interface,"up"])


def main():
    interface = str(input("[*] Enter Interface To Change Mac Address On: "))
    new_mac_address = input("[*] Enter Your New Mac Address That You Want: ")
	

    before_change = subprocess.check_output(["ifconfig",interface])

    change_mac_address(interface,new_mac_address)

    after_change = subprocess.check_output(["ifconfig",interface])


    if before_change == after_change:
        print(colored("[-] Failed To Changed Mac Address To: " + new_mac_address, 'red'))

    else:
        print(colored("[+] Mac Address Successfully Changed To: " + new_mac_address + "On Interface" + interface, 'green'))

main()