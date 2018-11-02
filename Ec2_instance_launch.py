import boto3




def Create_instance(ec2):
    #ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(ImageId='ami-0ac019f4fcb7cb7e6', MinCount=1, MaxCount=1, InstanceType='t2.micro')
    print(instance[0].id)


def  List_of_instances(ec2):

#    ec2 = boto3.resource('ec2')
    for instance in ec2.instances.all():
     print (instance.id, instance.state)

instance_list=boto3.Session(aws_access_key_id= Access_key,aws_secret_access_key=Secret_key)

my_ec2 = boto3.resource('ec2')
Create_instance(my_ec2)
List_of_instances(my_ec2)
