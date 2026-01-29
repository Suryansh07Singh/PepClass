def calc_perc(**marks):
    total_marks=sum(marks.values())
    num_sub=len(marks)
    max_marks=num_sub*100

    percentage=(total_marks/max_marks)*100
    print("Marks:",marks)
    print("Per:",percentage,"%")

calc_perc(maths=79,python=84,java=92)   