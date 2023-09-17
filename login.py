# Program need (FileHandling)
# While Registering user Ask the usertype whether he/she is buyer or seller
# While Login get the user type
# If usertype while login is buyer he/she can see all the products and he/she can buy all the products.
# If usertype while login is seller he/her can add products and he/she can see their products sold.

# Task
# Let the (buyer/seller)user to continue the system even after running a function, but if he/she wants to logout then logout
# Let the seller view his/her total revenue
import json


def userCredentials():
    userName = input('Enter Username: ')
    userPassword = input('Enter Password: ')

    return userName, userPassword

def regestration():
    f = open('E:/Kshitiz/Mind risers/userDB.txt','a')
    userDatabase = {'user_name' : userName, 'user_password' : userPassword, 'user_type' : userType}
    f.write(json.dumps(userDatabase) + '\n')
# file = json.loads('E:/Kshitiz/Mind risers/userDB.json')

    # print(file)
    f.close()

def loading_userDB():
    f = open('E:/Kshitiz/Mind risers/userDB.txt','r')
    user_info = f.read()
    user_info_list = user_info.split('\n')
    for data in user_info_list:
        if data != '':
            user_info_dict = json.loads(data)
            # return user_info_dict
    #     if userName == user_info_dict['user_name'] and userPassword == user_info_dict['user_password']:
    #         userType = user_info_dict['user_type']
    #         print(f'You have successfully Loggedin as {userType}.')
             

    # else:
    #     print('Invalid User.')

def products():
    f = open('E:/Kshitiz/Mind risers/productDB.txt','a')
    
    product_name = input('Enter your product name : ')
    product_detail = input('Enter your product detail : ')
    product_price = input('Enter your product price : ')
    seller_name = userName
    product_info = {'name':product_name,'detail':product_detail,'price':product_price,'seller': seller_name}
    f.write(json.dumps(product_info)+'\n')

    f.close()

def seller():
    while True:
        seller_choice  = input('''
                                            1. Add product
                                            2. See all the purchase infos
                                            3. Logout
                                            select a id option :''')
        if seller_choice == '1':
            products()
        elif seller_choice == '2':
            buyer()
        elif seller_choice == '3':
            print('Logged Out !')
            print('Thank You for using our service.')
            break
        else:
            print('Invalid input.')


def buyer():
    f = open('E:/Kshitiz/Mind risers/productDB.txt','r')
    p = f.read()
    product_list = p.split('\n')
    for data in product_list:
        if data != '':
            product_dict = json.loads(data)
            print(product_dict)

def login():
    f = open('E:/Kshitiz/Mind risers/userDB.txt','r')
    user_info = f.read()
    user_info_list = user_info.split('\n')
    for data in user_info_list:
        if data != '':
            user_info_dict = json.loads(data)
        if userName == user_info_dict['user_name'] and userPassword == user_info_dict['user_password']:
            userType = user_info_dict['user_type']
            print(f'You have successfully Loggedin as {userType}.')
            if userType == 'buyer':
                buyer()
            elif userType == 'seller':
                seller()
            break  

        else:
            print('Invalid User.')

            
# products()

    f.close()

while True:
    i = input('Do You Want To Login/Regestration/Exit: ').casefold()
    if i == 'login':
        userName, userPassword = userCredentials()
        login()
    elif i == 'regestration':
        userType = input('Regester as Buyer / Seller: ')
        userName, userPassword = userCredentials()
        regestration()
        print(f'Your username "{userName}" & password "{userPassword}" been Regestred / saved in Database as "{userType}"')
    elif i == 'exit':
        print('Thanks for using our Service. ')   
        break
    else:
        print('Invalid Command. ')

