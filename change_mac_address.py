import optparse
import subprocess

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface",
                  help="Interface which MAC address will be changed")
parser.add_option("-m", "--mac", dest="mac_address",
                  help="New MAC Address")
(values, arguments) = parser.parse_args()
interface = values.interface
mac_address = values.mac_address


def change_mac_address(interface_value, new_mac, shell=True):
    subprocess.call(f"ifconfig {interface_value} down", shell=shell)
    subprocess.call(f"ifconfig {interface_value} hw ether {new_mac}", shell=shell)
    subprocess.call(f"ifconfig {interface_value} up", shell=shell)

    subprocess.call(f"ifconfig {interface_value}")


# interface = input("enter interface: ")
# mac_address = input("enter mac address: ")
change_mac_address(interface, mac_address)
