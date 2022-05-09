from flask import Flask, request, abort, json
import ssl

app = Flask(__name__)

@app.route('/test',methods = ['POST'])
def outgoing_webhook(): #Teams -> Flask Server로 Receive 받는 Fucntion
    if request.methods == 'POST':
        print(request.json)
        data = {
            "type":"message",
            "text":"Echo."
        }
        response = app.response_class(response = json.dumps(data), status=200, mimetype = 'application/json')

        return response_class
    else :
        abort(400)

if __name__ == '__main__':
    app.debug=True
    app.run(host="0.0.0.0",port='50')
