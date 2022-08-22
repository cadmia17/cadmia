import json
from math import ceil
from random import randrange

def get_mc(time): #multis given time
  return ceil(time / 12)


def get_sa_marks(time): #marks of short section given time
  return ceil(time / 2)


def get_sa_questions(marks): #questions given marks
  if marks < 32: #hardcoded, really not sorry tbh
    return 2
  elif marks < 52:
    return 3
  elif marks < 70:
    return 4
  return 5


k = open("settings.json")
settings = json.load(k)

#time = settings["time"]
time = randrange(60, 125, 5)
difficulty = settings["difficulty"]
blocklist = settings["blocklist"]
pen = settings["pen"]
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
  "blocklist": blocklist,
  "pen": pen
}

def settings():
  return final_settings

#cry