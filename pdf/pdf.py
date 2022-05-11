import texit, json

pdf = texit.PDF()

output_location = "output.pdf"

#pdf.MARKDOWN_UNDERLINE_MARKER = "---"

#pdf.set_left_margin(24)
#pdf.set_top_margin(24)
#pdf.set_draw_color(0) #black outline

#pdf.add_page() #title page


sth = 6.5 #standard title [page] height

q_1_json = open("pdf/q_1.json")
q_1 = json.load(q_1_json)

pdf.title_page(pen="black")


#pdf.set_left_margin(23)

#pdf.multiple_choice(n=1, question=q1)

pdf.parse(q_1)


pdf.output(output_location)


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