import boto3
import json
import os

ec2_client = boto3.client('ec2')
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    instances = ec2_client.describe_instances()
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_state = instance['State']['Name']

            if instance_state == 'running':
                uptime = get_uptime(instance)
                if uptime > 72:  # 72 hours limit for POC
                    send_alert(instance_id, uptime)

    return {"statusCode": 200, "body": "Resource monitoring completed."}

def get_uptime(instance):
    # Placeholder for uptime calculation
    return 100  # For example purposes

def send_alert(instance_id, uptime):
    sns_client.publish(
        TopicArn=os.getenv('SNS_TOPIC_ARN'),
        Message=f"Instance {instance_id} has been running for {uptime} hours.",
        Subject=f"EC2 Monitoring Alert: {instance_id}"
    )