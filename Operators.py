#Sceanrio 1

total_bill = 1370
num_friends = 4
print(f"Equal share per person (rounded down):{total_bill //num_friends}\n"
f"Leftover amount to collect separately:{total_bill % num_friends}\n"
f"Exact fair share per person:{total_bill / num_friends}")


#Sceanrio 2
visting_age=int(input("Enter your age:"))
if visting_age<18:
    print("Entry Denied")
else:
    has_valid_id=input("Do you have a valid ID? (yes/no):")=="yes"
    if not has_valid_id:
            print("Entry Denied")
    else:
            is_movie_full=input("Is the movie full? (yes/no):")=="no"
            if not has_valid_id:
                print("Entry Denied")
            elif is_movie_full:
                print("Entry Allowed")
            else:
                print("Entry Denied")


"""if __name__ == "__main__":
    visting_age=int(input("Enter your age:"))
    if visting_age<18:
        print("Entry Denied")
    else:
        has_valid_id=input("Do you have a valid ID? (yes/no):")=="yes"
        if not has_valid_id:
                print("Entry Denied")
        else:
                is_movie_full=input("Is the movie full? (yes/no):")=="no"
                if not has_valid_id:
                    print("Entry Denied")
                elif is_movie_full:
                    print("Entry Allowed")
                else:
                    print("Entry Denied")"""

"""vistor_age=int(input("Enter the age:"))
if vistor_age <18:
    print("Entry Notallowed")
else:
    has_valid_id =input("Is there any valid id:")=='yes'
    if not has_valid_id:
        print("Entry Notallowed")
    else:
        is_movie_full = input("Is there seat in theatre:")=='yes'
        if is_movie_full:
            print("Entry Allowed")
        else:
            print("Entry Notallowed")"""

#Sceanrio 3
cart_value = int(input("Enter the cart value:"))
coupon_code = input("Enter the Coupon Code:")
is_coupon_expired = input("Is the coupon expired? (yes/no):")=="yes"

discount=10
valid_coupons = [coupon.lower() for coupon in ["SAVE10", "FLAT50", "WELCOME5"]]
#coupon_valid=input(f"coupon valid:{valid_coupons}")
discount_applied=cart_value*discount/100
final_price=cart_value - discount_applied
if coupon_code in valid_coupons and not is_coupon_expired and cart_value>500:
    print(f"cart qualifies(>500):{cart_value}")
    print(f"coupon expired:{is_coupon_expired}")
    print(f"Discount Applied:{discount_applied}")
    print(f"Final Payable Amount:{final_price}")
else:
    print(f"cart qualifies(>500):{cart_value}")
    print(f"coupon expired:{is_coupon_expired}")
    print(f"Discount Applied:0")
    print(f"Final Payable Amount:{cart_value}")


"""stock = 25
reorder_threshold = 10
orders_today = [3, 5, 2, 8]
new_stock_arrived = 4

for orders in orders_today:
    stock-=orders
    print(f"orders placed(orders).stock left:",(stock))
if stock<=reorder_threshold:
    stock+=new_stock_arrived
    print(f"New stock arrived ({new_stock_arrived}).Stock now:",(stock))
print(f"Reorder Alert: No {(stock)}>{(reorder_threshold)}")"""



       