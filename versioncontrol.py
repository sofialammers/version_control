
# sofia lammers and ellie bender 

def encoder(to_encode):
    decoded = []
    for i in to_encode:
        digit = int(i) + 3
        decoded.append(digit)
    decoded_string = ''.join(str(e) for e in decoded)
    return decoded_string
game_continue = True
while game_continue:
    print("\nMenu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")
    option = int(input("\nPlease enter an option: "))
    if option == 1:
        to_encode = (input("Please enter your password to encode: "))
        decoded = encoder(to_encode)
        print("Your password has been encoded and stored!")
