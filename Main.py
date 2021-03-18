# Sydney Keller
# An integration of everthing I have learned about programing
# cited sources : https://www.w3schools.com/python/python_operators.asp
# cited sources: https://sites.google.com/site/profvanselow/programming/languages/python/variables-data-types-expressions-operators?authuser=0
# cited sources: https://www.w3schools.com/python/python_conditions.asp
#cited sources: https://www.studytonight.com/post/the-sep-and-end-parameters-in-python-print-statement
print("Hello and Welcome to my Project!")
Program_start = True
while Program_start:
    print("Enter the choice for what you would like to do")
    print("1. Test Score calculator")
    print("2. Wage Calculator")
    print("3. Fun with Numbers")
    print("4. Compound words")
    print("5. Your Favorites")
    print("6. Quit")
    activity_choice = int(input())
    if activity_choice == 1 :
        print("Calculate the Percent score on a test")
        #number of questions in total has a varible of num_questions
        #varible is a name for loaction in memory 
        num_questions = int(input("Enter amount of questions on the test :"))
        #number of questions answered correct has a varible of num_answer
        num_answer = int(input("Enter amount of questions you got correct :"))
        #score is equal to num_answer divied by num_questions then multiplied by 100
        score = (num_answer / num_questions * 100)
        print("You got a",format(score,'.0f'),"%")

    elif activity_choice == 2:
        print("Lets calculate how much you would get paid at an hourly job per week")
        hours = float(input("How many hours do you work this week? :"))
        pay = float(input("What is you pay per hour? :"))
        # multiply hours by pay to get total pay per week
        pay_week = (hours * pay)
        #end takes away new line and sep takes away the spaces
        print("You get paied $",format(pay_week,'.2f'),sep='',end='')
        print(" this week!")

    elif activity_choice == 3:
        print("Lets do some basic math yay!")
        #x_value is number that is going to be raised to a power
        x_value = int(input("Insert a number you want to be raised to a power: "))
        #input for exponential equation varible = power
        power = int(input("Insert a number to be the power: "))
        # ** does the exponential equation
        print(x_value ** power)
        print("Now time for some addition and subtraction!")
        #num1 is the varible we are going to add to.
        num1 = int(input("Insert a two digit number: "))
        #num2 is the varible we also are going to add.
        num2 = int(input("Insert a one digit number: "))
        print("What happens if we add your two numbers?")
        # to add we use +
        print(num1 + num2)
        print("What happens if we subtract your two numbers?")
        # use - to subtract
        print(num1 - num2)
        print("Lets divide and find the remainer between them as well!")
        # % helps us find the remainer between two numbers or the Modulus
        print(num1 % num2)
        print("We are almost done with our super fun math journey!")
        # crazy_number1 is a varible in number format however the user wants
        #crazy_number2 is a varible in number format however the user wants
        crazy_number1 = float(input("Enter any number you desire: "))
        crazy_number2 = float(input("Enter any number you desire again: "))
        print(" We are going to do some floor division which divides to one integer.")
        # use // to complete floor division process
        print(crazy_number1 // crazy_number2)

    elif activity_choice == 4:
        print("We are going to make some compound words!")
        # word_choice is varible user choses from list
        word_choice = input("Choose a word from the list: butter, base, rain, or note? ")
        # using + can add words together through a string
        # == means equals
        if word_choice == "butter":
            print("butter" + "fly")
        if word_choice == "base":
            print("base" + "ball")
        if word_choice == "rain":
            print("rain" + "bow")
        if word_choice == "note":
            print("note" + "book")
        print("How fun was that?!")

    elif activity_choice == 5:
        print("Lets have some fun with your favorite word and number!")
        fav_word = input("Type your favorite word here: ")
        fav_number = int(input("Type your  favorite whole number here: "))
        print("Ready for a suprise?")
        # using * can make a word repeat a number of times
        print(fav_word * fav_number)

    elif activity_choice == 6:
        Program_start = False
        print("Exiting.")
    else:
        print("try again, error")
                


