from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'webDev123'
app.config['MYSQL_DB'] = 'bucketlist'

mysql = MySQL(app)

@app.route('/')
def main():
    return render_template("index.html")


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods=['POST'])
def signUp():
    print(request.method)
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    cursor = mysql.connection.cursor()
    query = "INSERT INTO bucketlist.tb1_user VALUES (5,'cb','cc','cbbb')"
    cursor.execute(query)
    mysql.connection.commit()
    cursor.close()
    return "DONE"



app.run()

