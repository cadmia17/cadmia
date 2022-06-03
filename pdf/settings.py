import json, math
from random import randint

def get_mc(time): #multis given time
  return math.ceil(time / 12)


def get_sa_marks(time): #marks of short section given time
  return math.ceil(time / 2)


def get_sa_questions(marks): #questions given marks
  if marks < 32:
    return 2
  elif marks < 52:
    return 3
  elif marks < 70:
    return 4
  return 5


k = open("settings.json")
settings = json.load(k)

#time = settings["time"]
time = randint(60, 120)
difficulty = settings["difficulty"]
blocklist = settings["blocklist"]
#extra_names = settings["extra_names"]

mc_marks = get_mc(time)
sa_marks = get_sa_marks(time)

final_settings = {
  "marks": mc_marks + sa_marks,
  "time": time,
  "qns": get_sa_questions(sa_marks) + mc_marks,
  "mc_marks": mc_marks,
  "mc_time": mc_marks,
  "sa_marks": sa_marks,
  "sa_time": time - mc_marks,
  "sa_qns": get_sa_questions(sa_marks),
  "difficulty": difficulty,
  "blocklist": blocklist
}

def settings():
  return final_settings

#cry