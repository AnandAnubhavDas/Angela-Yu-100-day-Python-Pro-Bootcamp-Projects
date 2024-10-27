import art
def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1-n2
def mult(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
calculate={
    "+":add,
    "-":sub,
    "*":mult,
    "/":div,
}
def calc():
    print(art.logo)
    n1 = int(input("Enter the first number:\n"))
    x=1
    while x>0:
        key=input("Enter the mathematical operator:\n")
        n2=int(input("Enter the second number:\n"))
        print(f"The result is:",calculate[key](n1,n2))
        cont=input("Do you want to continue working with the previous result?Yes or No").lower()
        if cont=="yes":
            n1=calculate[key](n1,n2)
        else:
            calc()
        x+=1
calc()
