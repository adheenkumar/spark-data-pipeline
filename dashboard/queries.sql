-- Trips per day
SELECT DATE(pickup_datetime) AS trip_date,
       COUNT(*) AS total_trips
FROM taxi_trips
GROUP BY trip_date
ORDER BY trip_date;

-- Average distance
SELECT AVG(trip_distance) AS avg_distance FROM taxi_trips;

-- Trips per hour
SELECT HOUR(pickup_datetime) AS hr,
       COUNT(*) AS trips
FROM taxi_trips
GROUP BY hr
ORDER BY hr;