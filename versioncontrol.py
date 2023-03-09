
# sofia lammers and ellie bender 

def encoder(to_encode):
    decoded = []
    for i in to_encode:
        digit = int(i) + 3
        decoded.append(digit)
    decoded_string = ''.join(str(e) for e in decoded)
    return decoded_string

# joshua park
def decode(decoded):
    decoded_pwd = ''
    input_list = list(decoded)
    for i in range(0, len(input_list)):
        input_list[i] = int(input_list[i])
        if input_list[i] > 2:
            input_list[i] -= 3
        else:
            input_list[i] += 7
    for i in range(0, len(input_list)):
        decoded_pwd += str(input_list[i])
    return decoded_pwd


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
    elif option == 2:
        decoded_pwd = decode(decoded)
        print(f"The encoded password is {decoded}, and the original password is {decoded_pwd}.")
    elif option == 3:
        game_continue = False
