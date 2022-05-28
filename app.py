from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px
import pymongo
from pymongo import MongoClient
import plotly.graph_objects as go

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
    collection = db.population
    data = pd.DataFrame(list(collection.find()))

    data1= pd.DataFrame(columns =['Year', 'African Population','Asian Population','European Population','South American Population','North American Population','Oceanian Population'])
    data1=data[::-1]
    data1


    #fig = px.line(data1[['Year', 'African Population','Asian Population','European Population','South American Population','North American Population','Oceanian Population']], x="Year", y=['Year', 'African Population','Asian Population','European Population','South American Population','North American Population','Oceanian Population'], title='African Population')
    #fig = px.line(data1[['Year', 'African Population']], x='Year', y=['African Population'], title='Population')
    #fig.add_scatter(x=data1['Year'], y=data1['Asian Population'])
    data1['African Population']=data1['African Population'].astype(float)
    data1['African Population']=data1['Asian Population'].astype(float)
    data1['African Population']=data1['European Population'].astype(float)
    
    fig = go.Figure()


    fig.add_trace(go.Bar(
     x = data1['Year'],
     y = data1['Asian Population'],
    name = "Asian Population",
    ))

    fig.add_trace(go.Bar(
     x = data1['Year'],
     y = data1['African Population'],
     name = "African Population",
    ))




    fig.update_layout(title_text="Multi-category axis")



    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="teeeeeeeeeeeeest"
    description = """
    description
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
    description
    """
    return render_template('notdash2.html', graphJSON=graphJSON, header=header,description=description)


    