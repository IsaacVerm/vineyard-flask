DROP TABLE IF EXISTS cleaned_weather_station;
DROP TABLE IF EXISTS output_model;

CREATE TABLE cleaned_weather_station
(
    id INTEGER PRIMARY KEY,
    moment TEXT,
    temperature INTEGER,
    rainfall INTEGER
);

CREATE TABLE output_model
(
    id INTEGER PRIMARY KEY,
    moment TEXT,
    prediction_boolean INTEGER,
    prediction_percentage INTEGER
);

CREATE TABLE spray
(
    id INTEGER PRIMARY KEY,
    moment TEXT,
    pesticide TEXT
);