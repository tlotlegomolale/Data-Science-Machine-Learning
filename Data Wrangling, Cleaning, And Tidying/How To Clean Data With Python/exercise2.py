import codecademylib3_seaborn
import pandas as pd
import glob

student_files = glob.glob("exams*.csv")

df_list = []

for filename in student_files:
  df_list.append(pd.read_csv(filename))
  
students = pd.concat(df_list)

print(students.head())
print(len(students))
