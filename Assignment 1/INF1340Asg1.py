#
# INF1340, Section LEC0101
# Assingment 1 - Due 2018-10-15
# Wilson, Courtney
#
# POS Program for MinMax
# v.1.4 - 2018-10-14
# Compatibale with Python version 3.7
# Source File: INF1340Asg1.py
#


def display_welcome():
    """
    Displays the welcome message when the program is started
    @rtype: None
    """
    print("Welcome to MinMax! Please Begin Scanning: \n")

def display_goodbye():
    """
    Displays the goodbye message when the program has ended
    @rtype: None
    """
    print("Thank You For Using MinMax!")

def get_barcode():
    """ (None) -> str
    Returns the <barcode> that is inputted by the user
    @rtype: str
    >>>Input = '111111'
    111111
    >>>Input = '666666'
    666666
    """
    barcode = input("Input Barcode: \n")
    return barcode
    
def caculate_subtotal(number_of_singles,number_of_smalls,number_of_larges):
    """ (int, int, int) -> float
    Returns the <subtotal_before_tax> after multipling each <number_of_singles>,
    <number_of_smalls> and <number_of_larges> by its respective selling price.
    @type number_of_singles: int
    @type number_of_smalls: int
    @type number_of_larges: int
    @rtype: float
    >>calculate_subtotal(1,1,1)
    25
    >>calculate_subtotal(3,5,6)
    142
    """

    #Price constants for easier readability
    PRICE_SINGLE = 1.00 
    PRICE_SMALL = 5.00
    PRICE_LARGE = 19.00
    
    singles_price = number_of_singles * PRICE_SINGLE
    smalls_price = number_of_smalls * PRICE_SMALL
    larges_price = number_of_larges * PRICE_LARGE

    subtotal_before_tax = singles_price + smalls_price + larges_price
    return subtotal_before_tax

def calculate_hst_tax(subtotal_before_tax):
    """(float) -> float
    Returns <hst> calculated from the <subtotal_before_tax>.
    @type subtotal_before_tax: float
    @rtype: float
    >>calcualate_hst_tax(21.55)
    1.7240000000000002
    >>calculate_hst_tax(5.00)
    0.4
    """
    #Price constant for easier readability 
    HST_RATE = 0.08 
    
    hst = subtotal_before_tax * HST_RATE
    return hst

def calculate_total_bill(subtotal_before_tax,hst):
    """ (float, float) -> float
    Returns <total_bill> by adding <subtotal_before_tax> with <hst>
    @type subtotal_before_tax: float
    @type hst: float
    @rtype: float
    >>calculate_total_bill(56.42, 3.01)
    59.43
    >>calculate_total_bill(22.03, 1.45)
    23.48
    """    
    total_bill = subtotal_before_tax + hst
    return total_bill
    
def display_total_bill(subtotal_before_tax,hst,total_bill,total_bill_rounded):
    """ (float, float, float) -> NoneType
    Displays the <subtoal_before_tax>, <hst>, <total_bill> and <total_bill_rounded> to the user.
    @type subtotal_before_tax: float
    @type hst: float
    @type total_bill: float
    @type total_bill_rounded: float
    @rtype: NoneType
    """
    print("Subtotal Before Tax: ")
    print(format_num(subtotal_before_tax))
    print("Total HST: ")
    print(format_num(hst))
    print("Total Bill: ")
    print(format_num(total_bill))
    print("Bill Rounded: ")
    print(format_num(total_bill_rounded))
    
def format_num(num):
    """(float) -> str
    Returns formatted <num> to display only two decimals places.
    @type num: float
    @rtype: str
    >>format_num(1.1)
    1.10
    >>format_num(34.534)
    34.53
    """
    num = '{:.2f}'.format(num)
    return num

def round_to_fifth(num):
    """ (float) -> float
    Returns rounded <num> to the neartest 0.05.
    @type num: float
    @rtype: float
    >>round_to_fifth(47.32)
    47.3
    >>round_to_fifth(72.23424234)
    72.25
    """
    num = round(0.05*round(num/0.05),2)
    return num

def get_amount_tendered(total_bill):
    """ (float) -> float
    Returns <amount_tendered> by subtracting the amount the user inputted to pay by the
    <total_bill>. If the user inputted value is less than the <total_bill>, user will be
    prompted to enter a different value. 
    @type total_bill: float
    @rtype: float
    >>get_amount_tendered(44.50)
    <amount_tendered> = 50
    5.5
    >>get_amount_tendered(35.00)
    <amount_tendered> = 40
    5
    """
    amount_tendered = float(input("Please Input Amount You Want to Pay, Enter '0' to Cancel Order: "))

    #Checks if the input amount is less then the total_bill passed.
    #Checks if the input amount is 0, for cancelled order
    while amount_tendered < total_bill and amount_tendered != 0:
       amount_tendered = float(input("Input Value Not Enough For Payment, Please Try Again: "))

    #Transaction will end of input amount is 0 (not 0.00)
    if amount_tendered == 0:
        print("Your order has been cancelled")
        return 0
        
    return amount_tendered      
        
def display_change(total_bill,amount_tendered):
    """ (float, float) -> NoneType
    Prints the change calcualted from <total_bill> and <amount_tendered>
    @type total_bill: float
    @type amount_tendered: float
    @rtype: NoneType
    >>display_change(54.00,60.00)
    6
    >>display_change(35.00,50.00)
    15
    """
    print("Your Change: ")
    amount_of_change = format_num(amount_tendered - total_bill)
    print(amount_of_change)
    input("Press Enter to Continue:")
    

if __name__ == '__main__':
    display_welcome()

    #Counter variables for each type of product 
    number_of_singles = 0
    number_of_smalls = 0
    number_of_larges = 0

    subtotal_before_tax = 0 #Running subtotal count as barcodes are being scanned 
    hst = 0 #Running hst total as barcodes are being scanned

    barcode = get_barcode()
    
    while (barcode != '0'):
        if(barcode == '111111'):
            number_of_singles = number_of_singles + 1
            subtotal_before_tax = caculate_subtotal(number_of_singles,number_of_smalls,number_of_larges)
            hst = calculate_hst_tax(subtotal_before_tax)
            barcode = get_barcode()
           
        elif (barcode == '666666'):
                number_of_smalls = number_of_smalls + 1
                subtotal_before_tax = caculate_subtotal(number_of_singles,number_of_smalls,number_of_larges)
                hst = calculate_hst_tax(subtotal_before_tax)
                barcode = get_barcode()
                
        elif (barcode == '242424'):
                number_of_larges = number_of_larges + 1
                subtotal_before_tax = caculate_subtotal(number_of_singles,number_of_smalls,number_of_larges)
                hst = calculate_hst_tax(subtotal_before_tax)
                barcode = get_barcode()
                
        else:
            print("Not Valid Barcode, Please Try Again: \n")
            barcode = input("Input Barcode: \n")

    total_bill = calculate_total_bill(subtotal_before_tax,hst)
    total_bill_rounded = round_to_fifth(total_bill)
    display_total_bill(subtotal_before_tax,hst,total_bill,total_bill_rounded)
    amount_tendered = get_amount_tendered(total_bill_rounded)

    #If return value of amount_tendered is 0, the program will end.
    if amount_tendered == 0:
        display_goodbye()
    else:   
        display_change(total_bill_rounded,amount_tendered)  
        display_goodbye()
