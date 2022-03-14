import json, shutil
from urllib.parse import quote as encode
from pdf_templates import PDF

base = "https://chart.googleapis.com/chart?cht=tx&chl="

def get_formula(formula, output="pdf/_texit.png"):
  en_formula = encode(formula)
  

class PDF(PDF):
  def parse(self, dic):
    for key in dic.keys():
      print(key)
      key_short = key[0] + key[-1]

      pass



get_formula("amogus + sus + ratio")