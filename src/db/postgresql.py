import logging
import psycopg2


def get_description_of_nvidia_displays():
    try:
        conn = psycopg2.connect(database="postgres",
                                host="localhost",
                                user="postgres",
                                password="M0633",
                                port="5432")
        logging.info("PostgreSQL connection is opened")
        cursor = conn.cursor()
        cursor.execute("SELECT description FROM public.test_data WHERE class='Display' "
                       "AND manufacturer='NVIDIA'")
        device = ';'.join(cursor.fetchone())
        return device

    except (Exception, psycopg2.Error) as error:
        logging.error("Error while fetching data from PostgreSQL", error)

    finally:
        if conn:
            cursor.close()
            conn.close()
            logging.info("PostgreSQL connection is closed")
