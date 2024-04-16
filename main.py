import mysql.connector

# Establishing connection to MySQL
connection = mysql.connector.connect(
    user='root',
    database='banking',
    password='Alex.0429'
)

# Creating Functions

def create_account():
    user_id = int(input("Enter in a 5 number account number: "))
    pin = int(input("Enter a 4 number pin: "))
    username = input("Enter username: ")
    password = input("Enter password: ")
    creation_date = input("Enter creation date (YYYY-MM-DD): ")
    email = input("Enter your email: ")

    # Execute SQL query to insert new account details
    cursor = connection.cursor()
    sql = "INSERT INTO create_account ('User ID', 'Pin', 'Username', 'Password', 'Creation Date', 'Email') VALUES (%s, %s, %s, %s, %s, %s)"
    val = (user_id, pin, username, password, creation_date, email)
    cursor.execute(sql, val)

    print("Account created successfully!")

    # Commit and close
    connection.commit()
    cursor.close()

def delete_account():
    # Get user ID of the account to be deleted
    user_id = int(input("Enter account number of the account to be deleted: "))

    # Execute SQL query to delete the account
    cursor = connection.cursor()
    sql = "DELETE FROM create_account WHERE 'User ID' = %s"
    cursor.execute(sql, (user_id,))

    if cursor.rowcount > 0:
        print("Account deleted successfully!")
        connection.commit()
    else:
        print("Account with the specified user ID does not exist.")

    # Close cursor and connection
    cursor.close()

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
    sql = "UPDATE create_account SET `Username` = %s, `Password` = %s, `Email` = %s, `Pin` = %s WHERE `User ID` = %s"
    val = (new_username, new_password, new_email, new_pin, user_id)
    cursor.execute(sql, val)

    if cursor.rowcount > 0:
        print("Account information updated successfully!")
        connection.commit()
    else:
        print("Account with the specified user ID does not exist.")

    # Close cursor and connection
    cursor.close()

def deposit():
    # Get user ID and amount to deposit
    user_id = int(input("Enter account number: "))
    amount = float(input("Enter amount to deposit: "))

    # Execute SQL query to update account balance
    cursor = connection.cursor()
    sql_select = "SELECT balance FROM create_account WHERE `User ID` = %s"
    cursor.execute(sql_select, (user_id,))
    result = cursor.fetchone()

    if result:
        current_balance = result[0]
        new_balance = current_balance + amount
        sql_update = "UPDATE create_account SET balance = %s WHERE `User ID` = %s"
        val = (new_balance, user_id)
        cursor.execute(sql_update, val)
        connection.commit()
        print("Deposit successful. New balance: {:.2f}".format(new_balance))
    else:
        print("Account with the specified user ID does not exist.")

    # Close cursor and connection
    cursor.close()

def withdraw():
    # Get user ID and amount to deposit
    user_id = int(input("Enter account number: "))
    amount = float(input("Enter amount to withdraw: "))

    # Execute SQL query to update account balance
    cursor = connection.cursor()
    sql_select = "SELECT balance FROM create_account WHERE `User ID` = %s"
    cursor.execute(sql_select, (user_id,))
    result = cursor.fetchone()

    if result:
        current_balance = result[0]
        if current_balance >= amount:
            new_balance = current_balance - amount
            # Execute SQL query to update account balance
            sql_update = "UPDATE create_account SET balance = %s WHERE `User ID` = %s"
            val = (new_balance, user_id)
            cursor.execute(sql_update, val)
            connection.commit()
            print("Withdrawal successful. New balance: {:.2f}".format(new_balance))
        else:
            print("Insufficient funds.")
    else:
        print("Account with the specified user ID does not exist.")

    # Close cursor and connection
    cursor.close()

def main_menu():
    print("Welcome to our application!")
    print("Main Menu:")
    print("1. Create an account")
    print("2. Delete an account")
    print("3. Modify an account")
    print("4. Deposit an amount into an account")
    print("5. Withdraw an amount from an account")
    print("6. Exit the app")

    # Prompt user for choice
    choice = input("Enter your choice (1-6): ")

    # Call corresponding function based on user's choice
    if choice == '1':
        create_account()
    elif choice == '2':
        delete_account()
    elif choice == '3':
        modify_account()
    elif choice == '4':
        deposit()
    elif choice == '5':
        withdraw()
    elif choice == '6':
        print("Exiting the application. Goodbye!")
        # Close the database connection before exiting
        connection.close()
        exit()
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main_menu()
