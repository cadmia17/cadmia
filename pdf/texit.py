import json, shutil, requests
from urllib.parse import quote as encode
from pdf_templates import PDF
from fpdf import XPos, YPos


###
###
###this code is quarantined
###
###


import argparse
import logging

parser = argparse.ArgumentParser()
parser.add_argument(
  "-d", "--debug",
  help="Print lots of debugging statements",
  action="store_const", dest="loglevel", const=logging.DEBUG,
  default=logging.WARNING,
)
args = parser.parse_args()    
logging.basicConfig(level=args.loglevel)


###
###
###end quarantine zone
###
###



base = "https://chart.googleapis.com/chart?cht=tx&chl="

def image_link(formula):
  return base + encode(formula)


class PDF(PDF):
  def parse(self, dic):
    print(dic) #after converting json to dictionary
    
    for key in dic.keys():
      print(key)

      val = dic[key] #question, ans a, ans b, ans c, ans d

      val_list = val.split("$") #splits into text, formula, text, etc.

      for v in val_list: #iterates for every text and formula
        print(f"~ v = [{v}]")

        if v[0] == "%": #formula
          v = v[1:] #removes leading % indicating formula
          
          self.image(image_link(v), alt_text=v) #gets the link to the image
          #then appends it to the pdf
          
          print(f"x: {self.get_x()}, y: {self.get_y()}")
        
        else: #normal text
          #if the cell would >right side, multi_cell
          #else cell
          print(f"w=30, h={self.sth}, txt={v}, new_x={XPos.END}, new_y={YPos.LAST}")

          self.multi_cell(w=30, h=self.sth, txt=v, new_x=XPos.END, new_y=YPos.LAST) #
          