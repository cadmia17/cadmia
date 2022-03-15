import json, shutil, requests
from urllib.parse import quote as encode
from pdf_templates import PDF

base = "https://chart.googleapis.com/chart?cht=tx&chl="

def get_formula(formula, output="img"):
  en_formula = encode(formula)

  response = requests.get(base+en_formula, stream=True)
  with open(f"pdf/_{output}.png", "wb") as out_file:
    shutil.copyfileobj(response.raw, out_file)
  del response
  

class PDF(PDF):
  def parse(self, dic):
    print(dic)
    for key in dic.keys():
      image_counter = 1 #yes this starts at 1
      print(key)
      key_short = key[0] + key[-1] #image id

      val = dic[key]

      val_list = val.split("$")

      for v in val_list:
        if not v.startswith("%"): #normal text
          self.multi_cell(w=0, h=0, txt=v, ln=3)
          print(f"added {v} to a multi-cell")

        else: #formula
          self.image(f"pdf/_{key_short}_")
          

      pass

q = open("pdf/q1.json")
qj = json.load(q)

pdf = PDF()
pdf.parse(qj)


get_formula("amogus + sus + ratio")