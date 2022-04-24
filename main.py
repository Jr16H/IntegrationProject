# Name: Jonathan Howard
# Description: This code is a quiz
# Sources:()
Name = input("Please Insert Name Here:")
# I am using if and else because they are better to use when you have
# if as the exact answer and anything else will be wrong.
print("Hello,", Name, "this is a quiz to test your basic knowledge?")
print("First we will start out with some basic math problems.")
mp_1 = int(input("#1.What is 1000 + 200 ?"))
if mp_1 == 1000 + 200:
    print("Good Job!")
else:
    print("Try again next time!")
mp_2 = int(input("#2.What is 350-20?"))
if mp_2 == 350 - 20:
    print("Bingo!!!")
else:
    print("Not Quite.")
mp_3 = int(input("#3.What is 10*13?"))
if mp_3 == 10 * 13:
    print("Nice!!")
else:
    print("Better luck next time!")
mp_4 = int(input("#4.What is 2**5?"))
if mp_4 == 2 ** 5:
    print("Your doing great!")
else:
    print("Not the answer we're looking for.")
mp_5 = int(input("#5.What is 15/3?"))
if mp_5 == 15 / 3:
    print("Way to go!")
else:
    print("Wrong!")
mp_6 = int(input("#6.What is 15%7 ?"))
if mp_6 == 15 % 7:
    print("Well-done!!")
else:
    print("Incorrect")
mp_7 = int(input("#7.What is 85//9?"))
if mp_7 == 85 // 9:
    print("Your On a roll!!")
else:
    print("Try again")
# I designated true or false as variables because it will allow for the user to
# input true or false themselves and I am using this the same way for the if
# and else statements.
# I also had the computer run the problem if you got it wrong in order to show
# you what it looks like.
print(Name, "you're doing great the next portion of the quiz will be true or " 
            "false.")
word_true = 'true' or 'True'
word_false = 'false' or 'False'
tf_p1 = input("#8. Would the line of code" "StudyHarder!*10" "return the code "
              "StudyHarder! 10 times?")
if tf_p1 == word_true:
    print("You have big brain!")
else:
    print("StudyHarder!" * 10)
print("This is what the code would return.")
tf_p2 = input("#9. Would the line of code" "Happy" + "Birthday!" "return the "
                                                     "code Happy + Birthday?")
if tf_p1 == word_false:
    print("You are doing great!")
else:
    print("Happy" + "Birthday")
print("This is what the outcome should be and why you got it wrong")
tf_p3 = input("#10. Would the line of code 10!=10 come back as true or false?")
if tf_p3 == word_false:
    print("You have big brain!")
else:
    print(10 != 10)
    print("This is what the outcome should be and why you got it wrong is "
          "because the != is when not equal")
tf_p4 = input("#11. Would the line of code 10>=1 come back as true or false?")
if tf_p4 == word_false:
    print("You have big brain!")
else:
    print(10 >= 1)
    print("This is what the outcome should be and why you got it wrong is "
          "because the >= is greater than or equal too")
print(
    "The next part of the quiz is going to be is typing a number that is going"
    "to make the statement true, if you get a false then it is incorrect!!!!")
print("#12. What is a number that makes this statement true: numPeople>20 and "
      "numPeople<45 ?")
numPeople = int(input("number:"))
print(numPeople > 20 and numPeople < 45)
print("#13. What is a number that makes this statement true: numDogs<30 or "
      "numDogs>45 ?")
numDogs = int(input("number:"))
print(numDogs < 30 or numDogs > 45)
print("#14. What is a number that makes this statement true: "
      "not(numberUmbrellas*5==100) ?")
numUmbrellas = int(input("number:"))
print(not (numUmbrellas * 5 == 100))
print("#15. Type a number that will make the following code print 5 numbers.")
print("while number <= 5:")
print("print(number)")
print("number=number + 1")
number = int(input("Input number here:"))
while number <= 5:
    print(number)
    number += 1
if number == range(1, 5):
    print("Nice Work!!!")
else:
    print("Better Luck Next Time")
while True:
    try:
        m_7 = str(input("#16. 20 and 30 are not equal, would you use =! to "
                        "code that?"))
        if m_7 != word_false:
            print("great job braniac! \n")
            break
        else:
            print("its okay in 5 more questions I will show you something "
                  "cool, hold tight")
    except ValueError:
        print("true or false")
# allowing the user to know these are math questions
print("The following will be math questions again, integers only")
while True:
    try:
        m_8 = int(input("#17. What number is <10 and >8"))
        if m_8 == m_8 < 10 and m_8 > 8:
            print("correct")
            break
        else:
            print('not so good')
            break
    except ValueError:
        print('Make sure it is an a whole integer')
while True:
    try:
        m_9 = int(input('#18. type 10'))
# utilizing while and not to simplify code and make it a little smoother
        if m_9 != 10:
            print("yikes")
        else:
            print("you cannot read I guess")
    except ValueError:
        print("number please")

while True:
    try:
        m_10 = int(input("#19. what is a number more than 10 OR less than 5"))
        if m_10 == m_10 > 10 or m_10 < 5:
            print("you got some math in yah")
        else:
            print("better luck next time")
    except ValueError:
        print("whole number please")
while True:
    try:
        m_11 = int(input("#20. what number plus another number does not equals"
                         " the first number"))
        total = 0
        for x in range(2):
            number = int(input("Enter a number: "))
            total += number
        if m_11 == total:
            print("nice")
            break
        else:
            print("not so nice")
            break
    except ValueError:
        print("whole number please")
while True:
    try:
        m_12 = int(input("#21.if i gave you x= range (3,6) how many lines"
                         " would the output have"))
        x = range(1, 2)
        for n in x:
            if m_12 == 3:
                print('mice are nice')
                break
            elif m_12 != 3:
                print("mice not nice")
                break
    except ValueError:
        print("number please")
print("you finished this quiz")
# utilizing def to define a function


def endofquiz( ):
    """
This ends the quiz saying bye
    """
    bye_coder = "Bye dear coder, wow I really had to try for this quiz so " \
                "please appreciate"
    print(bye_coder)
# function is returning parameter


endofquiz()
