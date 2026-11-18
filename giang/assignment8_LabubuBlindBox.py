import random


def open_package():
    normal_items = [
        "Santa Labubu",
        "Snowman Labubu",
        "Candy Cane Labubu",
        "Gingerbread Labubu",
        "Elf Labubu",
        "Snowflake Labubu"]
    secret_item = "Reindeer Labubu with pine tree scent"

    number = random.randint(1, 100)

    if number <= 5: # 5% chance to get the secret item
        package_items = random.sample(normal_items, 5) # picks 5 different normal items without duplicates and store in a list -> Chatgpt assistance
        package_items.append(secret_item) #add secret item to the list of package items -> Chatgpt assistance
    else:
        package_items = normal_items.copy() # copy the normal items list to avoid modifying the original -> Chatgpt assistance
    
    random.shuffle(package_items) # shuffle the package items to randomize their order -> Chatgpt assistance
    
    for i in range(6):
        input(f"\nPress Enter to open Box {i + 1}...") #prompt user to open each box
        print("You got:", package_items[i]) # display the item in the box 

def main():
    print("Welcome to Giang Do Popsmart!")
    print("\nOur store currently has:Labubu Christmas Collection")
    print("Package of 6 boxes: $160")

    packages = int(input("\nHow many packages do you want? ")) #ask user how many packages they want to buy

    print("\nTotal price: $", packages * 160) #show total price based on number of packages

    for i in range(packages): # open each package and display the items inside
        input(f"\nPress Enter to open your package {i + 1}...") #prompt user to open each package -> Chatgpt assistance
        print("Package", i + 1)
        open_package()

    print("\nThank you for shopping at Giang Do Popsmart!")


main()