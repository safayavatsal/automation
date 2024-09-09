import boto3

ec2 = boto3.client('ec2')

response = ec2.run_instances(
    ImageId='ami-0abcdef1234567890',  # Replace with your AMI ID
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='your-key-pair',
    SecurityGroupIds=['sg-0abcd1234efgh5678'],
    UserData='''#!/bin/bash
                yum update -y
                yum install -y httpd
                systemctl start httpd
                systemctl enable httpd
                echo "Hello World" > /var/www/html/index.html
             '''
)

instance_id = response['Instances'][0]['InstanceId']
