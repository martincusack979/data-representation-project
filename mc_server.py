from flask import Flask, request, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
        return "blasht off!!"

@app.route('/dvds')
def getAll():
        return "served by Get All()"

@app.route('/dvds/<int:id>')
def findById(id):
        return "served by find by id with id" + str (id)


if __name__ == "__main__":
            app.run(debug = True)




