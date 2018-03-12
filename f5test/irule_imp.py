from f5.bigip import ManagementRoot
import pprint
# Connect to the BigIP
mgmt = ManagementRoot("192.168.109.130", "admin", "pass")



VIP = input('Virtual server name:')
newrule = input('New rule name:')

rulelist = {}

virtuals = mgmt.tm.ltm.virtuals.get_collection()

for vip in virtuals:
    if VIP == vip.name:
        rulelist[vip.name] = vip.rules



if rulelist:
    for key in rulelist:
        print('----------------------')
        print('----------------------')
        print('Imlemenation steps:')
        print('modify ltm virtual '+ key +' rules ' + ' '.join(rulelist[key]) + ' ' + newrule) 
        print('----------------------')
        print('----------------------')
        print('Rollback steps:')
        print('modify ltm virtual '+ key +' rules ' + ' '.join(rulelist[key]))
else:
    pprint.pprint('No VIP with provided name')





#for line in rulelist:
#    rulelist[line].replace('/Common/','')
#    print(rulelist[line])

#for vserver in virtuals:
#    print(vserver.name)
#    # Catch an error to avoid a VS with no iRules breaking the script prematurely
#    try:
#        irules = vserver.rules
#    except AttributeError:
#        print('- No iRules on this Virtual Server!')
#    else:
#        for rule in vserver.rules:
#            print('-', rule)