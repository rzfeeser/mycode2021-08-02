#!/urs/bin/python3

import paramiko

host = "ssh.example.com"
port = 22
username = "demo"
password = "password"

command = "ls"

# create an ssh object
ssh = paramiko.SSHClient()

# sidesteps "do you want to add this fingerprint to your keyfile?" (first time ssh question)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# this connects using our creds
ssh.connect(host, port, username, password)

# issue the command "ls"
stdin, stdout, stderr = ssh.exec_command(command)

# capture the output
lines = stdout.readlines()

# display the output
print(lines)
