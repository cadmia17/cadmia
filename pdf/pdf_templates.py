from fpdf import FPDF
from settings import settings


class PDF(FPDF):
  set = settings()
  print(set)

  def dummy(self, x, y):
    self.cell(x, y, txt="", ln=2)
  
  def title_page(self, sth=6.5, year="2022", s=set, logo="pdf/nsw_logo.png"):
    self.MARKDOWN_UNDERLINE_MARKER = "---" #fixes weird mkdown bug
    self.sth = sth
    self.DASH = "--" #en soon hopefully
    
    self.set_left_margin(24)
    self.set_top_margin(24)
    self.set_draw_color(0)

    self.add_page()
    
    self.image(logo, w=24, alt_text="NSW government logo")
    self.ln(h=4)
    
    self.set_font("Helvetica", size=13)
    self.cell(w=200, h=10, txt="NSW Education Standards Authority", ln=1, align="L")
    self.ln(h=27)
    
    self.set_font("Helvetica", "B", size=15.5)
    self.cell(w=14, h=7, txt=year, border=1, ln=0, align="C") #year
    
    self.set_font("Helvetica", "B", size=10.5)
    self.cell(200, 10, txt=" HIGHER SCHOOL CERTIFICATE EXAMINATION", ln=1, align="L")
    self.ln(h=1)
    
    self.set_font("Helvetica", size=32.5)
    self.cell(200, 15, txt="Mathematics Extension 1", ln=1, align="L")
    self.ln(h=10)
    
    
    self.set_font("Helvetica", "B", size=12)
    self.cell(30, sth, txt="General", ln=0, align="L", border="T")
    self.set_font("Helvetica", size=12)
    self.cell(30, sth, txt=f" * Reading time {self.DASH} {s['mc_time']} minutes", ln=1, align="L")
    
    
    self.set_font("Helvetica", "B", size=12)
    self.cell(30, sth, txt="Instructions", ln=0, align="L")
    self.set_font("Helvetica", size=12)
    self.cell(30, sth, txt=f" * Working time {self.DASH} {s['time']} minutes", ln=2, align="L")
    
    
    self.cell(30, sth, txt=f" * Write using {s['pen']} pen", ln=2, align="L")
    
    self.cell(30, sth, txt=" * Calculators approved by NESA may be used", ln=2, align="L")
    
    self.cell(30, sth, txt=" * A reference sheet is provided at the back of this paper", ln=2, align="L")
    
    self.multi_cell(135, h=sth, txt=" * For questions in Section II, show relevant mathematical reasoning and/or calculations", align="", ln=2)
    
    self.multi_cell(135, h=sth, txt=" * Write your Centre Number and Student Number on all Writing Booklets attached", align="", ln=2)
    
    
    self.ln(h=10)
    
    
    self.set_font("Helvetica", "B", size=12)
    self.cell(30, sth, txt="Total marks:", ln=0, align="L", border="T")
    self.set_font("Helvetica", size=12)
    self.cell(30, sth, txt=f"**Section I {self.DASH} {s['mc_marks']} marks**", ln=1, align="L", markdown=True)
    
    
    self.set_font("Helvetica", "B", size=12)
    self.cell(30, sth, txt=str(s["marks"]), ln=0, align="L")
    self.set_font("Helvetica", size=12)
    self.cell(30, sth, txt=f" * Attempt Questions 1-{s['mc_marks']}", ln=2, align="L") #ln=2 here!
    
    self.cell(30, sth, txt=f" * Allow about {s['mc_time']} minutes for this section", ln=2, align="L")
    
    
    self.ln(h=3)
    
    
    self.cell(30, sth, txt="", ln=0, align="L")
    self.cell(30, sth, txt=f"**Section II {self.DASH} {s['sa_marks']} marks**", ln=2, align="L", markdown=True)
    self.cell(30, sth, txt=f" * Attempt Questions {s['mc_marks'] + 1}-{s['qns']}", ln=2, align="L")
    self.multi_cell(135, sth, txt=f" * Allow about {s['sa_time']} minutes for this section", ln=2, align="L")
  def sus0():
    pass


  
  def multiple_choice(self, sth=6.5, s=set):
    self.sth = sth
    
    self.set_top_margin(19)
    self.add_page() #page 1 of mc
    
    self.set_font("Times", "B", size=14)
    self.cell(200, 15, txt="Section I", ln=1, align="L")
    
    
    self.set_font("Times", "B", size=12)
    self.cell(200, 5, txt=f"{s['mc_marks']} marks", ln=1, align="L")
    self.cell(200, 5, txt=f"Attempt Questions 1{self.DASH}{s['mc_marks']}", ln=1, align="L")
    self.cell(200, 5, txt=f"Allow about {s['mc_time']} minutes for this section", ln=1, align="L") #vary this
    
    self.set_font("Times", size=12)
    self.cell(150, 15, txt=f"Use the multiple-choice answer sheet for Questions 1{self.DASH}{s['mc_marks']}.", border="B", ln=1, align="L")
    self.ln(h=1)
  def sus1():
    pass





  def short_answer(self, sth=6.5, s=set):
    self.sth = sth
    
    self.set_top_margin(19)
    self.add_page() #page 1 of mc
    
    self.set_font("Times", "B", size=14)
    self.cell(200, 15, txt="Section II", ln=1, align="L")
    
    
    self.set_font("Times", "B", size=12)
    self.cell(200, 5, txt=f"{s['sa_marks']} marks", ln=1, align="L")
    self.cell(200, 5, txt=f"Attempt Questions {s['mc_marks'] + 1}-{s['qns']}", ln=1, align="L")
    self.cell(200, 5, txt=f"Allow about {s['sa_time']} minutes for this section", ln=1, align="L")
    self.ln(h=1)







  
  def DEP_multiple_choice(self, n=1, question={}, sth=6.5):
    print(f"mc q{n} starts here")
    self.sus = "amog us"
    self.cell(20, sth, txt="**1**", ln=0, align="L")

    
    self.cell(None, sth, txt=question["question"], ln=2, align="L")

    self.dummy(20, 1)
    self.cell(None, sth, txt=f"A. {question['answer_a']}", ln=2, align="L")
    self.cell(None, sth, txt=f"B. {question['answer_b']}", ln=2, align="L")
    self.cell(None, sth, txt=f"C. {question['answer_c']}", ln=2, align="L")
    self.cell(None, sth, txt=f"D. {question['answer_d']}", ln=1, align="L")
    
    self.ln(h=1) #fix height