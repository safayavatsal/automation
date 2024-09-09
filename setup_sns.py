import boto3

sns = boto3.client('sns')

# Create SNS Topics
response = sns.create_topic(Name='HealthAlerts')
health_topic_arn = response['TopicArn']

response = sns.create_topic(Name='ScalingAlerts')
scaling_topic_arn = response['TopicArn']

# Subscribe Email to SNS Topics
sns.subscribe(TopicArn=health_topic_arn, Protocol='email', Endpoint='your-email@example.com')
sns.subscribe(TopicArn=scaling_topic_arn, Protocol='email', Endpoint='your-email@example.com')
