from flask import Flask, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = 'your secret key'

 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pythonlogin'

user = {}
mysql = MySQL(app)


@app.route('/', methods = ['GET', 'POST'])
def login():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=3306, debug=True)


    