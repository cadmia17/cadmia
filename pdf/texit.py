from urllib.parse import quote as encode
from pdf_templates import PDF
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
  def parse_multiple_choice_2(self, dic, num=1):
    start = self.get_x()
    print(f"\n@ parsing question {num}")
    

    self.cell(w=25, h=self.sth, txt=f"**{num}.**", new_x=XPos.END, new_y=YPos.LAST, markdown=True) #creates 1) etc.

    indent = self.get_x()
    print(f"@ starting x-pos: {indent}")

    #question
    
    val = dic["question"]
    val_list = val.split("$") #splits into text, formula, text, etc

    
    for v in val_list: #iterates for every text and formula
      image_counter = 0

      if v[0] == "%": #formula
        print(f"\n\n@ value = [{v}], formula")
        v = v[1:] #removes leading % indicating formula

        
        x_formula = self.get_x()
        y_formula = self.get_y()


        full_path = f"pdf/q{num}_{image_counter}.png"
        get_formula(v, full_path) #creates the png

        img = Image.open(full_path)
        img_w, img_h = img.size
        
        self.image(img, alt_text=v)

        image_counter += 1


        self.set_x(x_formula + img_w)
        self.set_y(y_formula)

        #self.image(image_link(v), alt_text=v) #gets the link to the image #then appends it to the pdf
        #new_x=XPos.RIGHT, new_y=YPos.TOP
        #which means, add the width of the image and subtract the height

        print(f"x: {self.get_x()}, y: {self.get_y()}")

        

      
      else: #normal text
        print(f"\n\n@ value = [{v}], text")
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

        self.multi_cell(w=0, h=self.sth, txt=v, new_x=(XPos.END), new_y=(YPos.LAST))

    self.set_x(start)
    self.ln(10)




  
  
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
      self.parse_multiple_choice_2(dic)

    else:
      if dic["partite"] == False:
        print("parser: sw")
        self.parse_sa_whole(dic)

      else:
        print("parser: sp")
        self.parse_sa_partite(dic)
