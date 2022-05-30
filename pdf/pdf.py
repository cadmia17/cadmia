import texit, json
from settings import settings

s = settings()

pdf = texit.PDF()
pen = "black"
sth = 6.5


output_location = "pdf/output.pdf"

q_1_json = open("pdf/q_1.json")
q_1 = json.load(q_1_json)

q_11_a_json = open("pdf/q_11_a.json")
q_11_a = json.load(q_11_a_json)

q_11_b_json = open("pdf/q_11_b.json")
q_11_b = json.load(q_11_b_json)



pdf.title_page(pen=pen)
pdf.multiple_choice(questions_mc=s["mc_time"])


pdf.parse(q_1)
pdf.parse(q_11_a)
#pdf.parse(q_11_b)


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