from io import TextIOWrapper
import csv

def import_participants (file: TextIOWrapper, conn):
    print('importing participants')
    cur = conn.cursor() # Open a cursor to perform database operations
    csvFile = csv.reader(file) # Read file as csv
    next(csvFile, None)  # Skip the headers

    for lines in csvFile:
        id = lines[0]
        household_size = lines[1]
        have_kids = lines[2]
        age = lines[3]
        education_level = lines[4]
        interest_group = lines[5]
        joviality = lines[6]
        sql = f"INSERT INTO participants VALUES ({id},{household_size},{have_kids},{age},'{education_level}','{interest_group}',{joviality})"
        cur.execute(sql)

    conn.commit() # Commit changes to database
    print('participants fully imported')
    cur.close() # Close open database