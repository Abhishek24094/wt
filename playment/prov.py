import subprocess
command = str(raw_input("Please enter create ,ls or rm\n"))
if command == "create":
    service=str(raw_input("Please choose between hello_service,world_service,nginx or all \n"))
    if service == "nginx":
       subprocess.check_output('docker-compose up -d nginx_service ',shell=True)
    elif service == "hello_service":
       subprocess.check_output('docker-compose up -d hello_service ',shell=True)
    elif service == "world_service":
       subprocess.check_output('docker-compose up -d world_service ',shell=True)
    elif service == "all":
       subprocess.check_output('docker-compose up -d ',shell=True)
    else :
       print("Wrong Input")
elif command == "ls":
   out=subprocess.check_output("docker-compose ps",shell=True)
   print(out)
elif command == "rm":
    service=str(raw_input("Please choose between hello_service,world_service,nginx_service or all \n"))
    if service == "hello_service":
       subprocess.check_output('docker-compose stop  hello_service ',shell=True)
       subprocess.check_output('docker rm hello-container',shell=True)
    if service == "nginx_service":
       subprocess.check_output('docker-compose stop  nginx_service ',shell=True)
       subprocess.check_output('docker rm nginx',shell=True)
    elif service == "world_service":
       subprocess.check_output('docker-compose stop  world_service ',shell=True)
       subprocess.check_output('docker-compose rm  hello-container',shell=True)
    elif service == "all":
       subprocess.check_output('docker-compose down ',shell=True)
    else :
       print("Wrong Input")
else :
    print("Wrong Input")
