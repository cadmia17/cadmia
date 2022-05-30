import json, math

def get_mc(time): #multis given time
  return math.ceil(time / 12)


def get_sa_marks(time): #marks of short section given time
  return math.ceil(time / 2)


def get_sa_questions(marks):
  pass


k = open("settings.json")
settings = json.load(k)

time = settings["time"]
difficulty = settings["difficulty"]
blocklist = settings["blocklist"]
#extra_names = settings["extra_names"]

mc_marks = get_mc(time)
sa_marks = get_sa_marks(time)

final_settings = {
  "marks": mc_marks + sa_marks,
  "time": time,
  "mc_marks": mc_marks,
  "mc_time": mc_marks,
  "sa_marks": sa_marks,
  "sa_time": time - mc_marks,
  "difficulty": difficulty,
  "blocklist": blocklist
}

def settings():
  return final_settings

#cry