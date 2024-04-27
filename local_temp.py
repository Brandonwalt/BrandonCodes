"""Local tempatures from SQLite3 database.
Brandon Walters <Brandon.Walters@durhamcollege.ca>
Sat April 12, 2017"""

import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.Connection("measurement.db") 
curs = conn.cursor()
current_time = datetime.utcnow()

five_seconds = timedelta(seconds=5)
all_time = current_time - five_seconds

one_minutes = timedelta(minutes=1)
brandon_time = current_time - one_minutes

two_minutes = timedelta(minutes=2)
average_time = current_time - two_minutes

print("all the measurements taken in the last 5 seconds")
curs.execute("""SELECT sensor.name as s, measurement.timestamp as t, 
    measurement.value as v, units.name as u
    FROM measurement, sensor, type
  WHERE 
    measurement.sensor = sensor.id
    AND sensor.type = type.id
    AND type.units = units.id 
    AND measurement.timestamp > %s
  ORDER BY s DESC;""", (all_time.isoformat(' '),))
row = curs.fetchone()
for row in curs.fetchall():
    print("Name",row[0], "Timestamp", row[1], "value", row[2], "units", row[3])
    
print("all the measurements from a specific thermometer sensor")
curs.execute("""SELECT sensor.name as s, measurement.timestamp as t, 
    measurement.value as v, units.name as u
    FROM measurement, sensor, type
    WHERE 
    measurement.sensor = sensor.id AND sensor.name = 'Brandon sensor 1'
    AND sensor.type = type.id
    AND type.units = units.id 
    AND measurement.timestamp > %s
    ORDER BY s DESC;""", (brandon_time.isoformat(' '),))
row = curs.fetchone()
for row in curs.fetchall():
    print("Name",row[0], "Timestamp", row[1], "value", row[2], "units", row[3])


print("Calculate the average temperature from the last two minutes")
curs.execute("""SELECT sum(measurement.value), count(measurement.value),
    sum(measurement.value) / count(measurement.value)
  FROM measurement, sensor, type
  WHERE 
    measurement.sensor = sensor.id
    AND sensor.type = type.id AND type.name = 'ds18b20'
    AND measurement.timestamp > %s;""", (average_time.isoformat(' '),))
row = curs.fetchone()
if row[1] > 0:
    print("  sum",row[0], "count", row[1], "mean", row[2])
else:
    print("  No recent records found. Is the data collection process running?")

print("the last time switch 1 was pressed")
curs.execute("""SELECT measurement.timestamp as t, sensor.name as s,
    measurement.value as v
  FROM measurement, sensor, type, units
  WHERE measurement.sensor = sensor.id AND sensor.name = 'Brandon SW1'
    AND sensor.type = type.id;""")
for row in curs.fetchall():
    print("timestamp",row[0], "sensor", row[1], "value", row[2])
