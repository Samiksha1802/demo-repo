import os
import numpy as np
import pandas as pd

def save_var_latex(key,value):
  import csv
  dict_var={}
  file_path=os.path.join(os.getcwd(),"mydata.dt")
  try:
    with open(file_path,newline="") as file:
      reader = csv.reader(file)
      for row in reader:
        dict_var[[row[[0]] = row[1]
                  except FileNotFoundError:
                  pass
                  dict_var[key] = value
                  
               with open(file_path,"w") as f:
                  for key in dict_var.keys():
                  f.write(f"{key},{dict_var[kay]}\n")
  save_var_latex("number_participants",20)
  df = pd.DataFrame(np.random,rand(20,3),columns=['a','b','c'])
  save_var_latex("total_score",df.sum().sum().round())
