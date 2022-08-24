from flask import Flask, render_template, request, redirect
from threading import Thread
from pdf.pdf import pdf

app = Flask("paper generator")

@app.route("/")
def cadmia_main():
  return render_template("index.html")

@app.route("/guide/")
def cadmia_guide():
  return render_template("guide.html")

@app.route("/settings/")
def cadmia_settings(): #code from stackoverflow
  if request.method == "POST":
    if request.form["submit-form"] == "form-submitted":
      print("posted and working")
      return pdf
    else:
      print("posted and broken")

  elif request.method == "GET":
    print("got")
    return render_template("settings.html")

@app.route("/pdf/")
def cadmia_pdf():
  time = request.args.get("time")
  difficulty = int(request.args.get("difficulty")) / 100
  #t1 = request.args.get("t1")
  #t2 = request.args.get("t2")
  #t3 = request.args.get("t3")

  pdf(time=time, difficulty=difficulty, blocklist=[], output="/pdf/pdf.pdf")

  return redirect("pdf.pdf")


def start_server():
	app.run(host="0.0.0.0", port=8080)

t = Thread(target=start_server)
t.start()