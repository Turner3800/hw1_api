from flask import Flask, request, jsonify

app = Flask(__name__)

numBooks = 0
fiction = []  
non_fiction = []  
all_books = []  

@app.route('/library/getFiction',methods = ['GET'])
def getFiction():
   return jsonify({"Fiction Books":fiction});

@app.route('/library/getNon-Fiction',methods = ['GET'])
def getNonFiction():
   return jsonify({"Non-Fiction Books":non_fiction});

@app.route('/library/getAll',methods = ['GET'])
def getAll():
   return jsonify({"All Books":all_books});

@app.route('/library/getNumber',methods = ['GET'])
def getNumber():
   return jsonify({"Number of Books":numBooks});

@app.route('/library/addBook',methods = ['POST'])
def addBook():
   global numBooks
   current_book = request.get_json()

   if(current_book["genre"] == "fiction"):
   		fiction.append(current_book)
   elif(current_book["genre"] == "non-fiction"):
   		non_fiction.append(current_book)

   numBooks += 1
   all_books.append(current_book)
   return jsonify({"Total Books":numBooks});

@app.route('/library/removeBook',methods = ['POST'])
def removeBook():
   global numBooks
   current_book = request.get_json()

   name = current_book["title"]

   for book in fiction:
   		if book["title"] == name:
   			fiction.remove(book)
   for book in non_fiction:
   		if book["title"] == name:
   			non_fiction.remove(book)
   for book in all_books:
   		if book["title"] == name:
   			all_books.remove(book)
   			numBooks -= 1

   return jsonify({"Total Books":numBooks});

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8202, debug = True)