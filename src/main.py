from flask import Flask, render_template,redirect, url_for, request, session
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import hashlib
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'januar2020'

client = MongoClient("mongodb+srv://admin:admin@cluster0.ikglt.mongodb.net/test?retryWrites=true&w=majority")
db = client.test


rasporedi_kolekcija = db['rasporedi']

@app.route('/')
@app.route('/raspored')
def index():
    
	
	nasi_rasporedi = rasporedi_kolekcija.find({})

	return render_template('index.html', rasporedi = nasi_rasporedi)



if __name__ == '__main__':
	app.run(debug=True)