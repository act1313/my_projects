import pandas as pd
import numpy as np
from sklearn import *
from sklearn.utils import shuffle

data = pd.read_csv("student-mat.csv", sep=";")

data = data[["G1","G2","G3","studytime","failures","absences"]]
predict = "G3"

#9:43 seconds on video
