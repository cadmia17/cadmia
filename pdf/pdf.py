import texit, json

pdf = texit.PDF()

#pdf.MARKDOWN_UNDERLINE_MARKER = "---"

#pdf.set_left_margin(24)
#pdf.set_top_margin(24)
#pdf.set_draw_color(0) #black outline

#pdf.add_page() #title page


sth = 6.5 #standard title [page] height

q_1_json = open("pdf/q1.json")
q_1 = json.load(q_1_json)

pdf.title_page(pen="black")





#pdf.set_left_margin(23)
pdf.set_top_margin(19)
pdf.add_page() #page 1 of mc

pdf.set_font("Times", "B", size=14)
pdf.cell(200, 15, txt="Section I", ln=1, align="L")


pdf.set_font("Times", "B", size=12)
pdf.cell(200, 5, txt="10 marks", ln=1, align="L")
pdf.cell(200, 5, txt="Attempt Questions 1--10", ln=1, align="L")
pdf.cell(200, 5, txt="Allow about 15 minutes for this section", ln=1, align="L")

pdf.set_font("Times", size=12)
pdf.cell(150, 15, txt="Use the multiple-choice answer sheet for Questions 1--10.", border="B", ln=1, align="L")



pdf.multiple_choice(n=1, question=q_1)

pdf.parse(q_1)


pdf.output("unfunny.pdf")


s = open("pdf/stats.txt")
k = 0
for line in s:
  end = line.split(": ")
  k = int(end[-1].strip())
s.close()

s = open("pdf/stats.txt", "w")
s.write(f"pdfs generated: {k + 1}")
s.close()




#todo: clean up files that start with _

#for file in open("/pdf"):
#  if file.startswith("_"):
#    os.del(file)