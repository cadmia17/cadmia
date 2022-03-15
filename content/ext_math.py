from random import randint, choice
import math
import json

v = False


def vprint(text): #basic verbosity printer
  if v:
    print(text)


def dot_product(v1, v2):
  return v1[0]*v2[0] + v1[1]*v2[1]


def sign(n):
  if n > 0:
    return "+"
  else:
    return "-"


def ss(n): #strip sign
  if n > 1:
    return str(n)
  elif n == 1:
    return ""
  elif n == 0:
    return str(n)
  elif n == -1:
    return "-"
  else:
    return str(n)[1:]


def rand(n, blacklist=[]):
  r = randint(n[0], n[1])
  if r not in blacklist:
    return r
  return rand(n, blacklist=[])


def name(num): #wip #RANDOM.SAMPLE
  names = open("names.json")
  n = json.load(names)

  keys = list(n.keys())
  vals = list(n.values())

  name_list = []

  for key in range(len(keys)):
    keyval = vals[key] #how much of a key there is
    vprint(f"{key}, {keyval}")

    for val in range(keyval):
      name_list.append(keys[key]) #adds the key to the list val times

  vprint(name_list)

  returned_names = []

  for i in range(num):
    random_name = choice(name_list)
    vprint(f"random_name: {random_name}")
    returned_names.append(random_name)

    j = 0

    while j < len(name_list):

      vprint(f"  j: {j}  nl: {name_list[j]}")

      if name_list[j] == random_name:
        name_list.pop(int(j))
      
      else:
        j += 1

  names.close()
  return returned_names


#print(name(4))


def real(a, b, c): #checks if a quad has real solns
  if b*b - 4*a*c >= 0: #discriminant
    return b*b - 4*a*c
  return False


def quad_formula(a, b, c):
  r = real(a, b, c)

  if r > 0:
    positive = (-b + math.sqrt(r)) / 2*a
    negative = (-b - math.sqrt(r)) / 2*a

    return [positive, negative]
  
  elif r == 0:
    return [-b / 2*a]
  
  else:
    return []













def lead(n): #small strip sign #lead coeff
  if n > 1:
    return f"{n}"
  
  elif n == 1:
    return ""
  
  elif n == 0:
    return f"0" #todo: AAAAAAAAAAAAA
  
  elif n == -1:
    return "-"
  
  else:
    return f"-{-n}"


def coeff(n): #small strip sign
  if n > 1:
    return f"+ {n}"
  
  elif n == 1:
    return "+ "
  
  elif n == 0:
    return f"+ 0" #todo: AAAAAAAAAAAAA
  
  elif n == -1:
    return "- "
  
  else:
    return f"- {-n}"


def const(n): #small strip sign
  if n > 0:
    return f"+ {n}"

  elif n == 0:
    return f"+ 0" #todo: AAAAAAAAAAAAA

  else:
    return f"- {-n}"