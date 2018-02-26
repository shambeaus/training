import binconver_func
import validIP_func

inputIP = input('Please input your IP:')

validIP = validIP_func.validCheck(inputIP)

if validIP:
    binary = binconver_func.bin_convert(inputIP)
    print('Your IP is valid, following is IP with binary conversion \n' + binary + '\n' + inputIP)
else:
    print('provided invlaid IP')
