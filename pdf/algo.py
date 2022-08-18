import importlib.util as ilu
from random import choice

def load_mod(mod):
  file = mod
  folder = f"/home/runner/cadmia/content/{file}.py"
  
  spec = ilu.spec_from_file_location(file, folder)
  arb_mod = ilu.module_from_spec(spec)
  spec.loader.exec_module(arb_mod)

  print(arb_mod.return_question())


topics = ["q_polys", "q_vectors_parallel", "q_vectors_perpendicular"]
random_topic = choice(topics)

load_mod(random_topic)