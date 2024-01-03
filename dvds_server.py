from flask import Flask, request, jsonify, redirect, abort

app = Flask(__name__)

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

@app.route('/')
def index():
        return "Good day to you, sir!"

# get all dvds
@app.route('/dvds')
def getAll():
        return jsonify(dvds)

# find by ID
@app.route('/dvds/<int:id>')
def findById(id):
        foundDvds = list(filter(lambda t:  t["ID"]== id, dvds))
        if len (foundDvds) == 0:
                return jsonify ({}), 204
        return jsonify (foundDvds[0])
        
# create dvd
# test curl: curl -X POST -H "content-type:application/json" -d "{\"Title\":\"test\", 
# \"Director\":\"some dude\", \"Year\":\"1999\", \"Price\":123}" http://127.0.0.1:5000/dvds

@app.route('/dvds', methods =['POST'])
def create():
    global nextID
    if not request.json:
        abort(400)

    dvd = {
        "id" : nextID,
        "Title" : request.json["Title"],
        "Director" : request.json["Director"],
        "Year" : request.json["Year"],
        "Price" : request.json ["Price"]     
        }
    
    dvds.append(dvd)
    nextID += 1
    return jsonify(dvd)

# update dvds
# test curl: curl -X PUT -d "{\"Title\":\"The Shining\", \"Price\":20}" -H "content-type:application/json" http://127.0.0.1:5000/dvds/1
@app.route('/dvds/<int:id>', methods =['PUT'])
def update(id):
        foundDvds = list(filter(lambda t:  t["ID"]== id, dvds))
        if len (foundDvds) == 0:
                return jsonify ({}), 404
        currentDvd = foundDvds[0]
        if 'Title' in request.json:
                currentDvd['Title'] = request.json['Title']
        if 'Director' in request.json:
                currentDvd['Director'] = request.json['Director']        
        if 'Year' in request.json:
                currentDvd['Year'] = request.json['Year']
        if 'Price' in request.json:
                currentDvd['Price'] = request.json['Price']
        return jsonify(currentDvd)                

# delete dvd
@app.route('/dvds/<int:id>', methods =['DELETE'])
def delete(id):
        foundDvds = list(filter(lambda t:  t["ID"]== id, dvds))
        if len (foundDvds) == 0:
                return jsonify ({}), 404
        dvds.remove(foundDvds[0])        
        return jsonify({"done":True})


if __name__ == "__main__":
            app.run(debug = True)




