from urllib.parse import quote as encode
from pdf_templates import PDF
from fpdf import XPos, YPos


def image_link(formula):
  base = "https://chart.googleapis.com/chart?cht=tx&chl="
  return base + encode(formula)


class PDF(PDF):
  def parse_multiple_choice(self, dic):
    for key in dic.keys():
      #print(key)
      val = dic[key] #question, ans a, ans b, etc
      val_list = val.split("$") #splits into text, formula, text, etc.

      for v in val_list: #iterates for every text and formula
        print(f"~ v = [{v}]")
        if v[0] == "%": #formula
          v = v[1:] #removes leading % indicating formula
          
          self.image(image_link(v), alt_text=v) #gets the link to the image #then appends it to the pdf
          
          print(f"x: {self.get_x()}, y: {self.get_y()}")
        
        else: #normal text
          #if the cell would >right side, multi_cell
          #else cell
          #todo
          print(f"w=30, h={self.sth}, txt={v}, new_x={XPos.END}, new_y={YPos.LAST}")

          self.multi_cell(w=30, h=self.sth, txt=v, new_x=XPos.END, new_y=YPos.LAST) #
    
  def parse(self, dic):
    print("parser: sus")

    if dic["type"] == "multiple_choice":
      self.parse_multiple_choice(dic)

    else:
      if dic["partite"] == False:
        self.parse_sa_whole(dic)

      else:
        self.parse_sa_partite(dic)
    
    