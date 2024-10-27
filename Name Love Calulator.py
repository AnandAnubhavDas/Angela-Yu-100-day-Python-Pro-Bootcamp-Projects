def calculate_love_score(name1,name2):
    list_name=[]
    name1=name1.lower()
    name2=name2.lower()
    for letter in (name1+name2):
        list_name.append(letter)
    true=["t","r","u","e"]
    count=0
    for letter in list_name:
        if letter in true:
            count+=1
    love=["l","o","v","e"]
    count2=0
    for letter in list_name:
        if letter in love:
            count2+=1
    print(f"Your love score is: {count}{count2}")
print("Welcome to love calculator!")
first_name=input("Enter name of the first person")
second_name=input("Enter name of the second person")
calculate_love_score(first_name,second_name)
