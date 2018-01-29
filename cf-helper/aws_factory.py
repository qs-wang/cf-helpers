import os
import boto3

import logger_factory

logger =  logger_factory.create_logger('cf-helper.logger.factory')

def role_arn_to_session(**kwargs):
    """
    Usage :
        session = role_arn_to_session(
            RoleArn='arn:aws:iam::012345678901:role/example-role',
            RoleSessionName='ExampleSessionName')
        client = session.client('sqs')
    """
    client = boto3.client('sts')
    response = client.assume_role(**kwargs)
    return boto3.Session(
        aws_access_key_id=response['Credentials']['AccessKeyId'],
        aws_secret_access_key=response['Credentials']['SecretAccessKey'],
        aws_session_token=response['Credentials']['SessionToken'])



def create_aws_client(client_name, region='us-east-1'):
    logger.info('Creating aws client for {}'.format(client_name))

    arn = os.environ.get("aws_rolearn")
    session = None
    if not arn:
        session = boto3.Session()
    else:  # This is for local testing. Set AWS_ROLEARN
        session = role_arn_to_session(
            RoleArn=arn,
            RoleSessionName='ExperimentSession'
        )
    

    return session.client(client_name,region_name= region)
