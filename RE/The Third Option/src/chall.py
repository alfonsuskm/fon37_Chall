p = [0xc1, 0xde, 0xd8, 0xdf, 0xca, 0xd8, 0xc2, 0xc6, 0xdb, 0xc7, 0xce, 0xd3, 0xc4, 0xd9]

def calculate_bep():
    fixed_cost = int(input("Fixed Production Cost: ").replace(".", ""))
    variable_cost = int(input("Variable Cost/Unit: ").replace(".", ""))
    selling_price = int(input("Selling Price: ").replace(".", ""))

    if selling_price <= variable_cost:
        print("Selling price must be greater than the variable cost.")
        exit()

    bep_unit = int(fixed_cost / (selling_price - variable_cost))
    bep_rp = int(bep_unit * selling_price)

    print("")
    print("BEP/UNIT:", f"{bep_unit:,d}".replace(",", "."))
    print("BEP/RP:", f"{bep_rp:,d}".replace(",", "."))


def decode():
    text = ""
    for i in p:
        text += chr(i ^ 0xab)
    return text


def calculate_roi():
    total_sales = int(input("Total Sales: ").replace(".", ""))
    investment = int(input("Investment: ").replace(".", ""))

    roi_percentage = (total_sales - investment) / investment * 100

    print("")
    print("ROI:", f"{roi_percentage:.2f}%")


def win():
    print("Congratulations, you win!")


def main():
    secret = decode()

    print("1 = BEP, 2 = ROI")
    choice = input("Calculate: ")

    if choice == "1":
        calculate_bep()
    elif choice == secret:
        win()
    else:
        calculate_roi()


if __name__ == "__main__":
    main()