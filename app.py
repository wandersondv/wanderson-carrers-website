from flask import Flask, render_template

app = Flask(__name__)
JOBS = [
  {
    'id':1,
    'title':'Data Analist',
    'location': 'São Paulo, Brasil',
    'salary':'R$ 10000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location': 'São Paulo, Brasil',
    'salary':'R$ 15000'
  },
  {
    'id':3,
    'title':'Fronted Engineer',
    'location': 'Remote',
    'salary':'R$ 12000'
  },
  {
    'id':4,
    'title':'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary':'$ 12000'
  }
]

@app.route("/")
def hello_world():
  return render_template("home.html",  jobs=JOBS,  company_name="Wanderson")

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)