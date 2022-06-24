from io import TextIOWrapper
import csv

def import_buildings (file: TextIOWrapper, conn):
    print('importing buildings')

    cur = conn.cursor() # Open a cursor to perform database operations
    csvFile = csv.reader(file) # Read file as csv
    next(csvFile, None)  # Skip the headers

    for lines in csvFile:
        id = lines[0]
        location = f"ST_GeometryFromText('{lines[1]}')"
        building_type = lines[2]
        max_occupancy = lines[3] if lines[3] != '' else 'null'
        units = f"'{lines[4]}'" if lines[4] != '' else 'null'
        sql = f"INSERT INTO buildings VALUES ({id},{location},'{building_type}', {max_occupancy},{units})"
        cur.execute(sql)

    conn.commit() # Commit changes to database
    print('buildings fully imported')
    cur.close() # Close open database cursor