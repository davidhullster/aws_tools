import boto3
import click

session = boto3.Session(profile_name='guest')
ec2 = session.resource('ec2')

@click.command()
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
        print(', '.join((
           i.id,
           i.instance_type,
           i.placement['AvailabilityZone'],
           i.state['Name'],
           i.public_dns_name
        )))

    return

if __name__ == '__main__':
    list_instances()
