from flask import Flask, render_template
from database import engine ca
from sqlalchemy import text

app = Flask(__name__)

    # Define the load_tururi function outside any other function or route handler
def load_tururi():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Tur"))
        result_all = []
        rows = result.fetchall()
        for row in rows:
                result_all.append(row)
        return result_all

    # Define the route function properly, at the same indentation level as other functions
@app.route('/')
def hello_world():
        # You can call the load_tururi function here if needed
    tururi = load_tururi()
    return render_template('home.html', tururi=tururi)

if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True)
