from flask import Flask, jsonify, redirect, url_for, render_template
from sqlalchemy import create_engine, func
from flask_sqlalchemy import SQLAlchemy
import datetime


database_path = "my.db"
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
#db = create_engine(f"sqlite:///../Netapp_api/my.db")
db = SQLAlchemy(app)
 
class unifiedmanager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cluster_name = db.Column(db.TEXT(255))
    aggr_name = db.Column(db.TEXT(255))
    total_size = db.Column(db.TEXT(255))
    used_size = db.Column(db.TEXT(255))
    percent = db.Column(db.TEXT(255))
    date = db.Column(db.TEXT(255))


@app.route('/ploty2')
def index():
    return render_template('tsploty.html')

@app.route('/api/data')
def data():
    results = db.session.query().with_entities(unifiedmanager.cluster_name,unifiedmanager.aggr_name,\
        unifiedmanager.total_size,unifiedmanager.used_size,unifiedmanager.percent,unifiedmanager.date)

    # context = {
    #     'results' : results
    # }
    aggrArray = []

    for cluster_name,aggr_name,total_size,used_size,percent,date in results:
        aggrObj = {}
        aggrObj['Cluster_Name'] = cluster_name
        aggrObj['Aggr_Name'] = aggr_name
        aggrObj['Total_Size'] = total_size
        aggrObj['Used_Size'] = used_size
        aggrObj['Percentage_Used'] = percent
        aggrObj['Date'] = date

        aggrArray.append(aggrObj)

    # return render_template('table.html', **context)
    return {'test':aggrArray}

@app.route('/')
def todayhigher65():
    dt = datetime.datetime.now()
    #dt_string = dt.strftime("%d-%m-%Y")
    dt_string = '10-01-2021'
    results = db.session.query().with_entities(unifiedmanager.cluster_name,unifiedmanager.aggr_name,\
        unifiedmanager.total_size,unifiedmanager.used_size,unifiedmanager.percent,unifiedmanager.date)\
            .filter(unifiedmanager.date==dt_string).filter(unifiedmanager.percent>='65').all()

    context = {
        'results' : results
    }

    # aggrArray = []

    # for cluster_name,aggr_name,total_size,used_size,percent,date in results:
    #     aggrObj = {}
    #     aggrObj['Cluster_Name'] = cluster_name
    #     aggrObj['Aggr_Name'] = aggr_name
    #     aggrObj['Total_Size'] = total_size
    #     aggrObj['Used_Size'] = used_size
    #     aggrObj['Percentage_Used'] = percent
    #     aggrObj['Date'] = date

    #     aggrArray.append(aggrObj)

    return render_template('index.html', **context)

@app.route('/ploty')
def todayhigher65_2():
    dt = datetime.datetime.now()
    #dt_string = dt.strftime("%d-%m-%Y")
    dt_string = '10-01-2021'
    results = db.session.query().with_entities(unifiedmanager.cluster_name,unifiedmanager.aggr_name,\
        unifiedmanager.total_size,unifiedmanager.used_size,unifiedmanager.percent,unifiedmanager.date)\
            .filter(unifiedmanager.date==dt_string).filter(unifiedmanager.percent>='65').all()


    aggrArray = []
     

    for cluster_name,aggr_name,total_size,used_size,percent,date in results:
        aggrObj = {}
        aggrObj['Cluster_Name'] = cluster_name
        aggrObj['Aggr_Name'] = aggr_name
        aggrObj['Total_Size'] = total_size
        aggrObj['Used_Size'] = used_size
        aggrObj['Percentage_Used'] = percent
        aggrObj['Date'] = date

        aggrArray.append(aggrObj)

    return {'test':aggrArray}

@app.route('/data')
def data1():
    results = db.session.query().with_entities(unifiedmanager.cluster_name,unifiedmanager.aggr_name,\
        unifiedmanager.total_size,unifiedmanager.used_size,unifiedmanager.percent,unifiedmanager.date)

    context = {
        'results' : results
    }
    # aggrArray = []

    # for cluster_name,aggr_name,total_size,used_size,percent,date in results:
    #     aggrObj = {}
    #     aggrObj['Cluster_Name'] = cluster_name
    #     aggrObj['Aggr_Name'] = aggr_name
    #     aggrObj['Total_Size'] = total_size
    #     aggrObj['Used_Size'] = used_size
    #     aggrObj['Percentage_Used'] = percent
    #     aggrObj['Date'] = date

    #     aggrArray.append(aggrObj)

    return render_template('table.html', **context)
    # return {'test':aggrArray}


if __name__ == "__main__":
    app.run(debug=True)