"""
Description: 

This will be a small program that initializes our x-day/week cache table/database.
Creates any triggers, functions, etc. that will be used to copy incoming data into our cache.
"""

import psycopg2 as postgre

def main():
    """

    """

    conn = postgre.connect(dbname="chirpstack_as_events", user="postgres", password="dbpassword")
    curs = conn.cursor()

    curs.execute("select * from device_join;")

    for row in curs.fetchall():
        print(row)


if __name__ == "__main__":
    main()