import re

container=[]
users={}
user_count=1


def check_email():
    email = False
    reg_email = input('Enter your email address:\n')
    if re.findall('^\S+@\S+', reg_email):
        email = True
    else:
        print('invalid email')
        check_email()

    return email



#getting new users details
def getting_details_new_reg():
    reg_first_name = input('Enter your first name: \n')
    reg_last_name = input('Enter your last name: \n')
    while True:
        reg_phone_number = input('Enter your phone number:\n ')
        try:
            phone_number=int(reg_phone_number)
            break
        except ValueError:
            print('Enter a numeric value')
    email=check_email()
    reg_dob = input('Enter your date of birth:e.g 01/08/1999:\n  ')
    reg_marital_status = input('Enter your marital status: \n')
    reg_previous_illness = input('Enter your previous illness: \n')
    reg_current_illness=input('Enter current illness: \n')
    address=input('address: ')

    details=[reg_first_name,reg_last_name,reg_phone_number,email,reg_dob,reg_marital_status,reg_previous_illness,
                 reg_current_illness]

    return details


#generating password

def gen_password(details):
    generate_password=False
    check_password= details[0][0:2] + details[1][1]
    #print(check_password)
    generate_password = input('Use the first 2 letters of your first name and 1st of your last name with other letters and numbers: ')
    password=list(generate_password)
    #print(password)
    user_password=password[0]+password[1]+password[2]
    #print(user_password)
    if check_password==user_password:
        generate_password=True
    else:
        print('password not accepted :start password with 2 first letters of your first name and the first of your last')
        gen_password(details)



def homepage_login():

    login_page=int(input('Enter 1 for a new user and 2 for an existing user: \n'))
    if login_page==1:
        details=getting_details_new_reg()
        gen_password(details)
        details.append(gen_password)
        # compiling user details to the container
        container.append(details)
        users[user_count] = details
        print(users)
        homepage_login()

homepage_login()