#!/usr/bin/env python3

import numpy as np
import random

participants = [
  #"Amit",
  "Neil",
  "Mike W.",
  #"Sam",
  #"Theano",
  #"Jianan",
  "Jeff",
  "Anja",
  "Nick",
  "Shai",
  "Natalie",
  #"Khiem",
  #"Zhenyu",
  #"Ashwini",
  #"David",
  #"Dongsheng",
  "Nan",
  #"Wyatt",
  "Yue",
  "Jingyuan C.",
  "Leon S.",
  "Chris H.",
  "Chris A.",
  "Jennifer",
  #"Yushan",
  "Gongqi H.",
]

group_size = 3
num_groups = len(participants) // group_size
random.shuffle(participants)
grouping = np.array_split(participants, num_groups)
for i, g in enumerate(grouping):
  print("Group %s: %s" % (i, ", ".join(g)))

