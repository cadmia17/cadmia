import json, shutil, requests
from urllib.parse import quote as encode
from pdf_templates import PDF

base = "https://chart.googleapis.com/chart?cht=tx&chl="

def get_formula(formula, output="img.png"):
  en_formula = encode(formula)

  response = requests.get(base+en_formula, stream=True)
  with open(output, "wb") as out_file:
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
        print(f"~ v! {v}")
        if not v.startswith("%"): #normal text
          self.multi_cell(w=0, h=0, txt=v, ln=3)
          #print(f"added {v} to a multi-cell")

        else: #formula
          full_path = f"pdf/_{key_short}_{image_counter}.png"
          v = v[1:]
          get_formula("v", full_path)
          self.image(full_path)

          image_counter += 1
          

      pass

get_formula("amogus + sus + ratio", output="pdf/sus.png")