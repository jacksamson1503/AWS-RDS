from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host="YOUR-RDS-ENDPOINT",
    user="admin",
    password="YOUR-PASSWORD",
    database="userdb"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    db.commit()

    return "Data Stored Successfully!"

app.run(host='0.0.0.0', port=5000)