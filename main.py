from flask import Flask, render_template
from threading import Thread

app = Flask("paper generator")

@app.route("/")
def cadmia_main():
  return render_template("index.html")

@app.route("/guide/")
def cadmia_guide():
  return render_template("guide.html")

@app.route("/settings/")
def cadmia_settings():
  return render_template("settings.html")
     
def start_server():
	app.run(host="0.0.0.0", port=8080)

t = Thread(target=start_server)
t.start()