# method to add student details into the database
def insert_student_details(conn, cursor, request):
    sql_query = "insert into students values (%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql_query, tuple(request))
    conn.commit()


# method to fetch data from database ordered by percentage
def get_leaderboard(conn, cursor):
    sql_query = "select * from students order by percentage DESC"
    cursor.execute(sql_query)
    result = cursor.fetchall()
    return result
