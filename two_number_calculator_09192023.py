#MAKING A SIMPLE TWO NUMBER CALCULATOR
#Reference: https://www.programiz.com/python-programming/examples/calculator
#09/18/2023-09/19/2023
class Calculator:
    def main():
        #prompting user input with text 
        print('\033[1m'+"TWO-NUMBER CALCULATOR"+'\033[0m') #bolding, need a beginning and end (different codes) 
        print("Enter 'Q' to quit")
        print("Enter your values below")

        while True: #for overall calculator: this keeps repeating the calculator prompts untl the user decides to quit
            #First input
            while True: #for evaluation of first input
                num1 = "placeholder" #ended up having to put this variable here as str so that the if statement later on can access the value. Could not keep it outside
                # of the while loop because when running calculations a second time and inputting a random string, the 
                #calculator would not be able to convert it into a float, so num1 will remain the same float as the last calculation 
                #and push the file into the next method despite recognising that it was not a valid input. Defining this variable
                #here as a string helps reset the value everytime this loop happens.
                val1=input("First Number: ").replace(",","") #defining the input once + getting rid of commas
                try: #here, putting a method that we want to execute
                    num1=float(val1) 
                except ValueError: #here, we put the expected error message and how to respond to it
                    if val1 == "Q":
                        break
                    else:
                        print("Put in a number bruh")
                if isinstance(num1, float):#breaks out of loop when proper input is given
                    break
            if val1 == "Q": #closes the calculator if user decides to quit
                print("You've exited the calculator.")
                break

            #Second input
            while True: #for evaluation of second input
                num2 = "p"
                val2=input("Second Number: ").replace(",","") #defining the input once + getting rid of commas
                try: #here, putting a method that we want to execute
                    num2=float(val2) 
                except ValueError: #here, we put the expected error message and how to respond to it
                    if val2 == "Q":
                        break
                    else:
                        print("Put in a number bruh :/")
                if isinstance(num2, float): #quitting the while loop once a number is properly entered
                    break
            if val2 == "Q": #closes the calculator if user decides to quit
                print("You've exited the calculator.")
                break
            
            print("Your 4 operations are: 'add', 'sub', 'div', and 'mul'")

            #Operation input
            while True:
                operation = input("Operation: ")
                if operation == "add": #basically test cases for each operation
                    print("Answer: " + str(num1+num2))
                    break
                elif operation == "sub":
                    print("Answer: " + str(num1-num2))
                    break
                elif operation == "mul":
                    print("Answer: " + str(num1*num2))
                    break
                elif operation == "div":
                    try: #forgot to add this, thanks Dill
                        num1/num2
                        print("Answer: " + str(num1/num2))
                    except ZeroDivisionError:
                        print("Can't divide by zero man")
                    break
                elif operation == "Q":
                    break
                else:
                    print("ERROR: Enter 'add', 'sub', 'mul', or 'div' for the operation")
            if operation == "Q": #quitting function
                print("You've exited the calculator.")
                break

            #prompt for another calculation?
            while True: 
                decision = input("Would you like to do another calculation? Y/N: ")
                if decision == 'N' or decision == 'n': #breaking out if no
                    print("Peace out")
                    break
                elif decision == 'Y' or decision == 'y': #breaking out if yes
                    break
                else:
                    print("huh") #visible confusion
            if decision == "N" or decision == 'n': #terminating file if answer was no
                break
    
    if __name__ == "__main__":
        main()

        

        
            
                
            
