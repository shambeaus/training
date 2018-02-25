

def validCheck(IP):
    validIP = True

    octets = IP.split('.')
    if len(octets) != 4:
        return False

    for i, octet in enumerate(octets):

        try:
            octets[i] = int(octet)
        except ValueError:
            return False
       
    
    first_octet, second_octet, third_octet, fourth_octet = octets

    if first_octet < 1:
        return False
    elif first_octet > 223:
        return False
    elif first_octet == 127:
        return False

    if first_octet == 169 and second_octet == 254:
        return False

    for octet in (second_octet, third_octet, fourth_octet):
        if (octet < 0) or (octet > 255):
            return False

    return True





check = validCheck('172.168.5.5')

print(check)

