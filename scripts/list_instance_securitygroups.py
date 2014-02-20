#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  simple script to display all security groups
#
#  TODO: allow passing of region as parameter, or allow "all regions",
#  TODO: allow passing of a list of instance ids.
#
# Requires: your boto config file (~/.boto) to contain your aws credentials
#
# [Credentials]
# aws_access_key_id = <your access key>
# aws_secret_access_key = <your secret key>



def main():
	import boto.ec2
	from pprint import pprint
	import sys

	if len(sys.argv) <2:
		print "Usage: ./list_instance_securitygroups.py <instance_id>"
		return 1

	instance_id = sys.argv[1]
	#instance_id = 'i-dbe3f8e6'
	#conn = boto.ec2.connect_to_region("ap-southeast-2")
	conn = boto.ec2.connect_to_region("us-west-2")
	reservations = conn.get_all_reservations(instance_ids=instance_id)
	instances = reservations[0].instances
	print "Instance ID: %s\n" % instance_id
	print "Security Groups:"
	for securityGroup in instances[0].groups:
		print "%s: %s" % (securityGroup.id,securityGroup.name)
		#print pprint(vars(securityGroup))
	return 0

if __name__ == '__main__':
	main()

