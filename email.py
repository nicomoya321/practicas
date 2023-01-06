import smtplib
import ssl
from email.message import EmailMessage

sujeto = " email de python"
body = " este es un e mail de prueba de python"
enviar_email = "niconob07@hotmail.com"
recibir_email = "niconob07@hotmail.com"
contraseña =input("ingrese contraseña:")

mensaje = EmailMessage()
mensaje["de"] = enviar_email
mensaje["para"] = recibir_email
mensaje["sujeto"] = sujeto
mensaje.set_content(body)

contexto = ssl.create_default_context()
print("enviando e mail")
with smtplib.SMTP_SSL("smtp.outlook.com",465 , context=contexto) as server:
    server.login(enviar_email ,contraseña)
    server.sendemail(enviar_email,recibir_email,mensaje.as_string)

print("completado")