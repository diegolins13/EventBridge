import boto3
region = boto3.session.Session().region_name
ec2_client = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    action = event.get('action')
    instanceIds = event.get('instanceIds')
    if action == 'start':
        ec2_client.start_instances(
            InstanceIds=instanceIds
            )
        print(f'Instancias {instanceIds} foram iniciadas.')
    elif action == 'stop':
        ec2_client.stop_instances(
            InstanceIds=instanceIds
            )
        print(f'Instancias {instanceIds} foram desligadas.')