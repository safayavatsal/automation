import boto3

lambda_client = boto3.client('lambda')
sns_client = boto3.client('sns')

# Create Lambda Function (example)
response = lambda_client.create_function(
    FunctionName='NotifyHealthFunction',
    Runtime='python3.8',
    Role='arn:aws:iam::123456789012:role/service-role/my-role',
    Handler='lambda_function.lambda_handler',
    Code={'ZipFile': open('lambda_function.zip', 'rb').read()},
    Timeout=60,
    MemorySize=128
)

# Create SNS Subscription for Lambda
sns_client.subscribe(
    TopicArn='arn:aws:sns:region:account-id:HealthAlerts',
    Protocol='lambda',
    Endpoint='arn:aws:lambda:region:account-id:function:NotifyHealthFunction'
)
