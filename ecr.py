import boto3

ecr_client = boto3.client('ecr')

repository_name = 'cloud_native_monitoring_app'
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(f"Repository URI: {repository_uri}")