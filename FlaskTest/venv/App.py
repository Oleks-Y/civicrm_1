from flask import  Flask, jsonify,request



app = Flask(__name__)



@app.route('/tiktokparse/tasks', methods = ['GET'])
def get_tasks():
    name = request.args.get('name')
    return jsonify({'name': name})



if __name__ == "__main__":
    app.run(debug=True)
