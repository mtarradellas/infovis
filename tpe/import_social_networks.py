from io import TextIOWrapper
import csv

def import_social_networks (file: TextIOWrapper, conn):
    print('importing social networks')
    print('0% done')

    cur = conn.cursor() # Open a cursor to perform database operations
    csvFile = csv.reader(file) # Read file as csv
    next(csvFile, None)  # Skip the headers

    total_lines = 7482488

    # TODO update "social_network" to plural "social_networks"
    sql = "INSERT INTO social_network VALUES "
    i = 1
    for lines in csvFile:
        log_time = lines[0]
        participant_id_from = lines[1]
        participant_id_to = lines[2]
        sql += f"('{log_time}',{participant_id_from},{participant_id_to}), "

        # Execute insert block
        if (i % 500000 == 0):
            print(f'{round(i*100/total_lines)}% done')
            cur.execute(sql[:-2])
            sql = "INSERT INTO social_network VALUES "
        i += 1

    cur.execute(sql[:-2])
    print('100% done')
    conn.commit() # Commit changes to database
    print('social networks fully imported')
    cur.close() # Close open database cursor