import re

f = open("r1")

fileread = f.readlines()

for line in fileread:
    data = re.findall(r"IP address: (.+)", line)
    device = re.findall(r"Device ID: (.+)", line)
    platform = re.findall(r"Platform: (.+?) (.+)", line)
    cap= re.findall(r"Capabilities: (.+?) ", line)

    if data:
        print(data)
    if device:
        print(device)
    if platform:
        print(platform)
    if cap:
        print(cap)



# >>> z = re.findall(r"Platform: (.+?) (.+?), Capabilities: (.+)", cdp_data)
# >>> for vendor, model, device in z:
# ...     print(vendor)
# ...     print(model)
# ...     print(device)