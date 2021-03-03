def insert_student_details(conn,cursor,request):
    sql_query = "insert into students values (%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql_query,tuple(request))
    conn.commit()

def get_leaderboard(conn,cursor):
    sql_query = "select * from students order by percentage DESC"
    cursor.execute(sql_query)
    result = cursor.fetchall()
    return result