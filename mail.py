import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# 设置SMTP服务器地址和端口
smtp_server = 'smtp.live.com'
smtp_port = 587  # 或者 465，取决于您的邮件服务器
# 邮件发送者和接收者的信息
sender_email = ''
receiver_email = ''
password = ''
# 创建MIME邮件对象
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = 'demo'
# 邮件正文内容
body = '这是邮件内容，用Python发送，后续会把它改成可复用的形式。'
msg.attach(MIMEText(body, 'plain'))
# 发送邮件
try:
    # 连接到SMTP服务器
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # 启动TLS加密
    # 登录SMTP服务器
    server.login(sender_email, password)
    # 发送邮件
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print("邮件发送成功！")
except Exception as e:
    print(f"邮件发送失败: {e}")