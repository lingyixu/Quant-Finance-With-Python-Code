condition1_1 = True
condition1_2 = True
condition2_1 = True
condition2_2 = True

if (condition1_1) and (condition1_2):
    print("call function1()")
elif (condition2_1) or not (condition2_2):
    print("call function2()")
else:
    print("call function3()")