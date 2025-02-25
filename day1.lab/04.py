#HIGHEST scorer in dictinary

marks = {
    "sss" : 92,
    "aaa" : 87,
    "yyy" : 98

}
highest_scorer = max(marks, key = marks.get)
print(highest_scorer)