"""fluffy tempatures from PostgreSQL database.
Brandon Walters <Brandon.Walters@durhamcollege.ca>
Sat April 12, 2017"""

import psycopg2
from datetime import datetime, timedelta

#Change user and password to your credentials
conn = psycopg2.connect(dbname="greenhouse2", \
                       host="fluffy.durhamcollege.org", user="brandonwalters1", \
                       password="thole-pippin-reborn-guppy")

curs = conn.cursor()
current_time = datetime.utcnow()

five_seconds = timedelta(seconds=5)
all_time = current_time - five_seconds

one_minutes = timedelta(minutes=1)
brandon_time = current_time - one_minutes

two_minutes = timedelta(minutes=2)
average_time = current_time - two_minutes

print("  from", all_time.isoformat(' '))

print("all the measurements taken in the last 5 seconds")
curs.execute("""SELECT sensor.name as s, measurement.timestamp as t,
    measurement.value as v, units.name as u
    FROM measurement, sensor, type, units
    WHERE 
    measurement.sensor = sensor.id
    AND sensor.type = type.id
    AND type.units = units.id
    AND measurement.timestamp > %s
    ORDER BY s DESC;""", (all_time.isoformat(' '),))
row = curs.fetchone()
print("|","\t","Name  ","\t","|", "\t","Timestamp", "\t","|", "value","|", "units", "|",
      "\n","_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" )
for row in curs.fetchall():
    print( "|",row[0]," "*(18-len(row[0])), "|", row[1],"|", row[2]," "*(13-len(row[0])),"|", row[3],"|")

print("all the measurements from a specific thermometer sensor")
curs.execute("""SELECT sensor.name as s, measurement.timestamp as t,
    measurement.value as v, units.name as u
    FROM measurement, sensor, type, units
    WHERE 
    measurement.sensor = sensor.id AND sensor.name = 'Brandon sensor 1'
    AND sensor.type = type.id
    AND type.units = units.id 
    AND measurement.timestamp > %s
    ORDER BY s DESC;""", (brandon_time.isoformat(' '),))
row = curs.fetchone()
print("|","\t","Name  ","\t","|", "\t","Timestamp", "\t","|", "value","|", "units", "|",
      "\n","_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" )
for row in curs.fetchall():
    print( "|",row[0]," "*(18-len(row[0])), "|", row[1],"|", row[2]," "*(13-len(row[0])),"|", row[3],"|")


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

print("Was any switch been pressed in the last 5 seconds")
curs.execute("""SELECT measurement.timestamp as t, sensor.name as s,
    measurement.value as v
  FROM measurement, sensor, type
  WHERE measurement.sensor = sensor.id
    AND sensor.type = 1
    AND measurement.timestamp > %s;""", (all_time.isoformat(' '),))
row = curs.fetchone()
if row[2] > 0:
    print(" yes ")
else:
    print(" No ")
