'''                 Bin2Dec

User can enter up to 8 binary digits in one input field:                     done
User must be notified if anything other than a 0 or 1 was entered:           done
User views the results in a single output field containing the decimal
    (base 10) equivalent of the binary number that was entered:              done
User can enter a variable number of binary digits:                          to do

Currently this program accepts correctly the decimals between 00000000 and 11111111
Need to improve by filling the string in case of lesser characters(i.e. 1011)
Need to implement a function to make the calculation(or character verification)
Need to increment the use of fractions and rationals(i.e. 1011.1000)
'''

def main():
    while True: # Using a lot of whiles just to loop trough the exceptions
        binnumber = input("Type a Binary number to convert to Decimal or type 9 to exit: ")
        if binnumber == "9":# A exit option
            break
        while len(binnumber) >= 9: # Working with 8 decimal numbers
            print("You can only add up to 8 digits!")
            binnumber = input("Type again or type 9 to exit: ")
        if binnumber == "9": # Another exit
            break
        result = 0 # The program cycles trough the string input, using a counter and the 8 binary values aside the string
        twopower = [128, 64, 32, 16, 8, 4, 2, 1]
        count = 0 # A counter for the list index
        for c in binnumber:
            if c == "1":
                result += twopower[int(count)]
            elif c == "0":
                pass
            else:
                print("You can add only 0 and 1 digits!")
                break
            count += 1
        print("The decimal form of {} is {}".format(binnumber, result))

if __name__ == '__main__':
    main()