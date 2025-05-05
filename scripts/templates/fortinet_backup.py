# FortiGate backup using SSH
import paramiko

host = "fortinet-firewall.local"
user = "admin"
password = "your_password"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=password)

stdin, stdout, stderr = client.exec_command("execute backup config flash")
print(stdout.read().decode())
client.close()
