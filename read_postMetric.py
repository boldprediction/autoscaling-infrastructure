################
# Code to read metrics from SQS and send them to cloud watch
################
import datetime
import time 
import boto3


auto_client = boto3.client('autoscaling')
sqs_client = boto3.client('sqs')
watch_client = client = boto3.client('cloudwatch')

sleep_time = 60

while True:
	response = sqs_client.get_queue_attributes(
	    QueueUrl='https://sqs.us-east-2.amazonaws.com/280175692519/bold_sqs',
	    AttributeNames=[
	        'ApproximateNumberOfMessages',
	    ]
	)
	msg_num = int(response['Attributes']['ApproximateNumberOfMessages'])

	response = auto_client.describe_auto_scaling_groups(
	    AutoScalingGroupNames=[
	        'ASG-6thOctober-Test',
	    ],
	    # NextToken='string',
	    MaxRecords=100
	)

	auto_instances = response['AutoScalingGroups'][0]['Instances']
	print("Auto instances",auto_instances)
	active_instance_num = 0 
	for instance in auto_instances:
		if instance['LifecycleState'] == 'InService':
			active_instance_num += 1
	
	print("active_instances",active_instance_num)

	print("Number of msgs",msg_num)

	print("msg_num = ", msg_num)
	print("active_instance_num = ", active_instance_num)
	backlog_per_instance = msg_num*1.0/active_instance_num if active_instance_num!= 0 else 10
	print("backlog_per_instance = ", backlog_per_instance)

	response = watch_client.put_metric_data(
	    Namespace='BoldPrediction',
	    MetricData=[
	        {
	            'MetricName': 'MyBacklogPerInstance',
	            'Dimensions': [
	                {
	                    'Name': 'AutoScaleGroup',
	                    'Value': 'ASG-6thOctober-Test'
	                },
	            ],
	            # 'Timestamp': datetime.datetime.now(),
	            'Value': backlog_per_instance,
	            'Unit': 'None',
	        },
	    ]
	)
	time.sleep(sleep_time)


