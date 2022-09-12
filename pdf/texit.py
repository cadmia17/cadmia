from urllib.parse import quote as encode
from pdf.pdf_templates import PDF
from fpdf import XPos, YPos
import shutil, requests
from PIL import Image



def image_link(formula):
  base = "https://chart.googleapis.com/chart?cht=tx&chl="
  return base + encode(formula)

def get_formula(formula, output="img.png"):
  response = requests.get(image_link(formula), stream=True)
  
  with open(output, "wb") as out_file:
    shutil.copyfileobj(response.raw, out_file)
  del response



ignore = ["type", "answer", "partite"]


class PDF(PDF):
  def parse_parser(self, val, indent):
    RESIZE_COEFF = 11 / 32

    val_list = val.split("$") #splits into text, formula, text, etcc
    
    for v in val_list: #iterates for every text and formula
      image_counter = 0

      if len(v) > 0:
        if v[0] == "%": #formula
          #print(f"\n\n@ value = [{v}], formula")
          v = v[1:] #removes leading % indicating formula
          
          x_formula = self.get_x()
          y_formula = self.get_y()
          #print(f"x: {self.get_x()}, y: {self.get_y()}")
  
          full_path = f"pdf/_image.png"
          get_formula(v, full_path) #creates the png
  
          img = Image.open(full_path)
          img_w, img_h = img.size
          #print(f"img_w: {img_w}, img_h: {img_h}")
          
          self.image(img, alt_text=v)
          #print(f"x: {self.get_x()}, y: {self.get_y()}") #
  
          image_counter += 1
  
          fixed_img_w = (img_w * RESIZE_COEFF) #magic number, sorry
          fixed_img_h = (img_h * RESIZE_COEFF)
  
          new_x = x_formula + fixed_img_w
          #print(f"x before img ({x_formula}) + fixed img's width ({fixed_img_w}) = new x ({new_x})")
          self.set_xy(new_x, y_formula)
          
          #print(f"x: {self.get_x()}, y: {self.get_y()}")
  
          #self.image(image_link(v), alt_text=v) #gets the link to the image #then appends it to the pdf
          #new_x=XPos.RIGHT, new_y=YPos.TOP
          #which means, add the width of the image and subtract the height
          
  
        
        else: #normal text
          #print(f"\n\n@ value = [{v}], text")
          #if the cell would >right side, multi_cell
          #else cell
          #todo
  
          #try:
            #self.set_x(x_formula)
            #print(f"@ set x to {x_formula}")
            #self.set_y(y_formula)
            #print(f"@ set y to {y_formula}")
            
          #except:
            #pass
  
          try:
            self.multi_cell(w=0, h=self.sth, txt=v, new_x=(XPos.END), new_y=(YPos.LAST))
          except:
            #print("@ returning to lowest indentation level")
            self.set_x(indent)
  
            new_y = y_formula + fixed_img_h
            self.set_y(new_y)
            
            self.multi_cell(w=0, h=self.sth, txt=v, new_x=(XPos.END), new_y=(YPos.LAST))




  
  def parse_multiple_choice_2(self, dic, num=1):
    mc_answers = ["answer_a", "answer_b", "answer_c", "answer_d"]
    
    start = self.get_x()

    self.cell(w=25, h=self.sth, txt=f"**{num}.**", new_x=XPos.END, new_y=YPos.LAST, markdown=True) #creates 1) etc.

    indent = self.get_x()
    #print(f"@ starting x-pos: {indent}")

    #question
    
    val = dic["question"]

    self.parse_parser(val, indent)

    self.ln(10)

    
    #print("\n& beginning printing mc answers")

    for answer in mc_answers:
      #print(f"\n& {answer}")
      a = answer[-1]
  
      self.set_x(start + 12)
  
      self.cell(w=25, h=self.sth, txt=f"**({a.upper()})**", new_x=XPos.END, new_y=YPos.LAST, markdown=True) #creates (A)) etc.

      self.set_x(self.get_x() + 6)

      val = dic[answer]
      #print(f"{answer}: {val}")

      self.parse_parser(val, indent)
      
      self.ln(10)

    self.set_x(start)
    self.ln(15)
    


  
  
  def parse_multiple_choice(self, dic):
    for key in dic.keys(): #question, ans a, ans b, etc
      if key not in ignore:
        val = dic[key]
        val_list = val.split("$") #splits into text, formula, text, etc.

        for v in val_list: #iterates for every text and formula
          #print(f"~ v_mc = [{v}]")
          #print(f"w=30, h={self.sth}, txt=[{v}], new_x={XPos.END}, new_y={YPos.LAST}")
          if v[0] == "%": #formula
            v = v[1:] #removes leading % indicating formula

            self.image(image_link(v), alt_text=v) #gets the link to the image #then appends it to the pdf

            #print(f"x: {self.get_x()}, y: {self.get_y()}")

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



  
  
  def parse(self, dic, num):
    if dic["type"] == "multiple_choice":
      #print(f"parser: mc #{num}")
      self.parse_multiple_choice_2(dic, num)

    else:
      if dic["partite"] == False:
        print("parser: sw")
        self.parse_sa_whole(dic)

      else:
        print("parser: sp")
        self.parse_sa_partite(dic)
