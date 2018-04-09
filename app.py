import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("'sqlite:///hawaii.sqlite'")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of all precipitation"""
    results = session.query(Measurement.date, Measurement.prcp)\
        .filter(Measurement.date >= (today - dt.timedelta(days=365))).all()
    # Create a dictionary from the row data and append to a list of all_precipatations
    all_precipitations = []
    for station in results:
        precp_dict = {}
        precp_dict["Date"] = measurement.date
        precp_dict["precipitation"] = measurement.prcp
        all_precipitations.append(precp_dict)
    return jsonify(all_precipitations)


@app.route("/api/v1.0/stations")
def station():
    """Return a list of all stations"""
    # Query all stations
    results = session.query(station).all()

    # Create a dictionary from the row data and append to a list of all_stations
    all_stations = []
    for station in results:
        station_dict = {}
        station_dict["ID"] = station.station
        station_dict["name"] = station.name
        all_stations.append(station_dict)
    return jsonify(all_stations)



@app.route("/api/v1.0/tobs")
def tobs():
       """Return a list of all temperature"""
    results= session.query(Measurement.date, Measurement.tobs)\
        .filter(Measurement.date >= (today - dt.timedelta(days=365))).all()
    # Create a dictionary from the row data and append to a list of all_tobs
    all_tobs = []
    for station in results:
        tobs_dict = {}
        tobs_dict["Date"] = measurement.date
        tobs_dict["tobs"] = measurement.tobs
        all_tobs.append(precp_dict)
    return jsonify(all_tobs)




if __name__ == "__main__":
    app.run(debug=True)

