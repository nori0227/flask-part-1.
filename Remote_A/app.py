from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'
  
@app.route('/page')
def page_new():
    return 'Hello world, this is my page!'
  
@app.route('/name')
def my_name():
    return 'Hello world, my name is Jannatul!'

  
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
