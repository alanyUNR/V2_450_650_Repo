9:19PM completed the initial code for assignment 8_labubu blind box 

10:00PM completed 2nd version

Project Description: 
    - this program simulates buying and opening Popsmart blind boxes . 
    - Each package costs $160 and contains 6 boxes. 
    - Users enter how many packages they want to purchase, see the total price, and discover the items inside. 
    - The program use: functions, lists, loops, conditional statements, user input,  random numbers.

Initial Version
    - welcome message, collection name, package price.
    - User input: number of packages to buy.
    - calculation of the total price.
    - open_package() function display six items for each package.
    - 5 different normal items in the first 5 boxes.
    - 6th box contain: the secret item or the remaining normal item ̣there is 5̃% that secret item will appear
    - loop that opens all packages
    - thank you message.
    - In this version, the items appeared in order, and all boxes opened automatically.

AI Tool Used: Chatgpt

AI Assistance: "my current code only show the item follow the order off the normal_item list, so when the program run to open boxes, it will open the same order everytime which not bring suprise to user when playing. suggest another way that the code can change the order of the normal item when open the first 5 boxes in a package. i also want the game is more fun, suggest the way that output dont show all at once, only show new output when user hit enter or something like that, and maybe the secret dont need to show in the last box, secret can come in any order , and the rest is randome 5 different item"

New or Modified Features: 
    - show the item in a random order intead of the same order evrytime open new package. 
    - box wont open until user hit enter and secret item can come any time instead of in the last box, make the game more exciting

Evaluation of AI Output
    - random.sample(normal_items, 5) pick 5 item from the list randomly
    - copy() copy content a of list to another list
    - random.shuffle() let the item show in random order 
    - input("hit enter to open")  users need to press Enter to open each box so it more fun
    - accepting AI suggestion because it matched I wanted to imporve user experince which making the game more surprising and interactive

How to Run the Program
    - Enter positive whole number when asked how many packages you want.
    - Press Enter when prompted to open each package and box.
    - check for output 