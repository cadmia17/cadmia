import importlib.util as ilu
from random import choice
import json

#topics = ["q_polys", "q_vectors_parallel", "q_vectors_perpendicular", "mc_vectors_parallel"]
topics = ["mc_vectors_parallel"]

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
    random_topic = choice(topics)
    load_mod(random_topic, q)