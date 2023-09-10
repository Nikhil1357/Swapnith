from flask import Flask,request
app = Flask(__name__)
@app.get('/myapi')
def myapi():
    print("Namaste i am get method")
    return {}

@app.post('/content')
def content():
    print(request.data)
    return {}

if __name__ == '__main__':
    app.run(port='4000')
