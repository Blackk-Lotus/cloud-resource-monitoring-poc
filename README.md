# Cloud Resource Monitoring POC
## Overview
This Proof of Concept (POC) project uses AWS to keep an eye on cloud resources, specifically EC2 instances, to make sure they don’t exceed preset thresholds. AWS Lambda runs the monitoring logic, which includes checking metrics such as instance health and usage. If anything goes over the defined limits—like CPU usage, memory, or instance count—a notification is automatically sent via Amazon SNS (Simple Notification Service).

The infrastructure is set up using AWS CloudFormation, which means it’s easy to deploy and scale across different accounts or regions. This setup is ideal for spotting potential issues before they become problems and can help prevent unexpected cloud costs or resource constraints by staying proactive with real-time alerts.

## Features
- **Monitor EC2 Instances**: Automatically checks the status of EC2 instances in your AWS account.
- **Alert Notifications**: Sends email notifications through Amazon SNS when a resource limit is exceeded.
- **Easy Deployment**: Utilize CloudFormation for seamless setup.

## Getting Started

### Prerequisites
- AWS Account
- AWS CLI configured on your machine
- Python 3.6 or higher
- Git installed

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/tandav333/cloud-resource-monitoring.git
   cd cloud-resource-monitoring
