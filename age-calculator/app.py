from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_age', methods=['POST'])
def calculate_age():
    dob = datetime.datetime.strptime(request.form['dob'], '%Y-%m-%d')
    today = datetime.datetime.today()
    age_year = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    
    return render_template('result.html', age_year=age_year)  # Specify the name of the variable

if __name__ == '__main__':
    app.run(debug=True)
