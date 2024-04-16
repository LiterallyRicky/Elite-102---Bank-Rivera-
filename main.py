import mysql.connector

# Establishing connection to MySQL
connection = mysql.connector.connect(
    user='root',
    database='banking',
    password='Alex.0429'
)

# End

# Creating Functions
def main_menu():
    print("Welcome to our application!")
    print("Main Menu:")
    print("1. Create an account")
    print("2. Delete an account")
    print("3. Modify an account")
    print("4. Deposit an amount into an account")
    print("5. Withdrawl an amount from an account")

if __name__ == "__main__":
    main_menu()

def create_account():
    user_id = int(input("Enter in a 5 number account number: "))
    pin = int(input("Enter a 4 number pin: "))
    username = input("Enter username: ")
    password = input("Enter password: ")
    creation_date = input("Enter creation date (YYYY-MM-DD): ")
    email = input("Enter your email: ")

    # Execute SQL query to insert new account details
    cursor = connection.cursor()
    sql = "INSERT INTO create_account (`User ID`, `Username`, `Password`, `Creation Date`, `Email`, `Pin`) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (user_id, username, password, creation_date, email, pin)
    cursor.execute(sql, val)

    print("Account created successfully!")

    # Commit and close
    connection.commit()
    cursor.close()
    connection.close()

# Call the function to create an account
create_account()

def delete_account():
    # Get user ID of the account to be deleted
    user_id = int(input("Enter account number of the account to be deleted: "))

    # Execute SQL query to delete the account
    cursor = connection.cursor()
    sql = "DELETE FROM create_account WHERE `User ID` = %s"
    cursor.execute(sql, (user_id,))

    if cursor.rowcount > 0:
        print("Account deleted successfully!")
        connection.commit()
    else:
        print("Account with the specified user ID does not exist.")

    # Close cursor and connection
    cursor.close()

# Call the function to delete an account
delete_account()

def modify_account():
    # Get user ID of the account to be modified
    user_id = int(input("Enter account number of the account to be modified: "))

    # Get new username, password, and email
    new_username = input("Enter new username: ")
    new_password = input("Enter new password: ")
    new_email = input("Enter new email: ")
    new_pin = input("Enter new pin: ")

    # Execute SQL query to update account information
    cursor = connection.cursor()
    sql = "UPDATE create_account SET 'Username' = %s, 'Password' = %s, 'Email' = %s, 'Pin' = %s WHERE 'User ID' = %s"
    val = (new_username, new_password, new_email, new_pin, user_id)
    cursor.execute(sql, val)

    if cursor.rowcount > 0:
        print("Account information updated successfully!")
        connection.commit()
    else:
        print("Account with the specified user ID does not exist.")

    # Close cursor and connection
    cursor.close()

# Call the function to modify account information
modify_account()

#User makes the choice of which option