from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [
  {
    'id':1,
    'title':'Data Analist',
    'location': 'Sao Paulo, Brasil',
    'salary':'R$ 10000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location': 'Sao Paulo, Brasil',
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
    'salary':'$ 15000'
  }
]

@app.route("/")
def hello_world():
  return render_template("home.html",
                         jobs=JOBS,
                         company_name="Wanderson")
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)