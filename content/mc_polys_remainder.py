import content.ext_math as ext_math
import random

def generator(all=[-4, -3, -2, 1, 2, 3, 4, 5]):
  [p, q, r, s] = random.sample(all, k=4)

  poly_a = 1
  poly_b = -(p + q + r)
  poly_c = (p * q + p * r + q * r)
  poly_d = -(p * q * r)

  mono_b = s
  #x + mono_b

  remainder = (poly_a * (mono_b ** 3)) + (poly_b * (mono_b ** 2)) + (poly_c * (mono_b)) + poly_d

  return {
    "a": poly_a,
    "b": poly_b,
    "c": poly_c,
    "d": poly_d,

    "mb": mono_b,

    "aa": remainder + p,
    "ab": remainder + q,
    "ac": remainder + r,
    "ad": remainder,
    
    "sol": {
      "n": remainder
    }
  }

def trim(num, str):
  if num == 0:
    return ""
  elif abs(num) == 1:
    return f"{ext_math.sign(num)}{str}"
  else:
    return f"{ext_math.const(num)}{str}"

def create_question(a, b, c, d, mb):
  return f"What is the remainder when the polynomial $%{ext_math.lead(a)}x^3 {trim(b, 'x^2')} {trim(c, 'x')} {ext_math.const(d)}$ is divided by $%x {ext_math.const(-mb)}$?"

def return_question():
  dict_ints = generator()
  question = create_question(dict_ints["a"], dict_ints["b"], dict_ints["c"], dict_ints["d"], dict_ints["mb"])
  
  s = dict_ints["sol"]["n"]

  answers = [dict_ints["aa"], dict_ints["ab"], dict_ints["ac"], dict_ints["ad"]]
  random.shuffle(answers)

  sol_letter = ""

  #get letter of answer
  for a in range(0, len(answers)):
    #print(f"s: {s}, a: {a}, answers[a]: {answers[a]}")
    if s == answers[a]:
      sol_letter = ext_math.num_to_let(a + 1)

  question_dic = {
    "type": "multiple_choice",
    "question": str(question),
    "answer": str(sol_letter),
    "answer_a": str(answers[0]),
    "answer_b": str(answers[1]),
    "answer_c": str(answers[2]),
    "answer_d": str(answers[3]),
  }
  
  return question_dic