from application import app
from flask import render_template
import pandas as pd
import json
import plotly
import plotly.express as px
from flask import Flask, render_template
import pandas as pd
import json

import pymongo
from pymongo import MongoClient
import plotly.graph_objects as go



@app.route('/')
def index():
    return render_template('index.html')

#Population
@app.route('/population')
def population():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.Population_db
    collection = db.population
    data = pd.DataFrame(list(collection.find()))
    data1= pd.DataFrame(columns =['Year', 'African Population','Asian Population','European Population','South American Population','North American Population','Oceanian Population'])
    data1=data[::-1]
    #data1


    # Graph 1
    fig1 = px.line(data1[['Year', 'African Population']], x='Year', y='African Population', title='African Population')
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 2
    fig2 = px.line(data1[['Year', 'Asian Population']], x='Year', y='Asian Population', title='Asian Population')
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 3
    fig3 = px.line(data1[['Year', 'European Population']], x='Year', y='European Population', title='European Population')
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 4
    fig4 = px.line(data1[['Year', 'South American Population']], x='Year', y='South American Population', title='South American Population')
    graph4JSON = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 5
    fig5 = px.line(data1[['Year', 'North American Population']], x='Year', y='North American Population', title='North American Population')
    graph5JSON = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 6
    fig6 = px.line(data1[['Year', 'Oceanian Population']], x='Year', y='Oceanian Population', title='Oceanian Population')
    graph6JSON = json.dumps(fig6, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('population.html', graph1JSON=graph1JSON,  graph2JSON=graph2JSON, graph3JSON=graph3JSON,graph4JSON=graph4JSON,graph5JSON=graph5JSON,graph6JSON=graph6JSON)


#Fertility Rate
@app.route('/fertility')
def fertility_rate():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.Population_db
    collection = db.fertility_rate
    data = pd.DataFrame(list(collection.find()))

    data1= pd.DataFrame(columns =['Year', 'African FR','Asian FR','European FR','South American FR','North American FR','Oceanian FR'])
    data1=data[::-1]
    #data1


    # Graph 1
    fig1 = px.line(data1[['Year', 'African FR']], x='Year', y='African FR', title='African Fertility Rate')
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 2
    fig2 = px.line(data1[['Year', 'Asian FR']], x='Year', y='Asian FR', title='Asian Fertility Rate')
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 3
    fig3 = px.line(data1[['Year', 'European FR']], x='Year', y='European FR', title='European Fertility Rate')
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 4
    fig4 = px.line(data1[['Year', 'South American FR']], x='Year', y='South American FR', title='South American Fertility Rate')
    graph4JSON = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 5
    fig5 = px.line(data1[['Year', 'North American FR']], x='Year', y='North American FR', title='North American Fertility Rate')
    graph5JSON = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 6
    fig6 = px.line(data1[['Year', 'Oceanian FR']], x='Year', y='Oceanian FR', title='Oceanian Fertility Rate')
    graph6JSON = json.dumps(fig6, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template('fertilityRate.html', graph1JSON=graph1JSON,  graph2JSON=graph2JSON, graph3JSON=graph3JSON,graph4JSON=graph4JSON,graph5JSON=graph5JSON,graph6JSON=graph6JSON)


#Urban Population
@app.route('/urbanPopulation')
def urbanPopulation():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.Population_db
    collection = db.urban_population
    data = pd.DataFrame(list(collection.find()))

    data1= pd.DataFrame(columns =['Year', 'African U.Population','Asian U.Population','European U.Population','South American U.Population','North American U.Population','Oceanian U.Population'])
    data1=data[::-1]
    #data1


    # Graph 1
    fig1 = px.line(data1[['Year', 'African U.Population']], x='Year', y='African U.Population', title='African Urban Population')
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 2
    fig2 = px.line(data1[['Year', 'Asian U.Population']], x='Year', y='Asian U.Population', title='Asian Urban Population')
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 3
    fig3 = px.line(data1[['Year', 'European U.Population']], x='Year', y='European U.Population', title='European Urban Population')
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 4
    fig4 = px.line(data1[['Year', 'South American U.Population']], x='Year', y='South American U.Population', title='South American Urban Population')
    graph4JSON = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 5
    fig5 = px.line(data1[['Year', 'North American U.Population']], x='Year', y='North American U.Population', title='North American Urban Population')
    graph5JSON = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 6
    fig6 = px.line(data1[['Year', 'Oceanian U.Population']], x='Year', y='Oceanian U.Population', title='Oceanian Urban Population')
    graph6JSON = json.dumps(fig6, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template('urbanPopulation.html', graph1JSON=graph1JSON,  graph2JSON=graph2JSON, graph3JSON=graph3JSON,graph4JSON=graph4JSON,graph5JSON=graph5JSON,graph6JSON=graph6JSON)


#Rural Population
@app.route('/ruralPopulation')
def ruralPopulation():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.Population_db
    collection = db.rural_population
    data = pd.DataFrame(list(collection.find()))

    data1= pd.DataFrame(columns =['Year', 'African R.Population','Asian R.Population','European R.Population','South American R.Population','North American R.Population','Oceanian R.Population'])
    data1=data[::-1]
    #data1


    # Graph 1
    fig1 = px.line(data1[['Year', 'African R.Population']], x='Year', y='African R.Population', title='African Rural Population')
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 2
    fig2 = px.line(data1[['Year', 'Asian R.Population']], x='Year', y='Asian R.Population', title='Asian Rural Population')
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 3
    fig3 = px.line(data1[['Year', 'European R.Population']], x='Year', y='European R.Population', title='European Rural Population')
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 4
    fig4 = px.line(data1[['Year', 'South American R.Population']], x='Year', y='South American R.Population', title='South American Rural Population')
    graph4JSON = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 5
    fig5 = px.line(data1[['Year', 'North American R.Population']], x='Year', y='North American R.Population', title='North American Rural Population')
    graph5JSON = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 6
    fig6 = px.line(data1[['Year', 'Oceanian R.Population']], x='Year', y='Oceanian R.Population', title='Oceanian Rural Population')
    graph6JSON = json.dumps(fig6, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template('population.html', graph1JSON=graph1JSON,  graph2JSON=graph2JSON, graph3JSON=graph3JSON,graph4JSON=graph4JSON,graph5JSON=graph5JSON,graph6JSON=graph6JSON)