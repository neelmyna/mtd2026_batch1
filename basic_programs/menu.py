
def monday():
    print('You selected Monday')

def tuesday():
    print('You selected tuesday')

def wednesday():
    print('You selected wednesday')

def thursday():
    print('You selected thursday')

def friday():
    print('You selected friday')

def menu(choice):
    match choice:
        case 1 : monday()
        case 2 : tuesday()
        case 3 : wednesday()
        case 4 : thursday()
        case 5 : friday()
        case _ : print('Invalid choice entered')

def run_app():
    while True:
        print('1:monday 2:tuesday 3:wednesday 4:thursday 5:friday 6:exit')
        choice = int(input('Entrer your choice(1-6): '))
        if choice == 6:
            break
        menu(choice)
    print('End of App')

run_app()
