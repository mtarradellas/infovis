from io import TextIOWrapper
import csv

def import_check_in_journal (file: TextIOWrapper, conn):
    print('importing check_in journal')
    print('0% done')

    cur = conn.cursor() # Open a cursor to perform database operations
    csvFile = csv.reader(file) # Read file as csv
    next(csvFile, None)  # Skip the headers

    total_lines = 2100635

    sql = "INSERT INTO check_in_journal VALUES "
    i = 1
    for lines in csvFile:
        participant_id = lines[0]
        log_time = lines[1]
        venue_id = lines[2]
        venue_type = lines[3]
        sql += f"('{log_time}',{participant_id},{venue_id},'{venue_type}'), "

        # Execute insert block
        if (i % 500000 == 0):
            print(f'{round(i*100/total_lines)}% done')
            cur.execute(sql[:-2])
            sql = "INSERT INTO check_in_journal VALUES "
        i += 1

    cur.execute(sql[:-2])
    print('100% done')
    conn.commit() # Commit changes to database
    print('check_in journal fully imported')
    cur.close() # Close open database cursor