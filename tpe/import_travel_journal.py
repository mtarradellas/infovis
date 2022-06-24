from io import TextIOWrapper
import csv

def import_travel_journal (file: TextIOWrapper, conn):
    print('importing travel journal')
    print('0% done')

    cur = conn.cursor() # Open a cursor to perform database operations
    csvFile = csv.reader(file) # Read file as csv
    next(csvFile, None)  # Skip the headers

    total_lines = 2099656

    sql = "INSERT INTO travel_journal VALUES "
    i = 1
    for lines in csvFile:
        participant_id = lines[0]
        travel_start_time = lines[1]
        travel_start_location_id = lines[2] if lines[2] != 'NA' else 'null'
        travel_end_time = lines[3]
        travel_end_location_id = lines[4] if lines[4] != 'NA' else 'null'
        purpose = lines[5]
        check_in_time = lines[6]
        check_out_time = lines[7]
        starting_balance = lines[8]
        ending_balance = lines[9]
        sql += f"({participant_id},'{travel_start_time}',{travel_start_location_id},'{travel_end_time}',{travel_end_location_id},'{purpose}','{check_in_time}','{check_out_time}',{starting_balance},{ending_balance}), "

        # Execute insert block
        if (i % 500000 == 0):
            print(f'{round(i*100/total_lines)}% done')
            cur.execute(sql[:-2])
            sql = "INSERT INTO travel_journal VALUES "
        i += 1

    cur.execute(sql[:-2])
    print('100% done')
    conn.commit() # Commit changes to database
    print('travel journal fully imported')
    cur.close() # Close open database cursor