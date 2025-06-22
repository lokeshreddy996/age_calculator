from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    age = None
    if request.method == 'POST':
        try:
            dob_str = request.form.get('dob')
            dob = datetime.strptime(dob_str, '%Y-%m-%d')
            today = datetime.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        except Exception as e:
            print("Error:", e)
            age = "Invalid Date"
    return render_template('index.html', age=age)

if __name__ == '__main__':
    app.run(debug=True)

