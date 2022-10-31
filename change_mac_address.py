import optparse
import subprocess


def get_command_line_parameters():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface which MAC address will be changed")
    parser.add_option("-m", "--mac", dest="mac_address",
                      help="New MAC Address")
    (values, arguments) = parser.parse_args()
    if not values.interface:
        parser.error("Please enter an interface. Type --help for info")
    elif not values.mac_address:
        parser.error("Please enter a MAC address. Type --help for info")
    return values


def change_mac_address(interface_value, new_mac, shell=True):
    subprocess.call(f"ifconfig {interface_value} down", shell=shell)
    subprocess.call(f"ifconfig {interface_value} hw ether {new_mac}", shell=shell)
    subprocess.call(f"ifconfig {interface_value} up", shell=shell)
    subprocess.call(["ifconfig", f"{interface_value}"])


values = get_command_line_parameters()
interface = values.interface
mac_address = values.mac_address
change_mac_address(interface, mac_address)
