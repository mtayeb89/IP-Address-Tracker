import socket
import os
import platform
import subprocess


# Function to get the current device's hostname and IP address
def get_device_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return hostname, ip_address


# Function to ping a device and check if it's online
def ping_device(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip]
    response = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return response == 0


# Function to scan the network and get IPs of active devices
def scan_network(base_ip):
    print(f"Scanning network {base_ip}.0/24...")
    active_ips = []
    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        if ping_device(ip):
            active_ips.append(ip)
            print(f"Device found at: {ip}")
    return active_ips


# Function to save the IP addresses to a file
def save_ips_to_file(ips, filename='ip_addresses.txt'):
    with open(filename, 'w') as f:
        for ip in ips:
            f.write(f"{ip}\n")
    print(f"Active IP addresses saved to {filename}.")


# Main function to track IP addresses
def main():
    # Get the local device's IP
    hostname, ip_address = get_device_ip()
    print(f"Device Hostname: {hostname}")
    print(f"Device IP Address: {ip_address}")

    # Get the base network IP
    base_ip = '.'.join(ip_address.split('.')[:-1])

    # Scan the network and get active IP addresses
    active_ips = scan_network(base_ip)

    # Save the results to a file
    save_ips_to_file(active_ips)


if __name__ == "__main__":
    main()
