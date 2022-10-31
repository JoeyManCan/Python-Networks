import optparse
import subprocess

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest = "interface",
                  help = "Interface which MAC address will be changed")
parser.add_option("-m", "--mac", dest = "new_mac",
                  help = "New MAC Address")
parser.parse_args()

def change_mac_address(interface, new_mac, shell = True):
    subprocess.call(f"ifconfig {interface} down", shell = shell)
    subprocess.call(f"ifconfig {interface} hw ether {new_mac}", shell = shell)
    subprocess.call(f"ifconfig {interface} up", shell = shell)


interface = input("enter interface: ")
mac_address = input("enter mac address: ")
change_mac_address(interface,mac_address)
