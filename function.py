

"""principal=int(input("Enter principal amount"))
rate=float(input("Enter intrest rate"))
time=int(input("Enter the time"))

def calculate_simple_interest(principal, rate, time):
    Simple_intrest=(principal * rate * time) / 100
    total_amount=principal + Simple_intrest
    return Simple_intrest, total_amount
simple_interest, total_amount = calculate_simple_interest(principal, rate, time)
print(f"Simple intrest: {simple_interest}")
print(f"Total amount: {total_amount}")"""


"""def calculate_simple_interest(principal, rate, time):
    simple_interest=(principal * rate * time) / 100
    total_amount=principal + simple_interest
    return simple_interest, total_amount
result=calculate_simple_interest(principal, rate, time)
print(result)
#87654
# 8
# 48766
# print(result[1])
#result = calculate_simple_interest(principal, rate, time)
#print(result[0])
#print(result[1])"""


def welcome_message(student,course):
        if course==None:
            print("Welcome {student}!You have sucessfully enrolled in the Python course")
        else:
            print("Welcome {student}!You have sucessfully enrolled in the {course} course")
        return