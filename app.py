from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    a=[]
    for i in str(10):
        a.append(i)
    return a


#if __name__ == '__main__':
app.run()
