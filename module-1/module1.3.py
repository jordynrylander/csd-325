# Jordyn Rylander
# 1.3 module
# CSD-325
# the program asks users how many bottles of beer are on the wall,
# it counts down to 1 using a function, and reminds users to buy more beer.


# making the countdown with the if/else function
# counts down the numbers of beer on the wall
def countdown_bottles(bottles):
    #the loop
    while bottles > 1:
        #display current number of bottles
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        bottles = bottles - 1

        # checking if only one remains
        if bottles == 1:
            print(f"Take one down, pass it around, {bottles} bottle of beer on the wall.\n")
        else:
            print(f"Take one down, pass it around, {bottles} bottles of beer on the wall.\n")
# ONE BOTTLE LEFT? this is the final verse
    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down, pass it around, no more bottles of beer on the wall.\n")


# the main program
def main():
    # ask how many number of bottles
    bottles = int(input("How many bottles of beer are on the wall?"))
    countdown_bottles(bottles)
    print("Buy more beer!")

main()
