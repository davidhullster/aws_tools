#!/usr/local/bin/python3
import boto3
import click

'''
include an option for eiamCli login in the script
have the script automatically refresh temporary credentials (timer? after expiration?)
have the script auto-ssh into an instance based on service name (how to decide which instance?)
have the script create one-click tunnels into databases and windows RDP
'''

def create_session(profile):
    az = 'us-west-2'
    session = boto3.Session(profile_name=profile)
    ec2 = boto3.resource('ec2', region_name=az)
    return ec2

def filter_instances(tag, resource, az):
    instances = []

    if tag:
        filters = [{'Name':'tag:Name', 'Values':[tag]}]
        instances = resource.instances.filter(Filters=filters)
    else:
        instances = resource.instances.all()

    return instances

@click.group()
def instances():
    """Commands for instances"""

@instances.command('ip')
@click.option('--tag', default='*',
    help="Only instances with tag (Name:<name>) - default: '*'")
@click.option('--profile', default='default',
    help="Optional AWS auth profile - default: 'default'")
@click.option('--az', default='us-west-2',
    help="Optional AWS Availability Zone - default: us-west-2")

def list_instance_ips(tag, profile, az):
    "List EC2 ip addresses"

    ec2 = boto3.resource('ec2', region_name=az)
    instances = filter_instances(tag,create_session(profile),az)

    if tag:
        filters = [{'Name':'tag:Name', 'Values':[tag]}]
        instances = ec2.instances.filter(Filters=filters)
                   
    else:
        instances = ec2.instances.all()

    for i in instances:
        tags = { t['Key']: t['Value'] for t in i.tags or [] }
        print(', '.join((
           "PvtIP: " + str(i.private_ip_address),
           "PubIP: " + str(i.public_ip_address),
        )))

    return

@instances.command('list')
@click.option('--tag', default='*',
    help="Only instances for tag (Name:<name>) - default: '*'")
@click.option('--profile', default='default',
    help="Optional AWS auth profile - default: 'default'")
@click.option('--az', default='us-west-2',
    help="Optional AWS Availability Zone - default: us-west-2")
def list_instances(tag, profile, az):
    "List EC2 instances"

    ec2 = boto3.resource('ec2', region_name=az)
    instances = filter_instances(tag,create_session(profile),az)

    if tag:
        filters = [{'Name':'tag:Name', 'Values':[tag]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()

    for i in instances:
        tags = { t['Key']: t['Value'] for t in i.tags or [] }
        print(', '.join((
           i.id,
           i.instance_type,
           i.placement['AvailabilityZone'],
           i.state['Name'],
           str(i.private_ip_address),
           str(i.public_ip_address),
           i.launch_time.strftime("%a %x %X"),
           tags.get('Name', '<no project>')
        )))

    return

if __name__ == '__main__':
    instances()
