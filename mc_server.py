from flask import Flask, request, jsonify, redirect, url_for, jsonify

app = Flask(__name__)

DVDs = [
   {"ID": 1, "Title": "The Shining", "Director": "Stanley Kubrick", "Year": "1980", "Price": 20},
   {"ID": 2, "Title": "Solaris", "Director": "Andrei Tarkovsky", "Year": "1972", "Price": 25},
   {"ID": 3, "Title": "Casino", "Director": "Martin Scorsese", "Year": "1995", "Price": 20},
   {"ID": 4, "Title": "Malcolm X", "Director": "Spike Lee", "Year": "1992", "Price": 22},
   {"ID": 5, "Title": "North by Northwest", "Director": "Alfred Hitchcock", "Year": "1959", "Price": 18},
   {"ID": 6, "Title": "Under the Skin", "Director": "Jonathan Glazer", "Year": "2013", "Price": 22},
   {"ID": 7, "Title": "Fargo", "Director": "Joel Coen", "Year": "1996", "Price": 15},
   {"ID": 8, "Title": "Dune", "Director": "Denis Villeneuve", "Year": "2020", "Price": 25},
   {"ID": 9, "Title": "Blue Velvet", "Director": "David Lynch", "Year": "1986", "Price": 28}
   ]

@app.route('/')
def index():
        return "Good day to you, sir!"

@app.route('/dvds')
def getAll():
        return jsonify(DVDs)

@app.route('/dvds/<int:id>')
def findById(id):
        return "served by find by id with id" + str (id)

@app.route('/dvds', methods =['POST'])
def create():
        return "served by Create"

@app.route('/dvds', methods =['PUT'])
def update():
        return "served by Update with id"

@app.route('/dvds', methods =['DELETE'])
def delete():
        return "served by Delete with id"


if __name__ == "__main__":
            app.run(debug = True)




