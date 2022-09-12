import content.ext_math as ext_math
import random

def vectorise(ar):
  return f"({ar[0]}, {ar[1]})"

def generator(all=[-4, -3, -2, -1, 2, 3, 4, 5]):
  [pi, pj, qi, qj] = random.sample(all, k=4)

  op = [pi, pj]
  oq = [qi, qj]

  pq = ext_math.v_sub(oq, op)

  #PQ = PO + OQ = -OP + OQ = OQ - OP

  return {
    "op": op,
    "oq": oq,
    
    "a": vectorise(pq),
    "b": vectorise(ext_math.v_add(oq, op)),
    "c": vectorise(ext_math.v_add(ext_math.v_neg(oq), op)),
    "d": vectorise(ext_math.v_add(ext_math.v_neg(oq), ext_math.v_neg(op))),
    
    "sol": {
      "n": vectorise(pq)
    }
  }

def create_question(op, oq):
  return f"Given that the vector OP> = {vectorise(op)} and the vector OQ> = {vectorise(oq)}, what is the vector PQ>?"

def return_question():
  dict_ints = generator()
  question = create_question(dict_ints["op"], dict_ints["oq"])
  
  s = dict_ints["sol"]["n"]

  answers = [dict_ints["a"], dict_ints["b"], dict_ints["c"], dict_ints["d"]]
  random.shuffle(answers)

  sol_letter = ""

  #get letter of answer
  for a in range(0, len(answers)):
    #print(f"s: {s}, a: {a}, answers[a]: {answers[a]}")
    if s == answers[a]:
      sol_letter = ext_math.num_to_let(a + 1)

  question_dic = {
    "type": "multiple_choice",
    "question": question,
    "answer": sol_letter,
    "answer_a": answers[0],
    "answer_b": answers[1],
    "answer_c": answers[2],
    "answer_d": answers[3],
  }
  
  return question_dic