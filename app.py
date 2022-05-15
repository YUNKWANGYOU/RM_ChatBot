from flask import Flask, request, abort, json
import ssl
app = Flask(__name__)

### request Teams Message
@app.route('/test',methods=['POST'])
def webhook():
    if request.method == 'POST' :
        print(request.json)
        data = {
            "type":"message",
            "text":"Hello, World!"
        }
        response = app.response_class(
            response = json.dumps(data),
            status = 200,
            mimetype = 'application/json'
        )

        return response
    else:
        abort(400)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port="5000")
