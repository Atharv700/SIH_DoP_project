# this is demo code which is under development for Sustainability Tracking

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# useing (SQLite)
def init_db():
    conn = sqlite3.connect('sustainability.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS reports (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        energy_consumed INTEGER,
                        waste_generated INTEGER,
                        water_used INTEGER,
                        comments TEXT
                    )''')
    conn.commit()
    conn.close()


@app.route('/')
def index():
    return render_template('index.html')

# Data submission 
@app.route('/submit', methods=['POST'])
def submit_data():
    if request.method == 'POST':
        energy = request.form['energy']
        waste = request.form['waste']
        water = request.form['water']
        comments = request.form['comments']

        conn = sqlite3.connect('sustainability.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO reports (energy_consumed, waste_generated, water_used, comments) VALUES (?, ?, ?, ?)',
                       (energy, waste, water, comments))
        conn.commit()
        conn.close()

        return redirect(url_for('report'))

# Report route
@app.route('/report')
def report():
    conn = sqlite3.connect('sustainability.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reports')
    data = cursor.fetchall()
    conn.close()

    return render_template('report.html', data=data)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
