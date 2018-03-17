from f5.bigip import ManagementRoot
import pprint
import argparse
pp = pprint.PrettyPrinter(indent=3)

mgmt = ManagementRoot("192.168.109.130", "admin", "pass")

parser = argparse.ArgumentParser(description='Script to create a pool on a BIG-IP device')
parser.add_argument("pool_name", help="The name of the pool")
parser.add_argument("pool_members", help="A comma seperated string in the format <IP>:<port>[,<IP>:<port>]")
parser.add_argument("-P", "--partition", help="The partition name", default="Common")
args = parser.parse_args()


mgmt = ManagementRoot("192.168.109.130", "admin", "pass")
print('test')

pool_path = '/{}/{}'.format(args.partition, args.pool_name)


if mgmt.tm.ltm.pools.pool.exists(partition=args.partition, name=args.pool_name):
    raise Exception("Pool '{}}' already exists".format(args.pool_name))

pool = mgmt.tm.ltm.pools.pool.create(partition=args.partition, name=args.pool_name)
print('Created pool ' + pool_path)

member_list = args.pool_members.split(',')

for member in member_list:
    pool_member = pool.members_s.members.create(partition=args.partition, name=member)
    print(' Added member {}'.format(member))