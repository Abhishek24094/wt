import subprocess
import json
cmd = """curl -s 'https://api.ipify.org?format=json'"""
output = subprocess.check_output(cmd,shell=True)
output = json.loads(output)
ip = output['ip']
with open('default.conf','r') as f:
	content = f.read()

content = content.replace('world-container',ip)
with open('default.conf','w') as f:
	f.write(content)
