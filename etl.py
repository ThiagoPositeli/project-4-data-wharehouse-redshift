import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):

    """ 
    This function load the files from s3 buckets into state_tables in redshift dhw database
    """

    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):

    """ 
    This function call queries from sql_querys.py and insert from sql_queries to insert the data into dhw redshift tables
    """

    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
        
    """ 
    This reads the dwh.cfg and get the all parameters they need to make the connections in aws and redshift to insert data into the tables
    """

    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()