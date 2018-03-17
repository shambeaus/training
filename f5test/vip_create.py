from f5.bigip import ManagementRoot
import sys
import random

mgmt = ManagementRoot("192.168.109.130", "admin", "pass")


partition = 'Common'
pool_name = 'pool-fdfsfff'
pool_members = ['192.168.5.5:80', '192.168.12.5:80']
public_IP = '5.5.4.5'
nat_IP = '192.168.10.15'
port = '80'
vip_name = 'VS-{}-{}'.format(public_IP,port)
destination_IP = '{}:{}'.format(nat_IP,port)



print(vip_name)



def create_new_pool(partition, pool_name, pool_members):
    # Check if there is an existing pool
    if mgmt.tm.ltm.pools.pool.exists(partition=partition, name=pool_name):
        print('Pool already exists')
        sys.exit()
    pool = mgmt.tm.ltm.pools.pool.create(partition=partition, name=pool_name, monitor='tcp')
    # Verify pool was created
    if mgmt.tm.ltm.pools.pool.exists(partition=partition, name=pool_name):
        print('Successfully created pool : ' + pool_name)
    else:
        print('something went wrong')
    # Add members to pool
    print('Adding members to pools')
    if pool_members:
        for member in pool_members:
            pool_member = pool.members_s.members.create(partition=partition, name=member)
            print(' Added member ' + member)
    else:
        print('no members provided')
        sys.exit()



def create_new_vip(partition, vip_name, destination_IP, pool_name):
    if mgmt.tm.ltm.virtuals.virtual.exists(partition=partition, name=vip_name):
        print('Virtual already exists')
        sys.exit()
    virtual = mgmt.tm.ltm.virtuals.virtual.create(partition=partition, name=vip_name, ipProtocol='tcp', pool='pool-third', destination=destination_IP)
    if mgmt.tm.ltm.virtuals.virtual.exists(partition=partition, name=vip_name):
        print('Successfully created VIP : ' + vip_name)
    else:
        print('something went wrong')



create_new_pool(partition, pool_name, pool_members)

create_new_vip(partition,vip_name,destination_IP,pool_name)
