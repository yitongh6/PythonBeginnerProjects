# Prompt user to enter some words and create a passage.
# Learning Objs: (1) Concatenation, (2) f-string f""
def madlib_icecream():
    person_female = input("Enter a female name: ")
    person_male = input("Enter a male name: ")
    adj1 = input("Enter a adj: ")
    vrb1 = input("Enter a vrb: ")
    vrb2 = input("Enter another vrb: ")

    madlib_ic = f"\nYour madlib is:\n{person_female} is {adj1}. She {vrb1}s {person_male} and {vrb2}s \
    ice cream."

    print(madlib_ic)

#uncomment to try out the function
#madlib_icecream()