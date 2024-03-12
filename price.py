def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price
    

def main():
    original_price = float(input("Enter the original price of item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    #calculate final price using calcutate_discount function
    final_price = calculate_discount(original_price, discount_percent)

    #print final price
    if final_price != original_price:
        print(f"The final price is: ${final_price:.2f}")

    else:
        print(f"The final price is: ${original_price:.2f}")

main()        