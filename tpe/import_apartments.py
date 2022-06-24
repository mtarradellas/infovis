from io import TextIOWrapper
import csv

def import_apartments (file: TextIOWrapper, conn):
    print('importing apartments')

    cur = conn.cursor() # Open a cursor to perform database operations
    csvFile = csv.reader(file) # Read file as csv
    next(csvFile, None)  # Skip the headers

    for lines in csvFile:
        id = lines[0]
        rental_cost = lines[1]
        max_occupancy = lines[2]
        rooms = lines[3]
        location = f"ST_GeometryFromText('{lines[4]}')"
        building_id = lines[5]
        sql = f"INSERT INTO apartments VALUES ({id}, {location}, {rental_cost}, {max_occupancy}, {rooms}, {building_id})"
        cur.execute(sql)
    
    conn.commit() # Commit changes to database
    print('apartments fully imported')
    cur.close() # Close open database cursor