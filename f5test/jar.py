from f5.bigip import ManagementRoot
import pprint
# Connect to the BigIP
mgmt = ManagementRoot("192.168.109.130", "admin", "pass")
# Create list of all virtuals and the assigned ssl profiles

virtuals = mgmt.tm.ltm.virtuals.get_collection()

for line in virtuals:    
    virt = mgmt.tm.ltm.virtuals.virtual.load(partition=line.partition, name=line.name)
    vip_sslprofile[line.name] = [
        profile.name
        for profile in virt.profiles_s.get_collection()
        if 'clientside' in profile.context
    ]


pprint.pprint(vip_sslprofile)

# Create list of all ssl profiles and the assigned cert/key
cert_key = {}
clientssl = mgmt.tm.ltm.profile.client_ssls.get_collection()

for line in clientssl:
    cert_key[line.name] = {line.cert: line.key}

# Create list of all certs with expiration date
expiration = {}
certinfo = mgmt.tm.sys.crypto.certs.get_collection()

for line in certinfo:
    expiration[line.name] = line.apiRawValues['expiration']

#Remove VIPs that haveno ssl certs applied

#Compare cert/key with ssl to correlate .crt and .key file

def compare_certvip(cert, profile):
    final_dic = {}
    
    for profile_names in filter(lambda v: v, vip_sslprofile.values()):
        for cert_key in cert.keys():
            for (prof_key, prof_val) in profile.items():
                if cert_key in prof_key:
                    final_dic[prof_val] = key


compare_certvip(cert_key, vip_sslprofile)
#compare_certexpiration(expiration,cert_key)


print('------------------------------------')
print('------------------------------------')

#pprint.pprint(final_dic)