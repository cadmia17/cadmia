import pdf.texit as texit
import json
import pdf.algo as algo
from pdf.settings import settings

STH = 6.5 #another magic number #if i said i was sorry i'd be lying

def increment_pdf_counter():
  s = open("pdf/stats.txt")
  k = 0
  for line in s:
    end = line.split(": ")
    k = int(end[-1].strip())
  s.close()
  
  final_message = f"pdfs generated: {k + 1}"
  
  s = open("pdf/stats.txt", "w")
  s.write(final_message)
  s.close()
  
  print(final_message)


def pdf(time=120, difficulty=1.0, blocklist=[], pen="black", output="pdf/output.pdf"):
  s = settings(time=120, difficulty=1.0, blocklist=[], pen="black")
  
  #Algorithm use
  
  algo.generate_mc(s["mc_marks"])
  #algo.generate_sa(s["sa_marks"])
  
  #PDF generation
  
  pdf = texit.PDF()
  
  
  #Generates title page
  pdf.title_page()


  
  #Generates MC
  pdf.multiple_choice(s=s)
  
  for mc in range(1, s["mc_marks"] + 1):
    q_mc_json = open(f"pdf/q/q_{mc}.json")
    q_mc = json.load(q_mc_json)
    
    pdf.parse(q_mc, mc)


  
  #Generates SA
  #guess what, this is still wip
  #should've done it earlier
  
  #pdf.parse(q_11_a)
  #pdf.parse(q_11_b)
  
  pdf.output(output)
  increment_pdf_counter()




#todo: clean up files that start with _

#for file in open("/pdf"):
#  if file.startswith("_"):
#    os.del(file)