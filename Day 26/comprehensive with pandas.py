student_dict = {
    "student" : ["Kiet","James","Lily"],
    "score" : [56,76,98]
}

# for (key,value) in student_dict.items():
#     print(value)
import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#Loop through a data frame
# for(key,value) in student_data_frame.items():
#     print(value)

#Loop through row of a data frame
for(index, row) in student_data_frame.iterrows():
    if row.student == "kiet":
        print(row.score)