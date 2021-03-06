from flask import Flask
from flask import request

path_to_db = '/db/database.txt'

app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello, Guest! Feel free to register'

@app.route('/register')
def register():
    name = request.args.get('name')
    if not name:
        return 'User is not specified'

    with open(path_to_db, 'a') as data:
        data.write(name + '\n')
    return 'User %s is registered!'%name

if __name__ == "__main__":
    app.run(host='0.0.0.0')