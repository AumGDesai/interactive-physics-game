"""
Aum Desai
Fall 2022
CS152B Lab 08

This program is for Lab 08. 
It give the user a set of word prompts and then records their answer.
"""


def main():

    '''
    This is the main function of this program
    '''

    prompt = 'Please answer these word prompts: '
    print(prompt)

    words = ["yes ", "no ", "maybe ", "right ", "wrong ", "left ", "none ", "red ", "black ", "blah "]

    mapping = {}

    for i in words:

        mapping[i] = input(i)

    for key in mapping.keys():

        print(key + "= " + mapping.get(key))




if __name__ == "__main__":
    main()





