# autoscaling-infrastructure
## This script has to continuously to read metrics from the AWS SQS and post them to AWS cloud watch for autoscaling.

### Instructions:
1. To run this script, please install the following packages using any package manager( preferably pip3) 
  - aws 
  - boto3
2. Please add your IAM credentials on aws-cli ( Follow the instructions in the link : https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
3. ***Note:*** 
  Your IAM role must have the following permissions -
  - AutoScalingFullAccess
  - AmazonS3FullAccess
  - CloudWatchFullAccess
  - AmazonSQSFullAccess
4. This script can be run on a t2.nano too! 
