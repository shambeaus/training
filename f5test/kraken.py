from f5.bigip import ManagementRoot
import sys
from F5_Tools import F5_Tools
import requests


mgmt = ManagementRoot("192.168.109.130", "admin", "pass")


partition = 'Common'
pool_members = ['192.168.5.5:80', '192.168.12.5:80']
public_IP = '12.5.4.7'
nat_IP = '192.168.10.55'
port = '80'
vip_name = 'VS-{}-{}'.format(public_IP,port)
destination_IP = '{}:{}'.format(nat_IP,port)
pool_name = 'POOL-{}-{}'.format(public_IP,port)

virtuals_data = mgmt.tm.ltm.virtuals.get_collection()
pools_data = mgmt.tm.ltm.pools.get_collection()
qc_data = [vip_name, pool_name, destination_IP]

f5_tools = F5_Tools()

f5_tools.qc_vip(virtuals_data, pools_data, vip_name, destination_IP, pool_name)

f5_tools.create_new_pool(mgmt, partition, pool_name, pool_members)

f5_tools.create_new_vip(mgmt, virtuals_data, partition, vip_name, destination_IP, pool_name)

