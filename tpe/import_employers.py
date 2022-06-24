from io import TextIOWrapper
import csv

def import_employers (file: TextIOWrapper, conn):
    print('importing employers')

    cur = conn.cursor() # Open a cursor to perform database operations
    csvFile = csv.reader(file) # Read file as csv
    next(csvFile, None)  # Skip the headers

    for lines in csvFile:
        id = lines[0]
        location = f"ST_GeometryFromText('{lines[1]}')"
        building_id = lines[2]
        sql = f"INSERT INTO employers VALUES ({id},{location},{building_id})"
        cur.execute(sql)
    
    conn.commit() # Commit changes to database
    print('employers fully imported')
    cur.close() # Close open database cursor