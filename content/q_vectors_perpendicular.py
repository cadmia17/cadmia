import ext_math

def generator(n=[-4, 4]):
  n = ext_math.rand(n, blacklist=[0])
  a = 1
  b = 1
  c1 = 1
  c2 = 1

  return {
    "a": a,
    "b": b,
    "c1": c1,
    "c2": c2,
    "n": n,
  }

def create_question(a, b, c1, c2, n):
  return f"For what values of n are (n, {c1}) and ({a}n + {b}, {c2}) perpendicular?"

def return_question():
  dict_ints = generator()
  question = create_question(dict_ints["a"], dict_ints["b"], dict_ints["c1"], dict_ints["c2"], dict_ints["n"])
  return question