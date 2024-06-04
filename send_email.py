import smtplib
import ssl
import mimetypes
from email.message import EmailMessage

# Dados do email
password = open("senha", "r").read() #O arquivo senha n foi pro github por motivos de segurança, mas é só entrar na sua conta google e pesquisar "Senhas de APP" e gerar a sua e coloca-la num arquivo "senha" na raiz do projeto
from_email = "anthonymnf30@gmail.com"
to_email = "anthonymnf30@gmail.com"
subject = "Automação Planilha"
body = """
Olá. Segue em anexo a automação da planilha para a empresa XYZ Automação.

Qualquer dúvida estou a disposição!
"""

# MOntado a estrutura do e-mail
message = EmailMessage()
message["From"] = from_email
message["To"] = to_email
message["Subject"] = subject

message.set_content(body)
safe = ssl.create_default_context()

# Adicionando o anexo
anexo = "data/bar_chart.xlsx"
mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split("/")
print(mimetypes.guess_type(anexo)[0].split("/"))

with open(anexo, "rb") as a:
  message.add_attachment(
    a.read(),
    maintype = mime_type,
    subtype = mime_subtype,
    filename = anexo
  )
  
# Enviando o e-mail
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=safe) as smtp:
  smtp.login(from_email, password)
  smtp.sendmail(
    from_email,
    to_email,
    message.as_string()
  )