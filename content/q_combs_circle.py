import ext_math

def generator(n=[5, 10]):
  n = ext_math.rand(n)
  
  return {
    "n": n,
  } #refer to physical documentation for validation

def create_question(n, name="Alex"):
  return f"Alex {n} is sussy"

def return_question():
  dict_ints = generator()
  question = create_question(dict_ints["n"], name=ext_math.name(1)[0])
  return question

#print(return_question())