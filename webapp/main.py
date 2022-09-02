from flask import Flask, render_template
import sqlite3
app = Flask(__name__)
def get_db_connection():
    conn = sqlite3.connect('asskicker.db')
    conn.row_factory = sqlite3.Row
    return conn
@app.route('/')
def index():
    
    conn = get_db_connection()
    logs = conn.execute('SELECT * FROM logs order by id DESC').fetchall()
#    history = conn.execute('SELECT * FROM browserhistory order by id DESC').fetchall()
    conn.close()
    return render_template('index.html', logs=logs, history=history)
  #   with app.open_resource('olupbiten.txt') as f:
 #       contents = f.readlines()

#        return render_template('index.html',logs=contents)
@app.route('/history')
def history():
    
    conn = get_db_connection()
#    logs = conn.execute('SELECT * FROM logs order by id DESC').fetchall()
    history = conn.execute('SELECT * FROM browserhistory order by id DESC').fetchall()
    conn.close()
    return render_template('history.html', history=history)
if __name__ == '__main__':
   app.run()