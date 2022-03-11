import ext_math

def generator(n=[-4, 4], a=[-4, 4], b=[-4, 4], c=[-4, 4], d=[-4, 4], p=[-4, 4], q=[-4, 4]):
  n = ext_math.rand(n, blacklist=[0])
  a = ext_math.rand(a, blacklist=[0])
  b = ext_math.rand(b, blacklist=[0])
  c = ext_math.rand(c, blacklist=[0])
  d = ext_math.rand(d, blacklist=[0])
  p = ext_math.rand(p, blacklist=[0])
  q = ext_math.rand(q, blacklist=[0])

  if ext_math.real(a*c, a*d + b*c, b*d - p*q):
    return {
      "a": a,
      "b": b,
      "c": c,
      "d": d,
      "p": p,
      "q": q,
      "sol": {
        "n": n
      }
    }

  else:
    return generator()

def create_question(a, b, c, d, p, q):
  return f"For what values of n are ({ext_math.lead(a)}n {ext_math.const(b)}, {p}) and ({q}, {ext_math.lead(c)}n {ext_math.const(d)}) parallel?"

def return_question():
  dict_ints = generator()
  question = create_question(dict_ints["a"], dict_ints["b"], dict_ints["c"], dict_ints["d"], dict_ints["p"], dict_ints["q"])
  return question