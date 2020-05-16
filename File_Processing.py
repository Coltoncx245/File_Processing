import os


directory = input('Input the directory you would like to save the file in: ')
directory = directory.strip()
# user inputs directory
name_of_file = input('Input a name for the file: ')
name_of_file = f'\\{name_of_file.strip().replace(" ", "_")}.txt'
# user inputs filename
name = input('Enter your name: ').title()
address = input('Enter your address: ')
phone_number = input('Enter your phone number: ')

try:
    if not os.path.exists(f'{directory}'):  # checking for directory
        os.makedirs(f'{directory}')  # make directory if it doesn't exist
    f = open(f'{directory}{name_of_file}', "a")

    f.write(f'{name}, {address}, {phone_number}\n')  # writing information to file
    f.close()

except IOError:
    print(f'Error reading file {name_of_file}')



