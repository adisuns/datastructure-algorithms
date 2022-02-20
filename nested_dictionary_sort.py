"""
{'Nikhil' : {'English' : 5, 'Maths' :  2, 'Science' : 14},
             'Akash' : {'English' : 15, 'Maths' :  7, 'Science' : 2},
             'Akshat' : {'English' : 5, 'Maths' :  50, 'Science' : 20}
"""




mydict = {'Nikhil' : {'English' : 5, 'Maths' :  2, 'Science' : 14},
            'Akash' : {'English' : 15, 'Maths' :  7, 'Science' : 2},
            'Akshat' : {'English' : 5, 'Maths' :  50, 'Science' : 20}}
sorted_dict = {}
studList =[]
marksheets = []
newdict= {}
for name in mydict:
    studList.append(name)
    sorted_marksheets = sorted(mydict[name].values())

    for score in sorted_marksheets:
        for subject in mydict[name].keys():
            if mydict[name][subject] == score:
                sorted_dict[subject] = score
                marksheets.append((subject,score))
    id = dict(marksheets)
    newdict[name] = id
    marksheets.clear()
print(newdict)
    

#     new_dict = dict.fromsubject(studList,sorted_dict)
# print(new_dict)
