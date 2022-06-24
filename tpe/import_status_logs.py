from io import TextIOWrapper
import csv

def import_participant_status_logs (file: TextIOWrapper, conn):
    print('0% done')

    cur = conn.cursor() # Open a cursor to perform database operations
    csvFile = csv.reader(file) # Read file as csv
    next(csvFile, None)  # Skip the headers

    total_lines = 1600000

    sql = "INSERT INTO participant_status_logs VALUES "
    i = 1
    for lines in csvFile:
        timestamp = lines[0]
        location = f"ST_GeometryFromText('{lines[1]}')"
        participant_id = lines[2]
        current_mode = lines[3]
        hunger = lines[4]
        sleep = f"'{lines[5]}'" if lines[5] != 'NA' else 'null'
        apartment_id = lines[6] if lines[6] != 'NA' else 'null'
        available_balance = lines[7] if lines[7] != 'NA' else 'null'
        job_id = lines[8] if lines[8] != 'NA' else 'null'
        financial_status = f"'{lines[9]}'" if lines[9] != 'NA' else 'null'
        food_budget = lines[10] if lines[10] != 'NA' else 'null'
        extra_budget = lines[11] if lines[11] != 'NA' else 'null'
        sql += f"({participant_id}, '{timestamp}', {location}, '{current_mode}', '{hunger}', {sleep}, {available_balance}, {financial_status}, {food_budget}, {extra_budget}, {apartment_id}, {job_id}), "

        # Execute insert block
        if (i % 500000 == 0):
            print(f'{round(i*100/total_lines)}% done')
            cur.execute(sql[:-2])
            sql = "INSERT INTO participant_status_logs VALUES "
        i += 1

    cur.execute(sql[:-2])
    print('100% done')
    conn.commit() # Commit changes to database
    print('partial participant status logs imported')
    cur.close() # Close open database cursor