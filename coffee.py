#!/usr/bin/env python3

import numpy as np
import random

participants = [
  #"Amit",
  "Sam",
  "Theano",
  "Jianan",
  "Jeff",
  "Anja",
  "Natalie",
  #"Khiem",
  #"Zhenyu",
  #"Ashwini",
  "David",
  #"Dongsheng",
  "Nan",
  #"Wyatt",
  "Yue",
  #"Chris",
  #"Jennifer",
  "Yushan"
]

group_size = 3
num_groups = len(participants) // group_size
random.shuffle(participants)
grouping = np.array_split(participants, num_groups)
for i, g in enumerate(grouping):
  print("Group %s: %s" % (i, ", ".join(g)))

