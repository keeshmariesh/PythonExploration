# More features of functions
# Can set default parameter value as with 'width'
# Can raise an exception as with 'raise ValueError'
# Does not have to return a value; if so, returns None

def banner_text(text=" ", width=80):
    if len(text) > width - 4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, width))

    if text == "*":
        print("*" * width)
    else:
        centered_text = text.center(width - 4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)


screen_width = 60

banner_text("*", screen_width)
banner_text("Always look on the bright side of life...", screen_width)
banner_text("If life seems jolly rotten", screen_width)
banner_text("There's something you've forgotten!", screen_width)
banner_text("And that's to laugh and smile and dance and sing,", screen_width)
banner_text(width = screen_width)
banner_text("When you're feeling in the dumps,", screen_width)
banner_text("Don't be silly chumps,", screen_width)
banner_text("Just purse your lips and whistle - that's the thing!", screen_width)
banner_text("And... always look on the bright side of life...", screen_width)
banner_text("*", screen_width)

# As expected assigning the value of the function to a variable will
# return None
#
# result = banner_text("Nothing is returned", screen_width)
# print(result)
#
# numbers = [4, 2, 7, 5, 8, 3, 9, 6, 1]
# the following will return None because it performs an action
# print(numbers.sort())