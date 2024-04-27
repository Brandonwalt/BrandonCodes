import sqlite3

conn = sqlite3.Connection("Music track survey.db") 
curs = conn.cursor()
sql = """SELECT Artist.Name, Song.Title FROM Artist, Track, Song
    WHERE Track.artist = Artist.ID AND Track.song = Song.ID
    AND Song.Title = 'Harlem Nocturne';"""

sql2 = """SELECT Artist.Name, Artist.Name FROM Artist
    WHERE name LIKE 'Al%';"""

sql3 = """SELECT Count(song .title) from song ; """

sql4 = """SELECT Artist.Name, Song.Title FROM Artist, Track, Song
    WHERE Track.song = Song.ID AND Song.Title
    = Artist.ID AND artist.name = 'Quincy Jones';"""

curs.execute(sql)
for row in curs.fetchall():
    print("{} recorded {}".format(row[0],row[1]))

curs.execute(sql2)
for row in curs.fetchall():
    print("{}".format(row[0],row[1]))

curs.execute(sql3)
for row in curs.fetchall():
    print("there are {} songs in the database".format(row[0]))

curs.execute(sql4)
for row in curs.fetchall():
    print("Quincy Jones recorded {}".format(row[0]))
