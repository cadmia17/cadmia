import texit, json, algo
from settings import settings

s = settings()

pdf = texit.PDF()
sth = 6.5

output_location = "pdf/output.pdf"

#q_11_a_json = open("pdf/q/q_11_a.json")
#q_11_a = json.load(q_11_a_json)

#q_11_b_json = open("pdf/q/q_11_b.json")
#q_11_b = json.load(q_11_b_json)



pdf.title_page()
pdf.multiple_choice(s=s)

for mc in range(1, s["mc_marks"] + 1):
  q_mc_json = open(f"pdf/q/q_{mc}.json")
  q_mc = json.load(q_mc_json)
  
  pdf.parse(q_mc, mc)

#pdf.parse(q_11_a)
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