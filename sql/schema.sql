CREATE DATABASE IF NOT EXISTS taxi_dw;

USE taxi_dw;

CREATE TABLE IF NOT EXISTS taxi_trips (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pickup_datetime DATETIME,
    dropoff_datetime DATETIME,
    trip_distance FLOAT
);