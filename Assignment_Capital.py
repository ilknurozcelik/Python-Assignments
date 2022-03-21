capital = 1000
interest = 0.07
time = 7
# Assumption : the interest is compound
capital_total = capital * (1 + interest) ** time
print ("The amount of capital will be : " , "{:.2f}".format(capital_total) , "$ at the end of 7 days when we use compound interest.")
