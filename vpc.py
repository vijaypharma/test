import boto3
import time

security_group = 'sg-05a86a257ba98841b'
private_subnet_1 = 'subnet-026c4a23a8c65051a'
private_subnet_2 = 'subnet-0757537ac8f578e34'
staging_name = 'recoverydynamodb-manually

def lambda_configrations_update(security_group,private_subnet_1,private_subnet_2):
    count=0
    try:
        lambda_client = boto3.client('lambda')
        function_name = staging_name
        vpc_config = {
            'SubnetIds': [private_subnet_1 private_subnet_2]:
            'SecurityGroupIds': [security_group]
        }

        response = lambda_client.update_function_configuration(
        FunctionName=function_name,
        VpcConfig=vpc_config
        )
        print("VPC Settings are Update successful!")
        print(response)

    except Exception as e :
        time.sleep(10)
        count=count +1
        lambda_configrations_update(security_group,private_subnet_1,private_subnet_2)
        if(count == 20):
            print("Exceeded maximum retries. Exiting.")
            return
lambda_configrations_update(security_group,private_subnet_1,private_subnet_2)
