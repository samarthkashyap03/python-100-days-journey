def calculate_love_score(name1,name2):
    name1=list(name1)
    name2=list(name2)
    name1.extend(name2)
    count1=0
    for i in "true":
        a=name1.count(i)
        count1+=a
    count2=0
    for i in "love":
        a=name1.count(i)
        count2+=a
    print(f"The love score is {str(count1)+str(count2)}")
calculate_love_score("samarth kashyap", "priya sindhe")