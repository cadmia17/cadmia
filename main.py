from flask import Flask, render_template
from threading import Thread

app = Flask("paper generator")
@app.route("/")

def cadmia_main():
  return render_template("index.html")
     
def start_server():
	app.run(host="0.0.0.0", port=8080)

t = Thread(target=start_server)
t.start()