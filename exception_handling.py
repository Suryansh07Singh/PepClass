'''try:
    x = 10 / 0
    print("Result:", x)
except BaseException as err:
    print("Error: Division by zero is not allowed.")
    print(err)   #What Error is occuring
    print(type(err))   #The error name itself
'''
import os
try:
    print("Working directory:", os.getcwd())
    fh = open("file.txt", "wt")
    fh.write("Hii\nHello")
except Exception:
    print("File Error")
    exit()
finally:    #Executes every time 
    print("Execution Completed")
    fh.close()