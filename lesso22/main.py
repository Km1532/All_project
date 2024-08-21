 import pymysql
from config import host, user, password , db_name

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("all its ride...")
    #print("#" * 20)



    try:
        # with connection.cursor() as cursor:
        #    create_table_query = " CREARE TABLE 'users'(id int AUTO_INCREMENT,"
        #                         " name varchar(32),"
        #                         " password varchar(32),"
        #                         " email varchar(32), PRIMARY KEY (id));"
        #cursor.execute(create_table_query)
        #print("Table, created is ok")
        cursor = connection.cursor()

    with connection_cursor() as cursor:
        print("The password must contain at least 6 to 8 digits and up to 3 letters")
        update_query = "UPDATE 'users' SET pasword = "xxxxXXX" WHERE id = 'Oleg' "
        cursor.execute(update_query)
        connection.connect()

    with connection.cursor() as cursor:
        delete_query = "DELETE FROM 'user' WHERE id = 5"
        cursor.execute(delete_query)
        connection.commit()

    with connection.cursor() as  cursor:
         inspect_query = "INSERT INTO 'users' (name. password, email) VAULES ('Oleg', '92014575' 'oleg.gmail.com')"
         cursor.execute(inspect_query)
         connection.commit()

    with connection.cursor() as  cursor:
         inspect_query = "INSERT INTO 'users' (name, password, email) VAULES ('Anna', '48972365' 'Ana.gmail.com')"
         cursor.execute(inspect_query)
         connection.commit()

    with connection.cursor() as  cursor:
         inspect_query = "INSERT INTO 'users' (name, password, email) VAULES ('Victor', '5047924' 'Victor.gmail.com')"
         cursor.execute(inspect_query)
         connection.commit()


    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM 'users'"
        cursor.execute(select_all_rows)
        cursor.execute("SELECT * FROM 'users'")
        rows = cursor.ferchall()
        for row in rows:
            print(row)
        print("#" * 20 )

    #delete.table.all
    with connection.cursor() as cursor:
        drop_table_query = "DROP TABLE 'users'"
        cursor.execute(drop_table_query)

    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)
