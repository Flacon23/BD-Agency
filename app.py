from flask import Flask, render_template
from database import engine
from sqlalchemy import text
app=Flask(__name__)
def load_tur():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM Tur"))
    result_all=[]
    rows = result.fetchall()  
    for row in rows:
      result_all.append(row)
    return result_all

def load_ghid():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM Ghid"))
    result_all=[]
    rows = result.fetchall()  
    for row in rows:
      result_all.append(row)
    return result_all

def load_destinatie():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM Destinatie"))
    result_all=[]
    rows = result.fetchall()  
    for row in rows:
      result_all.append(row)
    return result_all

def load_plate():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM Plata"))
    result_all=[]
    rows = result.fetchall()  
    for row in rows:
      result_all.append(row)
    return result_all

def load_rezervare():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM Rezervare"))
    result_all=[]
    rows = result.fetchall()  
    for row in rows:
      result_all.append(row)
    return result_all

def load_rezervare():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM Rezervare"))
    result_all=[]
    rows = result.fetchall()  
    for row in rows:
      result_all.append(row)
    return result_all

def load_turisti():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM Turisti"))
    result_all=[]
    rows = result.fetchall()  
    for row in rows:
      result_all.append(row)
    return result_all

def load_plecare():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM Plecare"))
    result_all=[]
    rows = result.fetchall()  
    for row in rows:
      result_all.append(row)
    return result_all

@app.route('/')
def login():
  return render_template('login.html')

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/tur')
def tur():
  tur=load_tur()
  return render_template('tur.html',tur=tur)

@app.route('/turisti')
def turisti():
  turisti=load_turisti()
  return render_template('turisti.html',turisti=turisti)

@app.route('/ghid')
def ghid():
  ghid=load_ghid()
  return render_template('ghid.html',ghid=ghid)

@app.route('/plate')
def plate():
  plate=load_plate()
  return render_template('plate.html',plate=plate)

@app.route('/destinatie')
def destinatie():
  destinatie=load_destinatie()
  return render_template('destinatie.html',destinatie=destinatie)

@app.route('/rezervare')
def rezervare():
  rezervare=load_rezervare()
  return render_template('rezervare.html',rezervare=rezervare)

@app.route('/plecare')
def plecare():
  plecare=load_plecare()
  return render_template('plecare.html',plecare=plecare)



if __name__=='__main__':
  app.run(host='0.0.0.0',debug=True)