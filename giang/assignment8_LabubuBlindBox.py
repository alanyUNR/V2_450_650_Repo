import random


def open_package():
    normal_items = [
        "Santa Labubu",
        "Snowman Labubu",
        "Candy Cane Labubu",
        "Gingerbread Labubu",
        "Elf Labubu",
        "Snowflake Labubu"]

    
    for i in range(5):
        print("Box", i + 1, ":", normal_items[i]) # First five boxes contain different normal items.

    number = random.randint(1, 100) # Last box contains the secret or remaining normal item.

    if number < 5:
        print("Box 6: SECRET Reindeer Labubu with pine tree scent!")
    else:
        print("Box 6:", normal_items[5])


def main():
    print("Welcome to Giang Do Popsmart!")
    print("\nOur store currently has:Labubu Christmas Collection")
    print("Package of 6 boxes: $160")

    packages = int(input("\nHow many packages do you want? ")) #ask user how many packages they want to buy

    print("\nTotal price: $", packages * 160) #show total price based on number of packages

    for i in range(packages): # open each package and display the items inside
        print("Package", i + 1)
        open_package()

    print("\nThank you for shopping at Giang Do Popsmart!")


main()