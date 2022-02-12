import os, re

def get_devices():
    with os.popen('arp -a') as arp:
        data = arp.read().splitlines()

    devices = []

    for line in data:
        if line.startswith("mystrom"):
            entry = line.split()
            device = {}
            device['name'] = entry[0]
            device['ip'] = entry[1][1:-1]
            device['mac'] = entry[3]
            devices.append(device)
    
    return devices

get_devices()