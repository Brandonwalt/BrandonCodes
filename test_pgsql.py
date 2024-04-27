"""Test queries from PostgreSQL database.
Louis Bertrand <louis.bertrand@durhamcollege.ca>
Sat April 1, 2017

This runs on the Raspberry Pi; needs the psycopg2 PostgreSQL DB API module."""

import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.Connection("measurement.db") 

# Get a cursor
curs = conn.cursor()

print("20 most recent measurements")
curs.execute("""SELECT sensor.name as s, measurement.timestamp as t, 
    measurement.value as v, units.name as u
  FROM measurement, sensor, type, units
  WHERE measurement.sensor = sensor.id
    AND sensor.type = type.id
    AND type.units = units.id
  ORDER BY s DESC
  LIMIT 20;""")
for row in curs.fetchall():
    print("Name",row[0], "Timestamp", row[1], "value", row[2], "units", row[3])


# Use the SQL SUM and COUNT functions to get the total of the value column
# and the count of records, then divide sum by count to get average.
print("average temperature for the last 5 minutes (all ds18b20 sensors).")
# To get 5 minutes earlier, subtract 5 minutes from the datetime instance
current_time = datetime.utcnow()
five_minutes = timedelta(minutes=5)
earlier_time = current_time - five_minutes
print("  from", earlier_time.isoformat(' '))
curs.execute("""SELECT sum(measurement.value), count(measurement.value),
    sum(measurement.value) / count(measurement.value)
  FROM measurement, sensor, type
  WHERE 
    measurement.sensor = sensor.id
    AND sensor.type = type.id AND type.name = 'ds18b20'
    AND measurement.timestamp > %s;""", (earlier_time.isoformat(' '),))
row = curs.fetchone()
if row[1] > 0:
    print("  sum",row[0], "count", row[1], "mean", row[2])
else:
    print("  No recent records found. Is the data collection process running?")
