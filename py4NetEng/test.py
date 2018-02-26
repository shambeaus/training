import sys


def bin_convert(IP):
    ip_addr_bin = []
    octets = IP.split(".")

    for octect in octets:

        bin_octet = bin(int(octect))
        bin_octet = bin_octet[2:]

        while True:
            if len(bin_octet) >= 8:
                break
            bin_octet = '0' + bin_octet

        ip_addr_bin.append(bin_octet)
        
    ip_addr_bin = ".".join(ip_addr_bin)
    return ip_addr_bin


inputIP = bin_convert('192.168.5.5')

print(inputIP)

