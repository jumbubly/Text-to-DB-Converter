import os
import sqlite3

def create_database():
    try:
        # Determine the file path for the SQLite database
        db_file = os.path.join(os.path.dirname(__file__), "db.sqlite")

        # Open a connection to the SQLite database
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Execute SQL statements to create tables or perform other operations
        # Example: Create a table called 'data' with columns 'username' and 'url'
        cursor.execute("CREATE TABLE IF NOT EXISTS data (username TEXT, url TEXT)")

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        print(f"Database created successfully: {db_file}")
        # Send a completion message
        completion_message = send_completion_message()
        print(completion_message)

    except sqlite3.Error as e:
        print(f"Error creating database: {e}")

def send_completion_message():
    github_account = "https://github.com/jumbubly"
    cracked_account = "https://cracked.io/rekingg"

    # Replace this with your preferred method of sending a message to the user
    # You can use email, SMS, push notification, or any other communication method
    message = f"Task completed. Database created successfully!\n\n"
    message += f"You can find my GitHub account here: {github_account}\n"
    message += f"And my Cracked.io account here: {cracked_account}"

    return message


# Usage
create_database()
