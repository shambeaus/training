from f5.bigip import ManagementRoot
import sys

class F5_Tools(object):

    def __init__(object):
        part = ''
        pool_name = ''
        pool_members = ''
        vip_name = ''
        destination_IP = ''


    def create_new_pool(self, mgmt, part, pool_name, pool_members):
        # Check if there is an existing pool
        if mgmt.tm.ltm.pools.pool.exists(partition='Common', name=pool_name):
            print('Pool already exists')
            sys.exit()
        pool = mgmt.tm.ltm.pools.pool.create(partition='Common', name=pool_name, monitor='tcp')
        # Verify pool was created
        if mgmt.tm.ltm.pools.pool.exists(partition='Common', name=pool_name):
            print('Successfully created pool : ' + pool_name)
        else:
            print('something went wrong')
        # Add members to pool
        print('Adding members to pools')
        if self.pool_members:
            for member in self.pool_members:
                pool_member = pool.members_s.members.create(partition='Common', name=member)
                print(' Added member ' + member)
        else:
            print('no members provided')
            sys.exit()



    def create_new_vip(self, partition, vip_name, destination_IP, pool_name):
        if mgmt.tm.ltm.virtuals.virtual.exists(partition=partition, name=vip_name):
            print('Virtual already exists')
            sys.exit()
        virtual = mgmt.tm.ltm.virtuals.virtual.create(partition=partition, name=vip_name, ipProtocol='tcp', pool='pool-third', destination=destination_IP)
        if mgmt.tm.ltm.virtuals.virtual.exists(partition=partition, name=vip_name):
            print('Successfully created VIP : ' + vip_name)
        else:
            print('something went wrong')


