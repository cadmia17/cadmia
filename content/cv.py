from random import choice

def choose_vector_question():
  if choice([False, False]): #stub, change to True
    from q_vectors_perpendicular import return_question

  else:
    from q_vectors_parallel import return_question
  
  return return_question()

print(choose_vector_question())