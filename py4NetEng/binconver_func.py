
def zeropad(IP):
    #Pad converted IP with leading zeros
    while True:
        if len(IP) >= 8:
            break
        IP = '0' + IP
    return IP

def bin_convert(IP):
    ip_addr_bin = []
    octets = IP.split(".")

    for octect in octets:
        #slice leading characters
        bin_octet = bin(int(octect))
        bin_octet = bin_octet[2:]

        bin_octet = zeropad(bin_octet)

        ip_addr_bin.append(bin_octet)
        
    ip_addr_bin = ".".join(ip_addr_bin)
    return ip_addr_bin

