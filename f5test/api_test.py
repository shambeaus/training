from f5.bigip import ManagementRoot
import pprint
# Connect to the BigIP
mgmt = ManagementRoot("192.168.109.130", "admin", "test")

vip_sslprofile = {}
cert_key = {}
expiration = {}
final_dic = {}

# Create list of all virtuals and the assigned ssl profiles

virtuals = mgmt.tm.ltm.virtuals.get_collection()

for line in virtuals:    
    virt = mgmt.tm.ltm.virtuals.virtual.load(partition=line.partition, name=line.name)
    vip_sslprofile[line.name] = []
    for profile in virt.profiles_s.get_collection():
        if 'clientside' in profile.context:
            vip_sslprofile[line.name].append(profile.name)


pprint.pprint(vip_sslprofile)

# Create list of all ssl profiles and the assigned cert/key

clientssl = mgmt.tm.ltm.profile.client_ssls.get_collection()

for line in clientssl:
    cert_key[line.name] = {}
    cert_key[line.name] = [line.cert,line.key]

# Create list of all certs with expiration date

certinfo = mgmt.tm.sys.crypto.certs.get_collection()

for line in certinfo:
    expiration[line.name] = line.apiRawValues['expiration']

#Remove VIPs that have no ssl certs applied

for k, v in vip_sslprofile.items():
    if v:
        final_dic[k] = {}

#Compare cert/key with ssl to correlate .crt and .key file

def compare_certvip(dictOne,dictTwo):
    for key in dictOne.items():
        for key2 in dictTwo.items():
            if key[0] in key2[1]:
                final_dic[key2[0]] = key
#
##Compare cert to get expiration date:
#
#def compare_certexpiration(dictOne,dictTwo):
#    for key in dictOne.items():
#        for key2 in dictTwo.items():
#            if key[0] in key2[1]:
#                print(key[1])
#                final_dic[key2[1]].append(key)


compare_certvip(cert_key,vip_sslprofile)
#compare_certexpiration(expiration,cert_key)


print('------------------------------------')
print('------------------------------------')

pprint.pprint(final_dic)





#if vip_sslprofile['sslprofile'].items != None:    
#    for key, value in vip_sslprofile.items():
#        print(key)
#        print(value)


#for line in profiles:
#    clientprofiles = mgmt.tm.ltm.profile.client-ssl.ssl_profile.load(partition=line.partition, name=line.name)
#    print(clientprofiles)
#print(profiles)



#print(vip_sslprofile)


# Get a list of all pools on the BigIP and print their names and their
# members' names
#pools = mgmt.tm.ltm.pools.get_collection()

#print(pools)
#print(dir(pools))
#for line in pools:
#    print(line.name)

#    for member in pool.members_s.get_collection():
#         print(member.name)

#for line in virtuals:    
#    virt = mgmt.tm.ltm.virtuals.virtual.load(partition=line.partition, name=line.name)
#    print(line.name)
#    for profile in virt.profiles_s.get_collection():
#        if 'clientside' in profile.context:
#            vip_sslprofile[line.name] = {}
#            vip_sslprofile[line.name]['sslprofile'] = [profile.name]

# https://devcentral.f5.com/articles/icontrol-rest-cookbook-24575
#https://devcentral.f5.com/questions/adding-client-server-and-ssl-profiles-to-a-vip-via-the-sdk-55771