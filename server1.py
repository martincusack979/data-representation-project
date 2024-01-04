from flask import Flask, jsonify, request, abort
from dvdsDAO import dvdsDAO

app = Flask(__name__, static_url_path='', static_folder='.')

dvds = [
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

nextID = 10

# get all dvds
@app.route('/dvds')
def getAll():
    results = dvdsDAO.getAll()
    return jsonify(results)

# find by ID
@app.route('/dvds/<int:id>')
def findById(id):
    founddvd = dvdsDAO.findByID(id)

    return jsonify(founddvd)

# create dvd
# test curl: curl -X POST -H "content-type:application/json" -d "{\"Title\":\"test\", 
# \"Director\":\"some dude\", \"Year\":\"1999\", \"Price\":123}" http://127.0.0.1:5000/dvds
@app.route('/dvds', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    
    dvd = {
        "title": request.json['title'],
        "director": request.json['director'],
        "year": request.json['year'],
        "price": request.json['price'],
    }
    values =(dvd['title'],dvd['director'],dvd['year'], dvd['price'])
    newId = dvdsDAO.create(values)
    dvd['id'] = newId
    return jsonify(dvd)

# update dvds
# test curl: curl -X PUT -d "{\"Title\":\"The Shining\", \"Price\":20}" -H "content-type:application/json" http://127.0.0.1:5000/dvds/1
@app.route('/dvds/<int:id>', methods=['PUT'])
def update(id):
    founddvd = dvdsDAO.findByID(id)
    if not founddvd:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'price' in reqJson and type(reqJson['price']) is not int:
        abort(400)

    if 'title' in reqJson:
        founddvd['title'] = reqJson['title']
    if 'director' in reqJson:
        founddvd['director'] = reqJson['director']
    if 'year' in reqJson:
        founddvd['year'] = reqJson['year']
    if 'price' in reqJson:
        founddvd['price'] = reqJson['price']
    values = (founddvd['title'],founddvd['director'],founddvd['year'], founddvd['price'],founddvd['id'])
    dvdsDAO.update(values)
    return jsonify(founddvd)
        
# delete dvd
@app.route('/dvds/<int:id>' , methods=['DELETE'])
def delete(id):
    dvdsDAO.delete(id)
    return jsonify({"done":True})


if __name__ == '__main__' :
    app.run(debug= True)