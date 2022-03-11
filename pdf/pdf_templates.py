from fpdf import FPDF

class PDF(FPDF):
  def dummy(self, x, y):
    self.cell(x, y, txt="", ln=2)
  
  def title_page(self, sth=6.5, year=2022, rtime=10, pen="black", logo="pdf/nsw_logo.png"):
    self.MARKDOWN_UNDERLINE_MARKER = "---" #fixes weird mkdown bug
    self.sth = sth
    
    self.set_left_margin(24)
    self.set_top_margin(24)
    self.set_draw_color(0)

    self.add_page()
    
    self.image(logo, w=24) #forgery
    self.ln(h=4)
    
    self.set_font("Helvetica", size=13)
    self.cell(w=200, h=10, txt="NSW Education Standards Authority", ln=1, align="L")
    self.ln(h=27)
    
    self.set_font("Helvetica", "B", size=15.5)
    self.cell(None, 7, txt=f"{year}", border=1, ln=0, align="L")
    
    self.set_font("Helvetica", "B", size=10.5)
    self.cell(200, 10, txt=" HIGHER SCHOOL CERTIFICATE EXAMINATION", ln=1, align="L")
    self.ln(h=1)
    
    self.set_font("Helvetica", size=32.5)
    self.cell(200, 15, txt="Mathematics Extension 1", ln=1, align="L")
    self.ln(h=10)
    
    
    
    
    
    self.set_font("Helvetica", "B", size=12)
    self.cell(30, sth, txt="General", ln=0, align="L", border="T")
    self.set_font("Helvetica", size=12)
    self.cell(30, sth, txt=f" * Reading time -- {rtime} minutes", ln=1, align="L")
    
    
    self.set_font("Helvetica", "B", size=12)
    self.cell(30, sth, txt="Instructions", ln=0, align="L")
    self.set_font("Helvetica", size=12)
    self.cell(30, sth, txt=" * Working time -- 2 hours", ln=2, align="L") #ln=2 here!
    
    
    self.cell(30, sth, txt=f" * Write using {pen} pen", ln=2, align="L")
    
    self.cell(30, sth, txt=" * Calculators approved by NESA may be used", ln=2, align="L")
    
    self.cell(30, sth, txt=" * A reference sheet is provided at the back of this paper", ln=2, align="L")
    
    self.multi_cell(135, sth, txt=" * For questions in Section II, show relevant mathematical reasoning and/or calculations", ln=2, align="L")
    
    self.multi_cell(135, sth, txt=" * Write your Centre Number and Student Number on the Question 12 Writing Booklet attached", ln=2, align="L")
    
    
    
    self.ln(h=10)
    
    
    
    self.set_font("Helvetica", "B", size=12)
    self.cell(30, sth, txt="Total marks:", ln=0, align="L", border="T")
    self.set_font("Helvetica", size=12)
    self.cell(30, sth, txt="**Section I -- 10 marks** (pages 2-6)", ln=1, align="L", markdown=True)
    
    
    self.set_font("Helvetica", "B", size=12)
    self.cell(30, sth, txt="70", ln=0, align="L")
    self.set_font("Helvetica", size=12)
    self.cell(30, sth, txt=" * Attempt Questions 1-10", ln=2, align="L") #ln=2 here!
    
    self.cell(30, sth, txt=" * Allow about 15 minutes for this section", ln=2, align="L")
    
    
    
    self.ln(h=3)
    
    
    self.cell(30, sth, txt="", ln=0, align="L")
    self.cell(30, sth, txt="**Section II -- 60 marks** (pages 2-6)", ln=2, align="L", markdown=True)
    self.cell(30, sth, txt=" * Attempt Questions 11-14", ln=2, align="L")
    self.multi_cell(135, sth, txt=" * Allow about 1 hour and 45 minutes for this section", ln=2, align="L")










  
  def multiple_choice(self, n=1, question={}, sth=6.5):
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