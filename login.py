from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Set your SMTP server
app.config['MAIL_PORT'] = 587  # Set your SMTP port
app.config['MAIL_USE_TLS'] = True  # Use TLS (True/False)
app.config['MAIL_USERNAME'] = 'your_username'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@example.com'  # Set your default sender email

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get form data
            recipient_email = request.form['recipient_email']
            subject = request.form['subject']
            message = request.form['message']

            # Send email
            send_email(recipient_email, subject, message)

            flash('Email sent successfully!', 'success')
            return redirect(url_for('index'))

        except Exception as e:
            flash(f'Error sending email: {str(e)}', 'error')

    return render_template('index.html')

def send_email(recipient, subject, message):
    try:
        msg = Message(subject, recipients=[recipient])
        msg.body = message

        mail.send(msg)
    except Exception as e:
        raise Exception(f"Error sending email: {str(e)}")

if __name__ == '__main__':
    app.secret_key = 'supersecretkey'  # Change this to a more secure key
    app.run(debug=True)
