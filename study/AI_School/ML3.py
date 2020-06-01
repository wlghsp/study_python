import pandas as pd

store_a = pd.Series([20,21,23,22,26,28,35,35,41,42,43,44,45,46,47,47,46,4758,58,59,60,56,57,57,80])
store_b = pd.Series([5,6,11,13,15,16,20,20,21,23,22,27,27,30,30,32,36,37,37,40,40,43,44,45,51,54,70,600])

A_Q1 = store_a.quantile(0.25) ; print("1사분위수 : ",A_Q1)
A_Q2 = store_a.quantile(0.50) ; print("2사분위수(중앙값) : ",A_Q2)
A_Q3 = store_a.quantile(0.75) ; print("3사분위수 : ",A_Q3)
A_Q4 = store_a.quantile(1) ; print("4사분위수 : ",A_Q4)

B_Q1 = store_b.quantile(0.25) ; print("1사분위수 : ",B_Q1)
B_Q2 = store_b.quantile(0.50) ; print("2사분위수(중앙값) : ",B_Q2)
B_Q3 = store_b.quantile(0.75) ; print("3사분위수 : ",B_Q3)
B_Q4 = store_b.quantile(1) ; print("4사분위수 : ",B_Q4)


