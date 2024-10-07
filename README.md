# Cloud Resource Monitoring POC
## Overview
This project is a Proof of Concept (POC) for monitoring cloud resources using AWS Lambda and CloudFormation. The system checks the status of EC2 instances and sends alerts via Amazon SNS when resource limits are exceeded.

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
   git clone https://github.com/yourusername/cloud-resource-monitoring.git
   cd cloud-resource-monitoring
