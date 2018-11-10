import pickle as pk

def main():
    with open('user.dat', 'rb' ) as file:
        data = pk.load(file)

    print(data)
main()
