from flask import Flask,request,jsonify
import json
import requests

app = Flask(__name__)


@app.route('/numbers',methods=['get'])
def numbers():
    ans = []
    urls = request.args.getlist('url')
    for i in urls:
        print(i)
        response = requests.get(str(i))
        print(response.status_code)
        # print(response.json())
        if(response.status_code == 200):
            print("hi")
            for j in response.json()['numbers']:
                ans.append(j)
    # ans = ans.sort()
    print(ans)
    d = {
        "numbers" : sorted(ans)
    }

    return d

@app.route('/')
def index():
    return "Hello, world!"

if __name__ == '__main__':
    app.run(debug=True, port=8008)