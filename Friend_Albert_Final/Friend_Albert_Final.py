#----------------------------------------------------
# Assignment Name: Final
# Name: Albert Friend
#----------------------------------------------------

#-----------------------------------------------------
# Class
#-------------------------------------------------------
from Friend_Albert_Final_Classes import BikeRental as Shop
from Friend_Albert_Final_Classes import Customer as Customer

#--------------------------------------------------------------------------
#1. Function Name: Validation_Bike_Number
#2. Function Description: Validation of the User input for bike numbers
#--------------------------------------------------------------------------
def Validation_Bike_Number(intNumber):
    try:
        intNumber = int(intNumber)
        if intNumber >= 0:
            global strFlag
            strFlag = True
        else:
            print('Please enter a whole number greater than or equal to zero.')
    except ValueError:
        print("Please enter a whole number.")
    return intNumber

#--------------------------------------------------------------------------
#1. Function Name: Validation_Navigation
#2. Function Description: Validation Navigation
#--------------------------------------------------------------------------
def Validation_Navigation(intNumber):
    try:
        intNumber = int(intNumber)
        if intNumber >= 1 and intNumber <= 5:
            global strFlag
            strFlag = True
        else:
            print("Please select one of the listed options.")
    except ValueError:
        print("Please select one of the listed options.")
    return intNumber

#--------------------------------------------------------------------------
#1. Function Name: Navigation
#2. Function Description: Navigation option driver code
#--------------------------------------------------------------------------
def Navigation (intNavigationSelect):
    global strFlag
    match intNavigationSelect:
        case 1:
            New_Customer()
            strFlag = True
        case 2:
            Checkout()
            strFlag = True
        case 3:
            objShop.displaystock()
            strFlag = True
        case 4:
            objShop.endOfDay()
            strFlag = True

#--------------------------------------------------------------------------------------------------------------------------------------
#1. Function Name: User_New_Request
#2. Function Description: Validation to see if user wants to make a new selection, if so does the request, if not deletes the customer.
#----------------------------------------------------------------------------------------------------------------------------------
def User_New_Request (strRequestNew, customer):
    strFlag = False
    if strRequestNew.lower() == "y":
        while strFlag == False:
            while strFlag == False:
               strFlag = User_RequestBike_Type(customer)
            strFlag = False
            while strFlag == False:
                strFlag = User_RequestBike_Number(customer)
        return 1
    elif strRequestNew.lower() == 'n':
        print("Sorry we could not do business with you.")
        return 2
    elif strRequestNew.lower() != "y" or "n":
        print("Please select one of the two options.")
        return 0
#--------------------------------------------------------------------------
#1. Function Name: User_RequestBike_Type
#2. Function Description: modulize the call for customer request of a bike
#--------------------------------------------------------------------------
def User_RequestBike_Type(customer):
    intReturn = -1
    strFlag = False
    while intReturn == -1:
        intReturn = customer.requestBikeType()
    else:
        strFlag = True
        return strFlag


#--------------------------------------------------------------------------
#1. Function Name: User_RequestBike_Number
#2. Function Description: modulize the call for customer request of amount of bikes
#--------------------------------------------------------------------------
def User_RequestBike_Number(customer):
    intReturn = -1
    strFlag = False
    while intReturn == -1:
        intReturn = customer.requestBike()
    else:
        strFlag = True
        return strFlag

#--------------------------------------------------------------------------
#1. Function Name: Checkout
#2. Function Description: allowing for customer to check out
#--------------------------------------------------------------------------
def Checkout():
    global strFlag
    strFlag = False
    global Customer_list

    while strFlag == False:
       intReturn = Customer.Customer_Checkout()
       if intReturn == -1:
           strRequest = input("Would you like to try again? Y/N: ")
           if strRequest.lower() == 'y':
               intReturn = Customer.Customer_Checkout()
           elif strRequest.lower() == 'n':
               print("Please see an associate for help returning your bike")
               intReturn = 1
               strFlag = True
           elif strRequest.lower() != "y" or "n":
               print("Please enter only (Y/N).")
       else:
           customer = Customer_list[intReturn]
           request = customer.returnBike()
           objShop.returnBike(request)
           strFlag = True

#--------------------------------------------------------------------------
#1. Function Name: New_Customer
#2. Function Description: New_Customer option driver code
#--------------------------------------------------------------------------
def New_Customer():
    global intCustomerCount
    global Customer_list
    global Customer_info
    strFlag = False
    intReturn = -1
    strRequestNew = 0
    
    #sets up new object and gathers information
    customer = 'objCustomer%s' % intCustomerCount
    Customer_list.append(customer)
    Customer_list[intCustomerCount] = Customer()
    customer = Customer_list[intCustomerCount]
    customer.customerInfo()
    Customer_info.append(customer.info)

    while strFlag == False:
        while strFlag == False:
            while intReturn == -1:
                intReturn = customer.requestBasistype()
            else:
                strFlag = True

        strFlag = False
        
        while strFlag == False:
            customer.rentTime()
            strFlag = True

        strFlag = False

        while strFlag == False:
            strFlag = User_RequestBike_Type(customer)

        strFlag = False

        while strFlag == False:
            strFlag = User_RequestBike_Number(customer)

        strFlag = False

        while strFlag == False:
            intReturn = customer.couponCode()
            if intReturn == 1:
                strFlag = True

        strFlag = False

        while strFlag == False:
            match customer.rentalBasis:
                case 1:
                    intReturn = objShop.rentBikeOnHourlyBasis(customer.bikes, customer.biketype, customer.rentalTimeInput, intCustomerCount)
                case 2:
                    intReturn = objShop.rentBikeOnDailyBasis(customer.bikes, customer.biketype, customer.rentalTimeInput, intCustomerCount)
                case 3:
                    intReturn = objShop.rentBikeOnWeeklyBasis(customer.bikes, customer.biketype, customer.rentalTimeInput, intCustomerCount)
            if intReturn == None:
                strRequestNew = 0 
                print("We are sorry that we didnt have the requested bike type.")
                print(objShop.displaystock())
                while strRequestNew == 0:
                    strRequestNew = input("Would you like to request a differnt bike type and number of bikes? Y/N: ")
                    strRequestNew = User_New_Request(strRequestNew, customer)
                    if strRequestNew == 2:
                        del Customer_list[intCustomerCount]
                        del Customer_info[intCustomerCount]
                        Customer.removeCustomer()
                        strFlag = True;

            else:
                strFlag = True
                intCustomerCount += 1

    
#---------------------------------------------
# Setting up Stock for the shop
#---------------------------------------------
#--------------------------------------------------------------------------
# Declare Variables
#--------------------------------------------------------------------------
intMountain = 0
intRoad = 0
intTouring= 0
intCustomerCount = 0
Customer_list = []
Customer_info = []
strFlag = False

while strFlag == False:
    while strFlag == False:
        intMountain = input("How many mountain bikes do you have in stock? ")
        intMountain = Validation_Bike_Number(intMountain)

    strFlag = False

    while strFlag == False:
        intRoad = input("How many road bikes do you have in stock? ")
        intRoad = Validation_Bike_Number(intRoad)

    strFlag = False

    while strFlag == False:
        intTouring = input("How many touring bikes do you have in stock? ")
        intTouring = Validation_Bike_Number(intTouring)

objShop = Shop(intMountain, intRoad, intTouring)



#-----------------------------------------------------------------------------
# Main Navigation for the shop
#-----------------------------------------------------------------------------
#--------------------------------------------------------------------------
# Declare Variables
#--------------------------------------------------------------------------
intNavigationSelect = 0
strFlag = False

while strFlag == False:
    while strFlag == False:
        print('--------------------------------')
        print('Navigation Selection Options:')
        print('New Customer Rental: Select 1')
        print('Rental Return: Select 2')
        print('Show inventory: Select 3')
        print('End of day: Select 4')
        print('Close Program: Select 5')
        print('--------------------------------')
        intNavigationSelect = input("Plese select an option: ")
        print('--------------------------------')
        intNavigationSelect = Validation_Navigation(intNavigationSelect)

    strFlag = False

    if intNavigationSelect == 5:
        exit()

    while strFlag == False:
        Navigation(intNavigationSelect)

    strFlag = False
