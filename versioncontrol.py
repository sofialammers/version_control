
# sofia lammers and ellie bender 

def encoder(to_encode):
    decoded = []
    for i in to_encode:
        digit = int(i) + 3
        decoded.append(digit)
    decoded_string = ''.join(str(e) for e in decoded)
    return decoded_string
