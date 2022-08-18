import ext_math

def generator(n=[-4, 4], a=[-2, 4], b=[-3, 4], c=[-4, 5]):
  n = ext_math.rand(n, blacklist=[0])
  a = ext_math.rand(a, blacklist=[0])
  b = ext_math.rand(b)
  c = ext_math.rand(c, blacklist=[0])
  
  return {
    "a": ext_math.ss(a),
    "b": (b - a*n),
    "c": (c - b*n),
    "d": -c*n,
    "n": n,
  } #refer to physical documentation for validation

def create_question(a, b, c, d, n):
  return f"Let $%P(x) = {a}x^3 {ext_math.sign(b)} {ext_math.ss(b)}x^2 {ext_math.sign(c)} {ext_math.ss(c)}x {ext_math.sign(d)} {ext_math.ss(d)}$:\n\n    i) Show that $%P({n}) = 0$.\n    ii) Hence, factor the polynomial $%P(x)$ as $%A(x)B(x)$, where $%B(x)$ is a quadratic polynomial."

def return_question():
  dict_ints = generator()
  question = create_question(dict_ints["a"], dict_ints["b"], dict_ints["c"], dict_ints["d"], dict_ints["n"])
  return question

#print(return_question())