from io import TextIOWrapper
import csv

def import_jobs (file: TextIOWrapper, conn):
    print('importing jobs')

    cur = conn.cursor() # Open a cursor to perform database operations
    csvFile = csv.reader(file) # Read file as csv
    next(csvFile, None)  # Skip the headers

    for lines in csvFile:
        id = lines[0]
        employer_id = lines[1]
        hourly_rate = lines[2]
        start_time = lines[3]
        end_time = lines[4]
        days_to_work = lines[5]
        education_requirement = lines[6]
        sql = f"INSERT INTO jobs VALUES ({id},{employer_id},{hourly_rate}, '{start_time}', '{end_time}', '{days_to_work}', '{education_requirement}')"
        cur.execute(sql)
    
    conn.commit() # Commit changes to database
    print('jobs fully imported')
    cur.close() # Close open database cursor