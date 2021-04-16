"""
This program is a general combination of all the skills I have learned
from the programming exercises and coding we have done
"""

__author__ = "Dirk Johnson"

print("Hello there, \nWelcome to a program that aims to show off \neverything"
      " I have learned in this class so far.")
print(" \nPress Enter when you are ready to continue at all stops"
      " during the program.")
input()  # This is used to pace the program down so that all of the code
# isn't shown at once
print("To start off I need some basic information about you")
mothers_maiden_name = (input("What is your mother's maiden name?:"))
current_pets_name = (input("What was your current pet's name?:"))
print("Ok now that I can log into your bank account, we can ACTUALLY get"
      " started. \nI'm kidding of course I don't know how to do that...yet.")
input()
number_of_times_eaten_out = (input("How many times a week would you say"
                                   " you eat out?:"))
while True:
    # this while function tests the users input and makes sure it
    #  is an appropriate input
    try:  # I got help figuring out this loop from
        # https://stackoverflow.com/questions/23294658/
        # asking-the-user-for-input-until-they-give-a-valid-response this
        # code is used for every check of a valid response throughout the
        # program
        number_of_times_eaten_out = float(number_of_times_eaten_out)
    except ValueError:
        number_of_times_eaten_out = input("Invalid input. Please try again: ")
    else:
        break
while int(number_of_times_eaten_out) < 0:
    # this checks and makes sure the
    # user cant input a number less than or equal to -1 because
    # you cant go out a negative amount of times.
    number_of_times_eaten_out = input("Invalid input. please try again.")
    while True:
        try:
            number_of_times_eaten_out = float(number_of_times_eaten_out)
        except ValueError:
            number_of_times_eaten_out = input(
                "Invalid input. Please try again: ")
        else:
            break
average_cost_eating_out = (input(
    "Ok and on average how much would you say you spend each time you go "
    "out?:$"))
while True:
    try:
        average_cost_eating_out = float(average_cost_eating_out)
    except ValueError:
        average_cost_eating_out = input("Invalid input. Please try again: ")
    else:
        break
while average_cost_eating_out < 0:
    average_cost_eating_out = input("Invalid input. please try again: ")
    while True:
        try:
            average_cost_eating_out = float(average_cost_eating_out)
        except ValueError:
            average_cost_eating_out = input(
                "Invalid input. Please try again: ")
        else:
            break
while number_of_times_eaten_out > 0:
    while average_cost_eating_out <= 0:
        average_cost_eating_out = (input("Invalid input. Please try again: "))
        while True:
            try:
                average_cost_eating_out = float(average_cost_eating_out)
            except ValueError:
                average_cost_eating_out = input(
                    "Invalid input. Please try again: ")
            else:
                break
    break
    # this break allows the first while loop to terminate as soon as
    # the user enters a value that satisfies the second while loops condition
average_cost_for_year = int(
    (number_of_times_eaten_out * 52) * average_cost_eating_out)
# this takes the user input for number of times per week they eat out and
# scales it up to how many times they eat per year and then, multiplies
# it by the average cost per time eaten out.
print("So on average you spend about $" + format(average_cost_for_year, ".2f"),
      "eating out per year.")
# the + between $ and the average_cost_for_year makes it so the $ and
# number value are right next to each other instead of there being a space
input()
print("After seeing that number be higher than you likely thought it was, "
      "\nhow about we take out some of that frustration?")
angry_word = input("What do you say when your angry?: ")
times_said = (input("On a scale from 1 to 10 how angry are you right now: "))
while True:
    try:
        times_said = float(times_said)
    except ValueError:
        times_said = input("Invalid input. Please try again: ")
    else:
        break
while float(times_said) > 10 or float(times_said) < 1:
    # this makes sure the user stays between 1 and 10 for their input
    times_said = (input("Invalid input. Please try again: "))
    while True:
        try:
            times_said = float(times_said)
        except ValueError:
            times_said = input("Invalid input. Please try again: ")
        else:
            break
for x in range(round(float(times_said))):
    # this prints the users word the
    # number of times they input rounded to the nearest whole number for that
    # many number of columns and rows
    for y in range(round(float(times_said))):
        print(angry_word + " ", end=" ")
    print()
print("Feel better? \nGood, now we can continue right along.")
input()
name = input("I should have asked this earlier, but what is your name?: ")
age = (input("Also, how old are you?:"))
while True:
    try:
        age = float(age)
    except ValueError:
        age = input("Invalid input. Please try again: ")
    else:
        break


def time_worked_percentage(age, time_at_job):
    """
    this function takes the user inputs from the function below and inputs
    them into an equations that calculates the percentage of time the user
    has worked at their job in months
    :param age:
    :param time_at_job:
    :return: percentage_worked:
    """
    # this function calculates the
    # percentage the user has worked at their current job based on
    # their input values
    age_in_months = age * 12
    percentage_worked = float(
        format(((time_at_job / age_in_months) * 100), ".2""f"))
    return percentage_worked


def main(age):
    """
     this function takes the user inputs, checks to make sure they
     are appropriate, and passes the parameters onto the function that
     calculates the time worked at their job percentage
    """

    while age < 1:
        age = (input("Invalid input. Please try again: "))
        while True:
            try:
                age = float(age)
            except ValueError:
                age = input("Invalid input. Please try again: ")
            else:
                break
    time_at_job = (
        input("How many months have you worked at your current job?:"))
    while True:
        try:
            time_at_job = float(time_at_job)
        except ValueError:
            time_at_job = input("Invalid input. Please try again: ")
        else:
            break
    while time_at_job < 0:
        time_at_job = (input("Invalid input. Please try again: "))
        while True:
            try:
                time_at_job = float(time_at_job)
            except ValueError:
                time_at_job = input("Invalid input. Please try again: ")
            else:
                break
    while float(format(((time_at_job / (age * 12)) * 100), ".2""f")) > 100:
        time_at_job = (input("Invalid input. Please try again: "))
        while True:
            try:
                time_at_job = float(time_at_job)
            except ValueError:
                time_at_job = input("Invalid input. Please try again: ")
            else:
                break
    print("So ", name, end=', ')
    # I got help with figuring out how to use the end = argument thanks to
    # Professor Vanselow and
    # at https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
    print("you have worked about", time_worked_percentage(age, time_at_job),
          "% of your life so far at this job.")


main(age)

input()
print(
    "Now before I give you a quick math quiz, I need to make sure my code is"
    " calibrated correctly.")
user_number = (input(
    "Please input a number and I will tell you what kind of number it is: "))
while True:
    try:
        user_number = float(user_number)
    except ValueError:
        user_number = input("Invalid input. Please try again: ")
    else:
        break
if user_number > 0:
    print("The number you input was a positive number. It was", user_number)
elif user_number == 0:
    print("The number you input was zero.")
else:
    # this assumes that since the users input
    # wasn't positive or zero, that it must then be negative number
    print("The number input was a negative number. It was", user_number)
input()
print("One more calibration needed.")


def calibration_equation(first_number, second_number, third_number,
                         operator):
    """
    takes the inputs from the function below and adds them together and
    returns the final value
    :param operator:
    :param first_number:
    :param second_number:
    :param third_number:
    :return:
    """
    if operator == "+":
        answer = (first_number + second_number + third_number)
    else:
        answer = (first_number * second_number * third_number)
    return answer


correct_operators = ["+", "*"]


def main():
    """
    makes sure all three of the users inputs are valid
    """
    first_number = (input("Enter a number: "))
    while True:
        try:
            first_number = float(first_number)
        except ValueError:
            first_number = input("Invalid input. Please try again: ")
        else:
            break
    second_number = (input("Enter another number: "))
    while True:
        try:
            second_number = float(second_number)
        except ValueError:
            second_number = input("Invalid input. Please try again: ")
        else:
            break
    third_number = (input("Enter one more number: "))
    while True:
        try:
            third_number = float(third_number)
        except ValueError:
            third_number = input("Invalid input. Please try again: ")
        else:
            break
    operator = input("Now enter either \"+\" or \"*\":")
    while True:
        while operator not in correct_operators:
            operator = input("Invalid input. Please try again: ")
        break
    user_answer = 0
    if operator == "+":
        user_answer = input("Enter the solution by adding "
                            "all of the numbers you input:")
    if operator == "*":
        user_answer = input("Enter the solution by multiplying "
                            "all of the numbers you input:")
    while True:
        try:
            user_answer = float(user_answer)
        except ValueError:
            user_answer = input("Invalid input. Please try again: ")
        else:
            break
    print("Now we will see if your answer matches with what I got.")
    print(float(first_number), operator, float(second_number), operator,
          float(third_number), "=",
          format(calibration_equation(first_number, second_number,
                                      third_number, operator), ".2f"))
    if user_answer == calibration_equation(first_number, second_number,
                                           third_number,
                                           operator) and operator == "+":
        print("Good job adding those numbers up, I know it must've been"
              " very difficult")
    if user_answer != calibration_equation(first_number, second_number,
                                           third_number,
                                           operator) and operator == "+":
        print("You might want to check you adding skills next time")
    if user_answer == calibration_equation(first_number, second_number,
                                           third_number,
                                           operator) and operator == "*":
        print("Good job multiplying, I'm sure you were glad to have that "
              "calculator on your phone right about now")
    if user_answer != calibration_equation(first_number, second_number,
                                           third_number,
                                           operator) and operator == "*":
        print("You might want to recheck you multiplying skills on this one")


main()
input()
print("Now for a quick little math quiz")
print("If I were to tell you that the variables")
print("(x=3)" "(y=4)" "(z=5)", sep="  ")
# I also received help with the sep= argument from Professor
# Vanselow and https://www.geeksforgeeks.org/python-sep-parameter-print/?ref=rp
print("Could you solve the equation (x^3+(y/x))+(z^2-3x)")
print("with the answer rounded to the nearest whole number.")


def math_equation():
    """
    calculates to correct answer to the given math problem
    then returns the value
    :return:
    """
    number_one = 3
    number_two = 4
    number_three = 5
    solution = (pow(number_one, 3) + (number_two / number_one)) + \
               ((number_three ** 2) - number_one * 3)
    solution //= 1
    # this uses a shortcut operator the shortens the expression
    # solution = solution // 1
    return round(solution)
    # this rounds the value received from the equation to
    # the nearest whole number


def main():
    """
    checks to see if the user input is valid and matches the correct answer
    """
    user_solution = (input("Enter solution: "))
    while True:
        try:
            user_solution = float(user_solution)
        except ValueError:
            user_solution = input("Invalid input. Please try again: ")
        else:
            break
    while user_solution != math_equation():
        if user_solution == 43.8:
            user_solution = input(
                "Don't forget to round to the nearest whole number: ")
            while True:
                try:
                    user_solution = float(user_solution)
                except ValueError:
                    user_solution = input("Invalid input. Please try again: ")
                else:
                    break
        else:
            user_solution = (
                input("Your answer was incorrect. Please try again: "))
            while True:
                try:
                    user_solution = float(user_solution)
                except ValueError:
                    user_solution = input("Invalid input. Please try again: ")
                else:
                    break
    if float(user_solution) == math_equation():
        print("Congratulations on getting the answer correct!\nYour answer:",
              int(user_solution), "equals", math_equation())


main()
input()
print(
    "Now that you've passed my math test, its only fair that you get a prize"
    " right?")
animal_selection = input("Choose either Owl, Frog, Snowman, or Bunny: ")
acceptable_inputs = ["Owl", "owl", "Frog", "frog", "Snowman", "snowman",
                     "Bunny", "bunny"]
# I got help with the mechanics of a list and testing it against
# a while loop from
# https://stackoverflow.com/questions/55450907/while-loop-in-python-3-using-lists-and-if-statement-for-begginer
while True:
    # this test to see if the users input is inside of the list of acceptable
    # answers. if not then the user is asked for another input until they
    # input an answer that is in the list
    while animal_selection not in acceptable_inputs:
        animal_selection = input("Invalid input. Please try again: ")
    break
    # this break allows the first while loop to terminate as soon as the
    # user enters a value that satisfies the second while loops condition


def owl():
    """
    prints a owl picture
    """
    print("{o,o}")
    print(" /)_) ")
    print(" \"\"")


def frog():
    """
    prints a frog picture
    """
    print("  @..@")
    print(" (----)")
    print("( >__< )")
    print("^^ ~~ ^^")


def snowman():
    """
    prints a snowman picture
    """
    print("   _[_]_")
    print("   (*.*)")
    print(">-(  :  )-<")
    print(" (   :   )")


def bunny():
    """
    prints a bunny picture
    """
    print("(\(\ ")
    print("( -.-)")
    print("o_(\")(\")")


if animal_selection == "Owl" or animal_selection == "owl":
    print("Owl")
    owl()
if animal_selection == "Frog" or animal_selection == "frog":
    print("Frog")
    frog()
if animal_selection == "Snowman" or animal_selection == "snowman":
    print("Snowman")
    snowman()
if animal_selection == "Bunny" or animal_selection == "bunny":
    print("Bunny")
    bunny()
input()

user_random_number = input("Now I just need one more number:")
while True:
    try:
        user_random_number = float(user_random_number)
    except ValueError:
        user_random_number = input("Invalid input. Please try again: ")
    else:
        break
random_number = (3 % user_random_number)
current_age = age
if 0 <= random_number <= 2:
    print(
        "Ok, well until I learn more coding techniques and brainstorm up"
        " some new ideas,")
    print("Have a wonderful day", name, ", and I hope Mrs."
          + mothers_maiden_name,
          "and", current_pets_name, "are doing well.")
else:
    print(
        "Ok, well until I learn more coding techniques and brainstorm up"
        " some new ideas,")
    print("I hope you are living a very healthy life as a",
          current_age, "year old and that", current_pets_name,
          "is doing very well")
