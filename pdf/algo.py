import importlib.util as ilu
from random import choice
import json

sa_topics = ["q_polys", "q_vectors_parallel", "q_vectors_perpendicular", "mc_vectors_parallel"]
mc_topics = ["mc_vectors_parallel"]

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


def generate_mc(num):
  for q in range(1, num + 1):
    random_topic = choice(mc_topics)
    load_mod(random_topic, q)


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


from settings import settings
s = settings()
assign_sa_marks(s=s)