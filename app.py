import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from pymongo import MongoClient

db_pass = os.environ.get('DB_PASS')

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'songbook'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://Lingvistik:'+str(db_pass)+'@prviklaster-v3qci.mongodb.net/songbook?retryWrites=true&w=majority')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

mongo = PyMongo(app)

@app.route('/')
def route():
    return redirect(url_for('get_chords'))

@app.route('/get_chords')
def get_chords():
    return render_template('chordbook.html', chords=mongo.db.chords.find())

@app.route('/add_chords')
def add_chords():
    return render_template('addchords.html', genre=mongo.db.genre.find())

@app.route('/chords_diagram')
def chords_diagram():
    return render_template('chordsdiagram.html')

@app.route('/insert_chords', methods=['POST'])
def insert_chords():
    chords = mongo.db.chords
    chords.insert_one(request.form.to_dict())
    return redirect(url_for('get_chords')) 