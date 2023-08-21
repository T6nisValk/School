"""
Cats - Write a program that will correctly display the sentence "Alice has x cats" 
depending on the number of cats, it can show: Alice has 1 cat, Alice has 2 cats, 
Alice has 10 cats. use user input to get amount of cats
"""


def alices_cats(amount_of_cats):
    return (
        f"Alice has {amount_of_cats} cat"
        if amount_of_cats == 1
        else f"Alice has {amount_of_cats} cats"
    )


print(alices_cats(int(input("How many cats?: "))))
