from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'palomarochamochi138@gmail.com'
app.config['MAIL_PASSWORD'] = 'qfds qplq bexz myrz'
mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    email = request.form['email']
    doubt = request.form['doubt']

  
    msg = Message('Nova Dúvida de Contato', sender='palomarochamochi138@gmail.com', recipients=['palomarochamochi138@gmail.com'])
    msg.body = f'Dúvida: {doubt}\n\nResposta será enviada para: {email}'
    mail.send(msg)

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
