import codecademylib3_seaborn
import pandas as pd
from students import students

score_mean = students.score.mean()

print(score_mean)

students = students.fillna(0)

score_mean_2 = students.score.mean()

print(score_mean_2)
