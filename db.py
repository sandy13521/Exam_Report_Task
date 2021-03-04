# method to add student details into the database
def insert_student_details(conn, cursor, request):
    try:
        check_primary_key = "select Count(roll_no) from students where roll_no=%s"
        cursor.execute(check_primary_key,(request[0],)) 
        result = cursor.fetchone()
        if result[0] == 1:
            return False
        sql_query = "insert into students values (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql_query, tuple(request))
        conn.commit()
        return True
    except:
        print("Roll No is already present")
    

# method to fetch data from database ordered by percentage
def get_leaderboard(conn, cursor):
    sql_query = "select * from students order by percentage DESC"
    cursor.execute(sql_query)
    result = cursor.fetchall()
    return result
