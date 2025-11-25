from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def home():
    #return 'hello home'
    return render_template('Mathkey.html')

@app.route('/api')
def api():
    return 'hello api'
    #return render_template('Mathkey.html')

@app.route('/Mathkey')
def Mathkey():
    return 'hello mathkey'
    #return render_template('Mathkey.html')

if __name__ == '__main__':
    app.run()
    #app.run(host = '127.0.0.1:5000',port = 80,debug = True) # Develop version
    # app.run(host = '0.0.0.0',port = 80,debug = False) # Release version

