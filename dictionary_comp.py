student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
# print(student_dict)

new_list = {new:main for (new, main) in student_dict.items()}
print(new_list)

for num, life in student_dict.items():
    print(num)
    print(life)

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    print(key, value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    # print(index, row)
    #Access row.student or row.score
    print(row.student)
    print(row.score)


