from flask import Flask, render_template, request
import db
from flaskext.mysql import MySQL

app = Flask(__name__)

# application config
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'exam_report_task'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

# MySql
mysql = MySQL()
mysql.init_app(app)
# MySql Connection
conn = mysql.connect()
cursor = conn.cursor()


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/entermarks', methods=['GET', 'POST'])
def redirect_to_enter_marks():
    global cursor, conn
    if request.method == 'GET':
        return render_template('enter_marks.html')
    else:
        rollno = str(request.form['rollno'])
        name = str(request.form['name'])
        marks_physics = str(request.form['marks_in_physics'])
        marks_maths = str(request.form['marks_in_maths'])
        marks_chemistry = str(request.form['marks_in_chemistry'])
        total = str(request.form['total'])
        percentage = str(request.form['percentage'])
        print(total, percentage)
        db.insert_student_details(conn, cursor,
                                  [rollno, name, marks_physics, marks_maths, marks_chemistry, total, percentage])
        return render_template('enter_marks.html')


@app.route('/leaderboard', methods=['GET'])
def redirect_to_view_leaderboard():
    if request.method == 'GET':
        result = db.get_leaderboard(conn, cursor)
        print(result)
        return render_template('leaderboard.html', result=result)


if __name__ == '__main__':
    # app.run()
    app.run(host="0.0.0.0")
