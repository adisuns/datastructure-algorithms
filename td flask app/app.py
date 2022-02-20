from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getprime',methods=['POST'])
def getprime():
    data = request.get_json()
    number = int(data['n'])
    prime_number = []
    for p in range(2,number+1):
        if generate_prime(p):
            prime_number.append(p)
    return json.dumps(prime_number)


def generate_prime(num):
    if num <=1:
        return False
    for i in range(2,num):
        if num % i ==0:
            return False
    return True

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')