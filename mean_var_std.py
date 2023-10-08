import numpy as np


def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  arr = np.array(list).reshape(3, 3)
  #print(arr)
  #arr.mean(0) : mean of columns
  #i.e. [(0+3+6)/3, (1+4+7)/3, (2+5+8)/3]
  #arr.mean(1) : mean of rows
  #i.e. [(0+1+2)/3, (3+4+5)/3, (6+7+8)/3]

  calculations = {
    "mean": [arr.mean(0).tolist(),
             arr.mean(1).tolist(),
             arr.mean()],
    "variance": [arr.var(0).tolist(),
                 arr.var(1).tolist(),
                 arr.var()],
    "standard deviation":
    [arr.std(0).tolist(), arr.std(1).tolist(),
     arr.std()],
    "max": [arr.max(0).tolist(),
            arr.max(1).tolist(),
            arr.max()],
    "min": [arr.min(0).tolist(),
            arr.min(1).tolist(),
            arr.min()],
    "sum": [arr.sum(0).tolist(),
            arr.sum(1).tolist(),
            arr.sum()]
  }

  return calculations
