import mariadb
import dbcreds

def run_procedure(sql, args):
    try:
        results = None
        conn = mariadb.connect(**dbcreds.conn_params)
        cursor = conn.cursor()
        cursor.execute(sql, args)
        results = cursor.fetchall()
    except mariadb.ProgrammingError as error:
        print("There is an issue with the DB code: ", error)
    except mariadb.OperationalError as error:
        print("There is an issue connection to the DB: ", error)
    except Exception as error:
        print("There was an unknown error: ", error)
    finally:
        if(cursor != None):
            cursor.close()
        if(conn != None):
            conn.close()
        return results