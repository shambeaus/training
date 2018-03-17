from f5.bigip import ManagementRoot
import sys
from F5_Tools import F5_Tools


mgmt = ManagementRoot("192.168.109.130", "admin", "pass")


partition = 'Common'
pool_name = 'pool-classsfsfdss'
pool_members = ['192.168.5.5:80', '192.168.12.5:80']
public_IP = '5.5.4.52'
nat_IP = '192.168.10.15'
port = '80'
vip_name = 'VS-{}-{}'.format(public_IP,port)
destination_IP = '{}:{}'.format(nat_IP,port)


f5_tools = F5_Tools()

f5_tools.create_new_pool(mgmt, partition, pool_name, pool_members)
