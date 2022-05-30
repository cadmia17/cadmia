from urllib.parse import quote as encode
from pdf_templates import PDF
from fpdf import XPos, YPos

def image_link(formula):
  base = "https://chart.googleapis.com/chart?cht=tx&chl="
  return base + encode(formula)

ignore = ["type", "answer", "partite"]

class PDF(PDF):
  def parse_multiple_choice(self, dic):
    for key in dic.keys(): #question, ans a, ans b, etc
      if key not in ignore:
        val = dic[key]
        val_list = val.split("$") #splits into text, formula, text, etc.

        for v in val_list: #iterates for every text and formula
          print(f"~ v_mc = [{v}]")
          print(f"w=30, h={self.sth}, txt=[{v}], new_x={XPos.END}, new_y={YPos.LAST}")
          if v[0] == "%": #formula
            v = v[1:] #removes leading % indicating formula

            self.image(image_link(v), alt_text=v) #gets the link to the image #then appends it to the pdf

            print(f"x: {self.get_x()}, y: {self.get_y()}")

          else: #normal text
            #if the cell would >right side, multi_cell
            #else cell
            #todo
  
            self.multi_cell(w=30, h=self.sth, txt=v, new_x=XPos.END, new_y=YPos.LAST)



  

  def parse_sa_whole(self, dic):
    for key in dic.keys():
      if key == "question":     
        val = dic[key] #see parse_mc for documentation
        val_list = val.split("$")
  
        for v in val_list:
          print(f"~ v_sa = [{v}]")
          if v[0] == "%":
            v = v[1:]
            self.image(image_link(v), alt_text=v)
          
            print(f"x: {self.get_x()}, y: {self.get_y()}")
          
          else: 
            print(f"w=30, h={self.sth}, txt={v}, new_x={XPos.END}, new_y={YPos.LAST}")
  
            self.multi_cell(w=30, h=self.sth, txt=v, new_x=XPos.END, new_y=YPos.LAST)



  
  
  def parse(self, dic):
    if dic["type"] == "multiple_choice":
      print("parser: mc")
      self.parse_multiple_choice(dic)

    else:
      if dic["partite"] == False:
        print("parser: sw")
        self.parse_sa_whole(dic)

      else:
        print("parser: sp")
        self.parse_sa_partite(dic)
    
    