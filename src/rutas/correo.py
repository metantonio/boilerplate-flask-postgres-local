from ..main import request, jsonify, app
import requests, json
import smtplib, ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')
URL_BACKEND = os.environ.get('BASE_URL')

@app.route('/correo', methods=['GET'])
def enviarcorreo():
    smtp_address = 'smtp.gmail.com'
    smtp_port = 465
    #body = request.get_json()
     
   
    correo = request.json.post("correo")
    datab = {"JREmail":correo}
    r = requests.put(url = URL_BACKEND+"/usuarios/reset-password", json = datab) 
    #print("r: ", r) #devuelve 201
    pastebin_url = r.text #devuelve la clave nueva
    #print("The response is:%s"%pastebin_url) 
    #print(correo)
    email_address = EMAIL
    email_password = PASSWORD
    #print(email_address)
    email_receiver = correo

    # al crear un e-mail
    message = MIMEMultipart("alternative")
    # Asunto
    message["Subject"] = "Asunto del E-mail"
    # el que envía
    message["From"] = email_address
    # el correo de quién recibe
    message["To"] = email_receiver

    # version HTML
    texte = '''
    Buenos días 

    '''

    html = '''
    <html>
    <body>
    <h1>Estimado Usuario:</h1>
    <p>Se ha generado una nueva Clave Generada: '''+ pastebin_url+''' </p>
    <b>Saludos</b>
    <br>
    <a href="https://www.github.com/metantonio">Kaizen Capital</a>
    </body>
    </html>
    '''

    # crea elemento MIMEText 
    texte_mime = MIMEText(texte, 'plain')
    html_mime = MIMEText(html, 'html')

    # adjunta
    message.attach(texte_mime)
    message.attach(html_mime)

    # conecta  envía
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:  
        server.login(email_address, email_password)  
        server.sendmail(email_address, email_receiver, message.as_string())
 
    response_body = {
        "msg": "Mensaje Enviado "
    }

    return jsonify(response_body), 200

