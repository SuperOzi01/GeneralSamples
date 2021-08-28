
Names = ['Amal','Mohammed','Khadijah','Abullah','Rawan','Faisal','Layla']
Numbers = ['1111111111','2222222222','3333333333','4444444444','5555555555','6666666666','7777777777']
PhoneBook = []
def main():
    InitialData()
    MainProgram()
    return True

def InitialData():
    for i in range(len(Names)):
        item = {
            'Name': Names[i],
            'Number': Numbers[i]
        }
        PhoneBook.append(item)

def SearchByName(name):
    for i in range(len(PhoneBook)):
        if(PhoneBook[i]['Name'] == name):
            print('The Data Found: ', PhoneBook[i]['Name'], PhoneBook[i]['Number'])
            return True
    print('Sorry, the number is not found')
    return False

def SearchByNumber(number):
    if(len(number) < 10):
        print('This is invalid number')
        return False

    for i in range(len(PhoneBook)):
        if(PhoneBook[i]['Number'] == number):
            print('The User is found: ', PhoneBook[i]['Name'], PhoneBook[i]['Number'])
            return True
    print('Sorry, the number is not found')
    return False

def AddUser(name, number):
    if(str(name).isalpha() and str(number).isalnum()):
        item = {
            'Name': name,
            'Number': number
        }
        PhoneBook.append(item)
        print('Operation is successful')
        return True
    print('This Operation faced issue check your input again')
    return False

def MainProgram():
    Start = True
    while(Start):
        print('Select [1] To Search By Name')
        print('Select [2] To Search By Number')
        print('Select [3] To Add Your Number in the Phone Book')
        print('Select [4] To Exit')
        selection = input()
        if(selection == '4'):
            Start = False
        elif(selection == '1'):
            Name_Value = input('Enter The Name You Want To Search For ')
            SearchByName(Name_Value)
        elif(selection == '2'):
            Number_Value = input('Enter The Number You Want To Search For ')
            SearchByNumber(Number_Value)
        else:
            UserName = input('Enter Your Name ')
            UserNumber = input('Enter Your Number ')
            AddUser(UserName, UserNumber)



main()