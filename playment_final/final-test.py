import subprocess
import boto3
import time
import os,signal,shlex
def create():
	f=open('ec2.json','r')
	content=f.read()
	f.close()
	key=input("Please enter the key name for ssh and available in AWS:= ")
	content=content.replace('playment',key)
	servicename=input("Please enter service name:= ")
	hellover=input("Please enter hello version ex:- v2.0:= ")
	h='python-hello:'+hellover
	worldver=input("Please enter world version ex :- v2.0:= ")
	w='python-world:'+worldver
	client = boto3.client('cloudformation',region_name='us-east-1')
	response = client.create_stack(StackName=servicename,TemplateBody=content,Tags=[{'Key': 'task','Value': 'playment'}])
	time.sleep(60)
	response = client.describe_stacks(StackName=servicename)
	print("Instance has been provisioned , running ansible now\n")
	ip=response['Stacks'][0]['Outputs'][0]['OutputValue']
	print("Public ip of machine:-"+ip)
	f=open('/etc/ansible/hosts','w')
	f.write('[playment]')
	f.write('\n')
	f.write(ip)
	f.close()
	f=open('ansible.yml','r')
	content=f.read()
	f.close()
	content = content.replace('python-hello:v2.0',h)
	content = content.replace('python-world:v1.0',w)
	time.sleep(3)
	with open('ansible_final.yml','w') as f:
        	f.write(content)
	with open('error.err','w') as ferr, open('output.out','w') as fout:
		p=subprocess.Popen('ansible-playbook ansible_final.yml -u ec2-user &', stdout=fout, stderr=ferr,preexec_fn=os.setsid,shell=True)
	time.sleep(40)
	print('---------------------------------------------------------------------------------------')
	print('-------------------------------------Direct url----------------------------------------')
	print(ip+':3000/health\n')
	print(ip+':3000/version\n')
	print(ip+':4000/health\n')
	print(ip+':4000/version\n')
	print('------------------------------------Indirect Url---------------------------------------')
	print(ip+':80/world/version')
	print(ip+':80/hello/version')
	print(ip+':80/world/health')
	print(ip+':80/hello/health')
def list():
	client = boto3.client('cloudformation',region_name='us-east-1')
	response = client.describe_stacks()
	for x in (response['Stacks']):
		if x['StackStatus'] == 'CREATE_COMPLETE':
			for y in x['Tags']:
				if y['Value'] == 'playment':
					print(x['StackName'])
def remove():
	client = boto3.client('cloudformation',region_name='us-east-1')
	stackname=input("Please enter service name ")
	response = client.delete_stack(StackName=stackname)
	print(response)

def main():
	func=input("Please enter create , list or remove ")
	if func == 'create':
		create()
	elif func == 'list':
		list()
	elif func == 'remove':
		remove()
	else :
		print("Wrong Input")
main()
