import importlib.util as ilu
from random import choice
import json

sa_topics = ["q_polys", "q_vectors_parallel", "q_vectors_perpendicular", "mc_vectors_parallel"]

original_mct = {
  "vectors": ["mc_vectors_parallel"],
  "polys": ["mc_polys"],
  "combs": ["mc_combs"]
}

def omct():
  return list(original_mct.keys())

def load_mod(mod, q):
  file = mod
  folder = f"/home/runner/cadmia/content/{file}.py"
  
  spec = ilu.spec_from_file_location(file, folder)
  arb_mod = ilu.module_from_spec(spec)
  spec.loader.exec_module(arb_mod)

  question_dict = arb_mod.return_question()
  
  output = f"pdf/q/q_{q}.json"

  with open(output, "w") as o:
    json.dump(question_dict, o)




def generate_mc(num, blocklist=[]):
  mc_topics = original_mct

  for topic in blocklist:
    mc_topics.pop(topic)
  
  for q in range(1, num + 1):
    topic_keys = list(mc_topics.keys())
    random_topic = choice(topic_keys)
    random_subtopic = choice(mc_topics[random_topic])
    load_mod(random_subtopic, q)


def assign_sa_marks(s):
  #step 1: assign marks to each question
  #luckily i already did question calcs in settings config itself
  print(s)
  sa_marks = []
  
  marks_remaining = s["sa_marks"]
  marks_per_question = s["sa_marks"] // s["sa_qns"]

  for q in range(1, s["sa_qns"] + 1):
    sa_marks.append(marks_per_question)
    marks_remaining -= marks_per_question


def generate_sa(s): #takes settings config as input
  #step 2: generate questions until marks are filled
  #also luckily i did a DFD of this

  pass


from pdf.settings import settings
s = settings()
assign_sa_marks(s=s)