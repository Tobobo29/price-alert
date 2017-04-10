import time

# initialize the varialbes
recent_highest_price = 0
today_opening_price = 0

"""
calculate the selling point: 
1. either down 10% from highest point 
2. or drop more than 5% in today
"""

def calculate_selling_point(recent_highest_price = 0, today_opening_price = 0):
    # input the higest price and today's current price
    print()
    recent_highest_price = int(input("The recent highest price is: "))
    today_opening_price = int(input("Today's opening price is: "))

    # calculate and print selling point, will be the higher one in two situations
    if recent_highest_price * 0.9 > today_opening_price * 0.95:
        selling_point = recent_highest_price * 0.9
    else:
        selling_point = today_opening_price * 0.95

    # print the results
    print()
    print(time.strftime("%Y/%m/%d:"))
    print("The selling point is: %d" % selling_point)
    print()

    # write to the file named reslut, append everytime to the text file
    with open("results.txt", "a+") as result_file:
        result_file.write(time.strftime("%Y/%m/%d:\n"))
        result_file.write("Recent higest price: %d\n" % recent_highest_price)
        result_file.write("Today open price: %d\n" % today_opening_price)
        result_file.write("Selling point: %d\n\n" % selling_point)

 # check the user want to continue or not
while(1):
    calculate_selling_point(recent_highest_price, today_opening_price)
    count = input("Do you want to calculate another one? (y/n): ")
    if count == "n" or count == "N":
        break
