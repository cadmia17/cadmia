from math import ceil

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


def settings(time=120, difficulty=1.0, blocklist=[], pen="black"):
  time = ceil(time)

  if time >= 300:
    time = 300
  elif time <= 30:
    time = 30

  
  print(f"3set time={time}")
  return {
    "marks": get_mc(time) + get_sa_marks(time),
    "time": time,
    "qns": get_sa_questions(get_sa_marks(time)) + get_mc(time),
    "mc_marks": get_mc(time),
    "mc_time": get_mc(time),
    "sa_marks": get_sa_marks(time),
    "sa_time": time - get_mc(time),
    "sa_qns": get_sa_questions(get_sa_marks(time)),
    "difficulty": difficulty,
    "blocklist": blocklist,
    "pen": pen
  }

#cry
#22/8: not sure when the above comment was made but it fits
#25/8: lmao
#27/8: checked the commit history and it was somewhere between 11/5 and 30/5