import boto3

elb = boto3.client('elbv2')

# Create Load Balancer
response = elb.create_load_balancer(
    Name='my-load-balancer',
    Subnets=['subnet-0123456789abcdef0', 'subnet-abcdef0123456789'],
    SecurityGroups=['sg-0abcd1234efgh5678'],
    Scheme='internet-facing',
    Tags=[{'Key': 'Name', 'Value': 'my-load-balancer'}],
    Type='application',
    IpAddressType='ipv4'
)

load_balancer_arn = response['LoadBalancers'][0]['LoadBalancerArn']

# Create Target Group
response = elb.create_target_group(
    Name='my-target-group',
    Protocol='HTTP',
    Port=80,
    VpcId='vpc-0abcdef1234567890',
    HealthCheckProtocol='HTTP',
    HealthCheckPort='80',
    HealthCheckPath='/',
    HealthCheckIntervalSeconds=30,
    HealthCheckTimeoutSeconds=5,
    UnhealthyThresholdCount=2,
    HealthyThresholdCount=2
)

target_group_arn = response['TargetGroups'][0]['TargetGroupArn']

# Create Listener
elb.create_listener(
    LoadBalancerArn=load_balancer_arn,
    Protocol='HTTP',
    Port=80,
    DefaultActions=[{'Type': 'forward', 'TargetGroupArn': target_group_arn}]
)
