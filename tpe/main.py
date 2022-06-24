import psycopg2
from imports import *

# Connect to your postgres DB
conn = psycopg2.connect("dbname=test user=postgres password=postgres host=127.0.0.1")

with open('Data/Attributes/Participants.csv', mode='r') as file:
    import_participants(file, conn)

with open('Data/Journals/SocialNetwork.csv', mode='r') as file:
    import_social_networks(file, conn)

with open('Data/Journals/TravelJournal.csv', mode='r') as file:
    import_travel_journal(file, conn)

with open('Data/Journals/FinancialJournal.csv', mode='r') as file:
    import_financial_journal(file, conn)

with open('Data/Journals/CheckinJournal.csv', mode='r') as file:
    import_check_in_journal(file, conn)

with open('Data/Attributes/Buildings.csv', mode='r') as file:
    import_buildings(file, conn)

with open('Data/Attributes/Schools.csv', mode='r') as file:
    import_schools(file, conn)

with open('Data/Attributes/Restaurants.csv', mode='r') as file:
    import_restaurants(file, conn)

with open('Data/Attributes/Pubs.csv', mode='r') as file:
    import_pubs(file, conn)

with open('Data/Attributes/Employers.csv', mode='r') as file:
    import_employers(file, conn)

with open('Data/Attributes/Jobs.csv', mode='r') as file:
    import_jobs(file, conn)

with open('Data/Attributes/Apartments.csv', mode='r') as file:
    import_apartments(file, conn)

for i in range(1, 73):
    print(f'importing status logs {i}')
    with open(f'Data/ActivityLogs/ParticipantStatusLogs{i}.csv', mode='r') as file:
        import_participant_status_logs(file, conn)
print('status logs fully imported')



conn.close() # Close database connection
