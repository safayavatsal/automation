# Web Application Lifecycle Management on AWS

## Overview

This project provides a comprehensive solution for managing the lifecycle of a web application hosted on AWS EC2 instances. It automates the deployment, scaling, and monitoring of the application, while also handling notifications for administrators. Key AWS services used include S3, EC2, ALB, ASG, SNS, and Lambda.


## Project Structure

- **`create_s3_bucket.py`**: Creates an S3 bucket to store static files.
- **`launch_ec2_instance.py`**: Launches and configures an EC2 instance with a web server (e.g., Apache or Nginx).
- **`deploy_alb.py`**: Deploys an Application Load Balancer (ALB) and registers EC2 instances.
- **`create_asg.py`**: Configures an Auto Scaling Group (ASG) with scaling policies.
- **`setup_sns.py`**: Sets up SNS topics and subscribes email addresses for notifications.
- **`sns_lambda_integration.py`**: Integrates SNS with Lambda functions for alerting.
- **`deploy_infrastructure.py`**: A single script to deploy, update, or tear down the entire infrastructure.
- **`upload_content.py`**: Manages user-generated content by uploading it to S3.
- **`lambda_content_handler.py`**: Lambda function for handling content movement to S3.


## Setup Instructions

### Prerequisites

1. **AWS Account**: Ensure you have an AWS account.
2. **AWS CLI**: Install and configure AWS CLI with your credentials.
3. **Python**: Ensure Python is installed. You will need `boto3`, which you can install using `pip`.

   ```sh
   pip install boto3

### Deployment
**1. Create S3 Bucket:**
**Run the following command to create an S3 bucket:**
`python create_s3_bucket.py`

**2. Launch EC2 Instance:**
**Run the following command to launch an EC2 instance:**
`python launch_ec2_instance.py`

**3. Deploy ALB:**
**Run the following command to deploy an Application Load Balancer:**
`python deploy_alb.py`

**4. Configure ASG:**
**Run the following command to create an Auto Scaling Group:**
`python create_asg.py`

**5. Setup SNS:**
**Run the following command to set up SNS topics and subscriptions:**
`python setup_sns.py`

**6. Integrate SNS with Lambda:**
**Run the following command to integrate SNS with Lambda:**
`python sns_lambda_integration.py`

**7. Deploy Infrastructure:**
**Use the following script to deploy, update, or tear down infrastructure:**
`python deploy_infrastructure.py`

**8. Manage Content (Optional):**
**Use the following script to upload user-generated content to S3:**
`python upload_content.py`
**Deploy the Lambda function for content handling:**
`python lambda_content_handler.py`


### Usage
**Scaling and Load Balancing:** The Auto Scaling Group will automatically manage the scaling of EC2 instances based on defined policies.
**Notifications:** SNS topics will send notifications to administrators based on infrastructure health and scaling events.
**Dynamic Content:** User-generated content will be uploaded to S3, and Lambda functions will manage the transfer of content from EC2 to S3.


### Notes
Replace placeholder values in the scripts (e.g., AMI IDs, security groups, VPC IDs) with your actual values.
Ensure IAM roles and policies are correctly configured to allow the necessary permissions for each service.

