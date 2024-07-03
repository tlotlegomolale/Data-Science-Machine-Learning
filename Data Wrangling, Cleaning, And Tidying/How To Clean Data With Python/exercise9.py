import codecademylib3_seaborn
import pandas as pd
from students import students

print(students.grade.head())

students.grade = students.grade.str.split('(\d+)', expand=True)[1]

print(students.dtypes)

students.grade = pd.to_numeric(students.grade)
avg_grade = students.grade.mean()

print(avg_grade)
