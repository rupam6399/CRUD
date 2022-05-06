from flask import Flask , render_template, request,redirect

import mysql.connector


#connection to databases
conn=mysql.connector.connect(user='root',password='',host='localhost',database='python')

cursor=conn.cursor()
#app is object of Flask classx
app = Flask(__name__)
@app.route('/')

def register():
    return render_template('register.html')

@app.route('/getdata', methods=['post'])
def getdata():
    email = request.form['email']
    password = request.form['password']
    mobile = request.form['mobile']
    city = request.form['city']
    collage_id = request.form['collage_id']
    birth_date = request.form['birth_date']
    que="INSERT INTO users VALUES(NULL,%s,%s,%s,%s,%s,%s)"
    cursor.execute(que,(email,password,city,mobile,collage_id,birth_date,0,0))
    conn.commit()
    return redirect('/view')


@app.route('/view')
def view():
    query = "SELECT users.*, colleges.college_name FROM users INNER JOIN colleges ON users.college_id = colleges.id"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.commit()
    return render_template('view.html',result=result)


@app.route('/update', methods=['post'])
def update():
    update_id = request.form['update_id']
    query = "UPDATE users SET email=%s,password=%s,city=%s,mobile=%s,collage_id=%s,birth_date id=%s WHERE id="+update_id
    cursor.execute(query)
    result = cursor.fetchall()
    conn.commit()
    return redirect('/view')


#connection close
cursor.close()
conn.close()

#execute the file
app.run(debug=True)