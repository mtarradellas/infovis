from io import TextIOWrapper
import csv

def import_restaurants (file: TextIOWrapper, conn):
    print('importing restaurants')

    cur = conn.cursor() # Open a cursor to perform database operations
    csvFile = csv.reader(file) # Read file as csv
    next(csvFile, None)  # Skip the headers

    for lines in csvFile:
        id = lines[0]
        food_cost = lines[1]
        max_occupancy = lines[2]
        location = f"ST_GeometryFromText('{lines[3]}')"
        building_id = lines[4]
        sql = f"INSERT INTO restaurants VALUES ({id},{location},'{food_cost}', {max_occupancy},{building_id})"
        cur.execute(sql)
    
    conn.commit() # Commit changes to database
    print('restaurants fully imported')
    cur.close() # Close open database cursor