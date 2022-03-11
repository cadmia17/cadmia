from random import choice

def choose_comb_question():
  if choice([True, False]):
    from q_combs_circle import return_question

  else:
    pass
  
  return return_question()

print(choose_comb_question())