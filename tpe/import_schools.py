from io import TextIOWrapper
import csv

def import_schools (file: TextIOWrapper, conn):
    print('importing schools')

    cur = conn.cursor() # Open a cursor to perform database operations
    csvFile = csv.reader(file) # Read file as csv
    next(csvFile, None)  # Skip the headers

    for lines in csvFile:
        id = lines[0]
        monthly_fees = lines[1]
        max_enrollment = lines[2]
        location = f"ST_GeometryFromText('{lines[3]}')"
        building_id = lines[4]
        sql = f"INSERT INTO schools VALUES ({id},{location},'{monthly_fees}', {max_enrollment},{building_id})"
        cur.execute(sql)
    
    conn.commit() # Commit changes to database
    print('schools fully imported')
    cur.close() # Close open database cursor