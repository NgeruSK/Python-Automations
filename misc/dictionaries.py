#key(), values(), items() : good expound
#for k, v in dict.items()
#good checks
def running():
    birthday_dict = {'Simon':'June 12', 'Maya':'April 16','Dave':'November 30','Mike':'July 30'}
    while True:
        print('Enter a name or leave empty to quit')
        name = input()
        if not name:
            break
        if name in birthday_dict:
            print(name+' was born on '+birthday_dict[name])
        else:
            print('We do not have the info for '+name+' in our registry, press 1 to add, 2 to dismiss')
            opt = int(input())
            if opt == 1:
                print('Enter month and date')
                m_and_date= input()
                birthday_dict[name] = m_and_date
                print('Saved and Thanks, Adios!')
            elif opt == 2:
                break
            else:
                print('Not valid option, bye!')

if __name__ == '__main__':
    print('Hey')