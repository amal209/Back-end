from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chart1')
def chart1():
    df = pd.DataFrame({
        "Year": [2010,2015,2020,2025],
        "A": [1000000,1500000, 2500000, 3000000]
    })
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.Population_db
    collection = db.africanPopulation
    data = pd.DataFrame(list(collection.find()))
    #data.drop(['_id'], axis = 1)
    data1= pd.DataFrame(columns =['Year', 'Population','Fertility Rate','Urban Population'])
    data1=data[::-1]
    data1


    fig = px.line(data1[["Year", "Population"]], x="Year", y=["Year", "Population"], title='African Population')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Fruit in North America"
    description = """
    A academic study of the number of apples, oranges and bananas in the cities of
    San Francisco and Montreal would probably not come up with this chart.
    """
    return render_template('notdash2.html', graphJSON=graphJSON, header=header,description=description)

@app.route('/chart2')
def chart2():
    df = pd.DataFrame({
        "Vegetables": ["Lettuce", "Cauliflower", "Carrots", "Lettuce", "Cauliflower", "Carrots"],
        "Amount": [10, 15, 8, 5, 14, 25],
        "City": ["London", "London", "London", "Madrid", "Madrid", "Madrid"]
    })

    fig = px.bar(df, x="Vegetables", y="Amount", color="City", barmode="stack")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Vegetables in Europe"
    description = """
    The rumor that vegetarians are having a hard time in London and Madrid can probably not be
    explained by this chart.
    """
    return render_template('notdash2.html', graphJSON=graphJSON, header=header,description=description)


    