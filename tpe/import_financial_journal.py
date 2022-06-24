from io import TextIOWrapper
import csv

def import_financial_journal (file: TextIOWrapper, conn):
    print('importing financial journal')
    print('0% done')

    cur = conn.cursor() # Open a cursor to perform database operations
    csvFile = csv.reader(file) # Read file as csv
    next(csvFile, None)  # Skip the headers

    total_lines = 1856330

    sql = "INSERT INTO financial_journal VALUES "
    i = 1
    for lines in csvFile:
        participant_id = lines[0]
        log_time = lines[1]
        category = lines[2]
        amount = lines[3]
        sql += f"('{log_time}',{participant_id},'{category}',{amount}), "

        # Execute insert block
        if (i % 500000 == 0):
            print(f'{round(i*100/total_lines)}% done')
            cur.execute(sql[:-2])
            sql = "INSERT INTO financial_journal VALUES "
        i += 1

    cur.execute(sql[:-2])
    print('100% done')
    conn.commit() # Commit changes to database
    print('financial journal fully imported')
    cur.close() # Close open database cursor