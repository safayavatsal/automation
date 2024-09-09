import boto3

asg = boto3.client('autoscaling')
ec2 = boto3.client('ec2')

# Launch Configuration
response = asg.create_launch_configuration(
    LaunchConfigurationName='my-launch-configuration',
    ImageId='ami-0abcdef1234567890',
    InstanceType='t2.micro',
    SecurityGroups=['sg-0abcd1234efgh5678'],
    UserData='''#!/bin/bash
                yum update -y
                yum install -y httpd
                systemctl start httpd
                systemctl enable httpd
                echo "Hello World" > /var/www/html/index.html
             '''
)

# Auto Scaling Group
response = asg.create_auto_scaling_group(
    AutoScalingGroupName='my-auto-scaling-group',
    LaunchConfigurationName='my-launch-configuration',
    MinSize=1,
    MaxSize=3,
    DesiredCapacity=1,
    VPCZoneIdentifier='subnet-0123456789abcdef0,subnet-abcdef0123456789',
    Tags=[{'Key': 'Name', 'Value': 'my-auto-scaling-group', 'PropagateAtLaunch': True}]
)

# Scaling Policy
asg.put_scaling_policy(
    AutoScalingGroupName='my-auto-scaling-group',
    PolicyName='scale-out-policy',
    PolicyType='SimpleScaling',
    ScalingAdjustment=1,
    AdjustmentType='ChangeInCapacity',
    Cooldown=300
)

asg.put_scaling_policy(
    AutoScalingGroupName='my-auto-scaling-group',
    PolicyName='scale-in-policy',
    PolicyType='SimpleScaling',
    ScalingAdjustment=-1,
    AdjustmentType='ChangeInCapacity',
    Cooldown=300
)
