def sample(*args):
    if args:
        return sum(args), sum(args)/len(args)
    else:
        return 0, 0

Total_Marks, Average_Marks = sample(65,35,67,89,53)

print('Total Marks: ', Total_Marks)

print('Average Marks: ', Average_Marks)

Total_Marks, Average_Marks = sample()

print('Total Marks: ', Total_Marks)

print('Average Marks: ', Average_Marks)