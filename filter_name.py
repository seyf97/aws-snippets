import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')

filters = [
    {
        'Name': 'instance-state-name',
        'Values': ['running']
    },
    {
        'Name': 'tag:Name', # Name used when creating the instance
        'Values': ['slave']
    }
]

instance_ids = [inst.id for inst in ec2.instances.filter(Filters=filters)]
