import boto3
import click

profile_input = input("Enter --profile value: ")

session = boto3.Session(profile_name=profile_input)
ec2 = session.resource('ec2')

@click.group()
def instances():
    """Commands for instances"""

@instances.command('list')
@click.option('--name', default=None,
    help="Only instances for name (tag Name:<name>)")
def list_instances(name):
    "List EC2 instances"
    instances = []

    if name:
        filters = [{'Name':'tag:Name', 'Values':[name]}]
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
           i.public_dns_name,
           i.private_ip_address,
           tags.get('Name', '<no tag "Name">')
        )))

    return

if __name__ == '__main__':
    instances()
