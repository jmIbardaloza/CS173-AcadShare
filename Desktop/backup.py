from flask import Flask, render_template, redirect, url_for, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin@admin.com' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/add_mem')
def new_member():
   return render_template('new_member.html')

@app.route('/add_org')
def new_org():
   return render_template('new_org.html')

@app.route('/add_repo')
def new_repo():
   return render_template('new_repo.html')

@app.route('/add_folder')
def new_folder():
   return render_template('new_folder.html')

@app.route('/add_file')
def new_file():
   return render_template('new_file.html')

@app.route('/add_mem',methods = ['POST', 'GET'])
def add_mem():
   if request.method == 'POST':
      try:
         u_id = request.form['u_id']
         passw = request.form['pass']
         d_name = request.form['d_name']
         display_pic = request.form['d_pic']
         creation_date = request.form['creation_date']

         with sql.connect("database.db") as con:
            cur = con.cursor()

            # print("u_id=" + u_id)

            # cur.execute("INSERT INTO member VALUES ('1234', 'pass', 'dylan', NULL, '12/24/1999')")
            cur.execute("INSERT INTO member VALUES (?, ?, ?, NULL, ?);", (u_id, passw, d_name, creation_date))

            con.commit()
            msg = "Member successfully added"
      except Exception as err:
         con.rollback()
         msg = "Error in INSERT operation: %s" % str(err)

      finally:
         return render_template("result_add_rec.html",msg = msg)
         con.close()

@app.route('/add_org',methods = ['POST', 'GET'])
def add_org():
   if request.method == 'POST':
      try:
         u_id = request.form['u_id']
         org_code = request.form['org_code']
         passw = request.form['pass']
         d_name = request.form['d_name']
         display_pic = request.form['d_pic']
         creation_date = request.form['creation_date']

         with sql.connect("database.db") as con:
            cur = con.cursor()

            # print("u_id=" + u_id)

            # cur.execute("INSERT INTO member VALUES ('1234', 'pass', 'dylan', NULL, '12/24/1999')")
            cur.execute("INSERT INTO org VALUES (?, ?, ?, ?, NULL, ?);", (u_id, org_code, passw, d_name, creation_date))

            con.commit()
            msg = "Org successfully added"
      except Exception as err:
         con.rollback()
         msg = "Error in INSERT operation: %s" % str(err)

      finally:
         return render_template("result_add_rec.html",msg = msg)
         con.close()

@app.route('/add_repo',methods = ['POST', 'GET'])
def add_repo():
   if request.method == 'POST':
      try:
         repo_id = request.form['repo_id']
         repo_name = request.form['repo_name']
         creation_date = request.form['creation_date']

         with sql.connect("database.db") as con:
            cur = con.cursor()

            cur.execute("INSERT INTO repository VALUES (?, ?, ?);", (repo_id, repo_name, creation_date))

            con.commit()
            msg = "Repository successfully added"
      except Exception as err:
         con.rollback()
         msg = "Error in INSERT operation: %s" % str(err)

      finally:
         return render_template("result_add_rec.html",msg = msg)
         con.close()

@app.route('/add_folder',methods = ['POST', 'GET'])
def add_folder():
   if request.method == 'POST':
      try:
         folder_id = request.form['folder_id']
         folder_name = request.form['folder_name']
         creation_date = request.form['creation_date']

         with sql.connect("database.db") as con:
            cur = con.cursor()

            cur.execute("INSERT INTO folders VALUES (?, ?, ?);", (folder_id, folder_name, creation_date))

            con.commit()
            msg = "Folder successfully added"
      except Exception as err:
         con.rollback()
         msg = "Error in INSERT operation: %s" % str(err)

      finally:
         return render_template("result_add_rec.html",msg = msg)
         con.close()

@app.route('/list_all')
def list_all():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("SELECT * FROM member");
    mem_rows = cur.fetchall();

    cur.execute("SELECT * FROM org");
    org_rows = cur.fetchall();

    cur.execute("SELECT * FROM repository");
    repo_rows = cur.fetchall()

    cur.execute("SELECT * FROM folders");
    folder_rows = cur.fetchall()

    cur.execute("SELECT * FROM files");
    file_rows = cur.fetchall();

    return render_template("list_all.html", mem_rows = mem_rows, org_rows = org_rows, repo_rows = repo_rows,
    folder_rows = folder_rows, file_rows = file_rows)

if __name__ == '__main__':
   app.run(debug = True)
