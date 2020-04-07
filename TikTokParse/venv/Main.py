from flask import  Flask, jsonify,request
from Parser import getInfo
app = Flask(__name__)
@app.route('/tiktokparse/tasks', methods = ['GET'])
def getReq():
    name = request.args.get('name')
    return jsonify(getInfo(name))

if __name__ == "__main__":
    app.run(debug=True)