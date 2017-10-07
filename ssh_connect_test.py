import paramiko
import threading

hostname = ["123.206.129.82"]
login = {"ubuntu":"hudingyang123"}
paramiko.util.log_to_file('syslogin.log')
new_dict = {}
for x,k in zip(hostname, login.items()):
    new_dict[x] = k
#print(new_dict)
ssh_list = []

def ssh_connect(hostnamed, username, password):
    print(hostnamed,username,password)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostnamed, username=username, password=password, allow_agent=False, look_for_keys=False)
    ssh_list.append(ssh)
    return ssh

def ssh_command(command):
    for ssh in ssh_list:
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout.read())

def main():
    command = "ls -l"
    #print(new_dict)
    for host in new_dict:
        print(host,new_dict[host])
        threads = threading.Thread(target=ssh_connect, args=(str(host), str(new_dict[host][0]), str(new_dict[host][1])),name=host)
        print(threads.name)
        threads.start()
        threads.join()
    ssh_command(command)

if __name__ == "__main__":
    main()

