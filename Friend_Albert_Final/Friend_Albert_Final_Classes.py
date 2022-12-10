import datetime
from datetime import datetime, timedelta

class BikeRental:
    dlbRunningDailyTotal = 0
    intRentedBikes = 0
    intRentedRoadBikes = 0
    intRentedTouringBikes = 0
    intRentedMountainBikes = 0
    def __init__(self, mountain = 0, road = 0, touring = 0, stock = 0):
        """
        Our constructor class that instantiates bike rental shop.
        """
        self.mountain = mountain
        self.touring = touring
        self.road = road
        self.stock = mountain + road + touring
        self.rentedBikes = 0
    def displaystock(self):
        """
        Displays the bikes currently available for rent in the shop.
        """
        print("In total we currently have {} bikes available to rent. With {} mountain bikes, {} road bikes, and {} touring bikes to rent".format(self.stock, self.mountain, self.road, self.touring))
        return self.stock

    def dispalyrentedbikes(self):
        """"
        Displays the amount of bikes rented out
        """

    def rentBikeOnHourlyBasis(self, n, bikeType, rentalTimeInput, idNumber):
        """
        Rents a bike on hourly basis to a customer.
        """
        # reject invalid input 
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        # do not rent bike is stock is less than requested bikes
        if n > 0:
            match bikeType:
                case 'mountain':
                    if n > self.mountain:
                        print("Sorry! We have currently {} mountain bikes available to rent.".format(self.mountain))
                        return None
                    else:
                        self.mountain -= n
                case 'road':
                    if n > self.road:
                        print("Sorry! We have currently {} road bikes available to rent.".format(self.road))
                        return None
                    else:
                        self.road -= n
                case 'touring':
                    if n > self.touring:
                        print("Sorry! We have currently {} touring bikes available to rent.".format(self.touring))
                        return None
                    else:
                        self.touring -= n
        # rent the bikes        
            now = datetime.now()
            print("You have rented a {} bike(s) on hourly basis today at {} for {} hour(s).".format(n, now.time(), rentalTimeInput))
            print("You will be charged $5 for each hour per bike.")
            print("Your ID number is: {}. Please remeber this for checkout.".format(idNumber))
            print("We hope that you enjoy our service.")
            self.stock -= n
            self.rentedBikes += n
            return now      
     
    def rentBikeOnDailyBasis(self, n, bikeType, rentalTimeInput, idNumber):
        """
        Rents a bike on daily basis to a customer.
        """
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        # do not rent bike is stock is less than requested bikes
        if n > 0:
            match bikeType:
                case 'mountain':
                    if n > self.mountain:
                        print("Sorry! We have currently {} mountain bikes available to rent.".format(self.mountain))
                        return None
                    else:
                        self.mountain -= n
                case 'road':
                    if n > self.road:
                        print("Sorry! We have currently {} road bikes available to rent.".format(self.road))
                        return None
                    else:
                        self.road -= n
                case 'touring':
                    if n > self.touring:
                        print("Sorry! We have currently {} touring bikes available to rent.".format(self.touring))
                        return None
                    else:
                        self.touring -= n
            now = datetime.now()                      
            print("You have rented {} bike(s) on daily basis today at {} for {} day(s).".format(n, now.time(), rentalTimeInput))
            print("You will be charged $20 for each day per bike.")
            print("Your ID number is: {}. Please remeber this for checkout.".format(idNumber))
            print("We hope that you enjoy our service.")
            self.stock -= n
            self.rentedBikes += n
            return now
        
    def rentBikeOnWeeklyBasis(self, n, bikeType, rentalTimeInput, idNumber):
        """
        Rents a bike on weekly basis to a customer.
        """
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        if n > 0:
            match bikeType:
                case 'mountain':
                    if n > self.mountain:
                        print("Sorry! We have currently {} mountain bikes available to rent.".format(self.mountain))
                        return None
                    else:
                        self.mountain -= n
                case 'road':
                    if n > self.road:
                        print("Sorry! We have currently {} road bikes available to rent.".format(self.road))
                        return None
                    else:
                        self.road -= n
                case 'touring':
                    if n > self.touring:
                        print("Sorry! We have currently {} touring bikes available to rent.".format(self.touring))
                        return None
                    else:
                        self.touring -= n
            now = datetime.now()
            print("You have rented {} bike(s) on weekly basis today at {} for {} week(s).".format(n, now.time(), rentalTimeInput))
            print("You will be charged $60 for each week per bike.")
            print("Your ID number is: {}. Please remeber this for checkout.".format(idNumber))
            print("We hope that you enjoy our service.")
            self.stock -= n
            self.rentedBikes += n
            return now
    
    
    def returnBike(self, request):
        """
        1. Accept a rented bike from a customer
        2. Replensihes the inventory
        3. Return a bill
        """
       
        # extract the tuple and initiate bill
        rentalTime, rentalBasis, numOfBikes, bikeType, couponCode = request
        bill = 0
        # issue a bill only if all three parameters are not null!
        if rentalTime and rentalBasis and numOfBikes and bikeType:
            BikeRental.intRentedBikes += numOfBikes
            self.stock += numOfBikes
            self.rentedBikes -= numOfBikes
            if bikeType == 'mountain':
                self.mountain += numOfBikes
                BikeRental.intRentedMountainBikes += numOfBikes
            elif bikeType == 'touring':
                self.touring += numOfBikes
                BikeRental.intRentedTouringBikes += numOfBikes
            else:
                self.road += numOfBikes
                BikeRental.intRentedRoadBikes += numOfBikes
            now = datetime.now()
            rentalPeriod = now - rentalTime
            # hourly bill calculation
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * numOfBikes
                
            # daily bill calculation
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20 * numOfBikes
                
            # weekly bill calculation
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 60 * numOfBikes
            
            # discount calculation
            if (3 <= numOfBikes <= 5):
                print("You are eligible for Family rental promotion of 30% discount")
                bill = bill * 0.7
            if couponCode == 'Y':
                print("You are eligible for a discount coupon of 10% off")
                bill = bill * 0.9
            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            BikeRental.dlbRunningDailyTotal += bill

            return bill
        
        else:
            print("Are you sure you rented a bike with us?")
            return None

    def endOfDay (self):
        # ends the day, displaying the amount made, the bikes rented and the bikes still out for rent.
        print("The total revenue for the day was ${}.".format(BikeRental.dlbRunningDailyTotal))
        print("We have completed rentals on {} bikes in total today. With {} being mountain bikes, {} being touring bikes, and {} being road bikes".format(BikeRental.intRentedBikes, BikeRental.intRentedMountainBikes, BikeRental.intRentedTouringBikes, BikeRental.intRentedRoadBikes))
        print("We still have {} bikes out for rent.".format(self.rentedBikes))
        BikeRental.dlbRunningDailyTotal = 0
        BikeRental.intRentedBikes = 0
        BikeRental.intRentedRoadBikes = 0
        BikeRental.intRentedMountainBikes = 0
        BikeRental.intRentedTouringBikes = 0

class Customer:
    intCustomerCount = 0
    Customer_list = []
    def __init__(self):
        """
        Our constructor method which instantiates various customer objects.
        """
        
        self.bikes = 0
        self.biketype = ''
        self.rentalBasis = 0
        self.rentalTime = 0
        self.rentalTimeInput = 0
        self.bill = 0
        self.CustomerID = 0
        self.info = ()
        self.coupon = ''
        strFlag = False

    def customerInfo(self):
        """
        Gathers customer information and gives them a ID number
        """
        name = input("Please enter your name: ")
        CustomerID = Customer.intCustomerCount
        self.info = (name, CustomerID)
        Customer.Customer_list.append(self.info)
        print("Your customer id is {}. Please remeber this for checkout.".format(CustomerID))
        Customer.intCustomerCount += 1 
        return self.info

    def requestBike(self):
        """
        Takes a request from the customer for the number of bikes.
        """
        bikes = input("How many bikes would you like to rent?")
        # implement logic for invalid input
        try:
            bikes = int(bikes)
        except ValueError:
            print("That's not a positive integer!")
            return -1
        if bikes < 1:
            print("Invalid input. Number of bikes should be greater than zero!")
            return -1
        else:
            self.bikes = bikes
        return self.bikes

    def requestBikeType(self):
        """
        seeing what type of bike the customer would like
        """
        biketype = input("Would you like mountain, road, or touring bikes?")
        # implement logic for checking for bike type
        try:
            if biketype.isdigit() == False:
                try:
                    float(biketype)
                    print("Please enter the type of bike you would like. Options are mountain, road, or touring.")
                    return -1
                except ValueError:
                    biketype = biketype.lower()
        except ValueError:
            print("Please enter the type of bike you would like. Options are mountain, road, or touring.")
            return -1 
        if biketype == str(biketype):
            match biketype.lower():
                case 'mountain'| 'road' | 'touring':
                    self.biketype = biketype.lower()
                    return self.biketype
                case _:
                    print("Please enter the type of bike you would like. Options are mountain, road, or touring.")
                    return -1 

    def requestBasistype(self):
        """
        Checking what type of rental customer would like
        """

        strType = input("Please enter what type of rental you would like (Hourly: $5 per, Daily: $20 per, Weekly: $60 per): ")

        try:
            if strType.isdigit() == False:
                try:
                    float(strType)
                    print("Please enter one of the above options.")
                    return -1
                except ValueError:
                    strType = strType.lower()
        except ValueError:
            print("Please enter one of the above options.")
            return -1
        if strType == str(strType):
            match strType:
                case 'hourly':
                    self.rentalBasis = 1
                    return self.rentalBasis
                case 'daily':
                    self.rentalBasis = 2
                    return self.rentalBasis
                case 'weekly':
                    self.rentalBasis = 3
                    return self.rentalBasis
                case _:
                    print("Please enter one of the above options.")
                    return -1

    def rentTime(self):
        """
        Allows customer to set how long they would like to rent
        """
        Customer.strFlag = False
        while Customer.strFlag == False:
            match self.rentalBasis:
                case 1:
                    rentalTime = input('How many hours would you like to rent the bike(s) for? ')
                    rentalTime = self.validationOfTime(rentalTime)
                    if rentalTime != -1:
                        self.rentalTime = datetime.now() + timedelta(hours=-self.rentalTime)
                        self.rentalTimeInput = datetime.now()-self.rentalTime
                case 2:
                    rentalTime = input('How many days would you like to rent the bike(s) for? ')
                    rentalTime = self.validationOfTime(rentalTime)
                    if rentalTime != -1:
                        self.rentalTime = datetime.now() + timedelta(days=-self.rentalTime)
                        self.rentalTimeInput = datetime.now()-self.rentalTime
                case 3:
                    rentalTime = input('How many weeks would you like to rent the bike(s) for? ')
                    self.validationOfTime(rentalTime)
                    if rentalTime != -1:
                        self.rentalTime = datetime.now() + timedelta(weeks=-self.rentalTime)
                        self.rentalTimeInput = datetime.now()-self.rentalTime
   
        return self.rentalTime

    def validationOfTime(self, rentalTime):
        """
        Validation of the rental time
        """

        try:
            if not rentalTime.isdigit() or type(rentalTime) == float:
                print("Please input a whole number greater than zero.")
                return -1
            else:
                self.rentalTime = int(rentalTime)
                Customer.strFlag = True
                return self.rentalTime
        except TypeError:
            print("Please input a whole number greater than zero.")


    def couponCode (self):
        Customer.strFlag = False
        strAnswer = input('Do you have a coupon code? (Y/N): ')
        try:
            strAnswer = strAnswer.lower()
            if strAnswer != 'n' and strAnswer != 'y':
                print('Please enter Y/N only.')
            elif strAnswer == 'n':
                self.couponCode = 'N'
                return 1
            else:
                while Customer.strFlag == False:
                        strCouponCode = input("Please enter your coupon code: ")
                        strCouponCode = self.validationCoupon(strCouponCode)
                        if strCouponCode == -1:
                            strAnswer = input('Would like to enter the code again? (Y/N): ')
                            try:
                                strAnswer = strAnswer.lower()
                                if strAnswer != 'y' and strAnswer !=  'n':
                                    print('Please enter Y/N only.')
                                elif strAnswer == 'n':
                                    self.couponCode = 'N'
                                    Customer.strFlag = True
                                    return 1
                            except ValueError:
                                print('Please enter a Y/N only.')
                        else:
                            Customer.strFlag = False
                            return 1
        except ValueError:
            print('Please enter a Y/N only.')

    def validationCoupon (self, strCode):
        if strCode[len(strCode)-3:] != 'BBP':
            print('Invaild coupon code. Please check the code, and enter exactly as it is shown')
            return -1
        else:
            print('Thank you! Code accepted.')
            self.couponCode = 'Y'
            return 1

    def removeCustomer():
        """
        removes customer from list and subtracts 1 from customer count if customer does not finish renting
        """
        Customer.intCustomerCount -= 1
        del Customer.Customer_list[Customer.intCustomerCount]
    def Customer_Checkout():
        """
        allows information to be gathered for customer checkout
        """
        info = input("Please the ID number given to you when you rented: ")
        try:
            info = int(info)
        except ValueError:
            print("Please enter a whole number as your ID.")
            return -1

        try: 
            info = Customer.Customer_list[info]
            ID = int(info[1])
        except IndexError:
            print("Please check you Id number, as it does not appear in our system.")
            return -1 
        
        print('Hello {},'.format(info[0]))
        del Customer.Customer_list[ID]
        return ID

    def returnBike(self):
        """
        Allows customers to return their bikes to the rental shop.
        """
        if self.rentalBasis and self.rentalTime and self.bikes and self.biketype and self.couponCode:
            return self.rentalTime, self.rentalBasis, self.bikes, self.biketype, self.couponCode
        else:
            return 0,0,0,0,0
        


#shop1 = BikeRental(30)
#shop2 = BikeRental(30)

##shop1.displaystock()

##shop1.rentBikeOnHourlyBasis(31)

##shop2.rentBikeOnDailyBasis(-1)

##shop2.rentBikeOnWeeklyBasis(11)



## ##Create Customers

#customer1 = Customer()
#customer2 = Customer()
#customer3 = Customer()
#customer4 = Customer()

## Set up rental basis
#customer1.rentalBasis = 1 # hourly
#customer2.rentalBasis = 1 # hourly
#customer3.rentalBasis = 2 # daily
#customer4.rentalBasis = 2 # daily

## determine number of bikes
#customer1.bikes = 1
#customer2.bikes = 5 # eligible for family discount 30%
#customer3.bikes = 2
#customer4.bikes = 0


#customer1.biketype = 'mountain'
#customer2.biketype = 'mountain' # eligible for family discount 30%
#customer3.biketype = 'mountain'
#customer4.biketype = 'mountain'
## detrmine rental time
#customer1.rentalTime = datetime.now() + timedelta(hours=-4)
#print(type(customer1.rentalTime))
#customer2.rentalTime = datetime.now() + timedelta(hours=-23)
#customer3.rentalTime = datetime.now() + timedelta(days=-4)
#customer4.rentalTime = datetime.now() + timedelta(days=-14)

#print(customer1.rentalTime)
## create request to return the bike
#request1 = customer1.returnBike()
#request2 = customer2.returnBike()
#request3 = customer3.returnBike()
#request4 = customer4.returnBike()

## return the bike to shop and get a bill
#shop1.returnBike(request1) 
#shop1.returnBike(request2) 
#shop1.returnBike(request3) 
#shop1.returnBike(request4) 

