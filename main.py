from flask import Flask, render_template, request, redirect, send_file, send_from_directory
from threading import Thread
from pdf.pdf import pdf
from time import sleep
import os

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
  print(f"1main time={time}")
  difficulty = int(request.args.get("difficulty")) / 100
  #t1 = request.args.get("t1")
  #t2 = request.args.get("t2")
  #t3 = request.args.get("t3")

  pdf(time=time, difficulty=difficulty, blocklist=[], output="pdf.pdf")
  
  print(os.getcwd())
  print([f for f in os.listdir(".") if os.path.isfile(f)])


  return redirect("/pdf.pdf")




@app.route("/pdf2/")
def cadmia_pdf2():
  print("@pdf2")
  print(os.getcwd())
  print([f for f in os.listdir('.') if os.path.isfile(f)])
  sleep(2) #PLEASE
  with open("output/pdf.pdf", "rb") as static_file:
    return send_file(static_file, filename="output.pdf")

@app.route("/pdf3/")
def cadmia_pdf3():
  sleep(2) #PLEASE
  return send_from_directory(app.config[""], "pdf.pdf", as_attachment=True)


def start_server():
	app.run(host="0.0.0.0", port=8080)

t = Thread(target=start_server)
t.start()