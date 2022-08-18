from random import choice
import json

all_topics = ["addition", "subtraction"]

def generate_multiple_choice(mc_questions):
  for t in range(1, mc_questions + 1):
    topic = choice(all_topics)
    print(f"topic {topic} generated, glumbs up")

    add = {
      "type": "multiple_choice",
      "question": "sus $%+$ ratio",
      "answer_a": "%1",
      "answer_b": "%2",
      "answer_c": "%3",
      "answer_d": "%4"
    }

    sub = {
      "type": "multiple_choice",
      "question": "sus $%-$ ratio",
      "answer_a": "%1",
      "answer_b": "%2",
      "answer_c": "%3",
      "answer_d": "%4"
    }

    dic = choice([add, sub])
    
    with open(f"pdf/q/q_{t}.json", "w") as out:
      json.dump(dic, out)

generate_multiple_choice(10)

#30722 6292: h it g b__r, lv
#128: 