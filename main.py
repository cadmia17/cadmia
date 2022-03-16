from flask import Flask, render_template
from threading import Thread
import json

class Topic:
  test = "12.c"

  def __init__(self, name, difficulty):
    self.name = name
    self.difficulty = float(difficulty)

class TAuxiliary(Topic):
  pass

aux = TAuxiliary("aux", 1)

print(aux.difficulty)


inp = open("pdf/input.json")
inp2 = json.load(inp)
print(inp2)

inp.close()


app = Flask("paper generator")
@app.route("/")
def cadmia_main():
  return render_template("index.html")
     
def start_server():
	app.run(host="0.0.0.0", port=8080)

t = Thread(target=start_server)
t.start()