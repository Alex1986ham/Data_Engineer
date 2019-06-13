# https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972

from flask import Flask, render_template, request, json
from flask.ext.mysql import MySQL
app = Flask(__name__)

mysql= MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'aldudko2'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Dudko010914'
app.config['MYSQL_DATABASE_DB'] = 'Bucketlist'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()



@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods=['POST'])
def signUp():
    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # validate the received values
    if _name and _email and _password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fileds</span>'})






if __name__ == "__main__":
    app.run()
