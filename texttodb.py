import os
import sqlite3

def convert_text_to_sqlite(text_file, sqlite_file):
    try:
        # Open a connection to the SQLite database
        conn = sqlite3.connect(sqlite_file)
        cursor = conn.cursor()

        # Create a table to store the data
        cursor.execute("CREATE TABLE IF NOT EXISTS models (model TEXT, link TEXT)")

        # Read lines from the text file and insert into the database
        with open(text_file, "r") as file:
            for line in file:
                line = line.strip()
                if " " in line:
                    username, url = line.strip().split(" ", 1)
                    cursor.execute("INSERT INTO models (model, link) VALUES (?, ?)", (username, url))
                else:
                    print(f"Skipping invalid line: {line}")

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        print("Conversion completed successfully.")
        # Send a completion message
        completion_message = send_completion_message()
        print(completion_message)

    except sqlite3.Error as e:
        print(f"Error converting text to SQLite: {e}")

def send_completion_message():
    github_account = "https://github.com/jumbubly"
    cracked_account = "https://cracked.io/rekingg"

    # Replace this with your preferred method of sending a message to the user
    # You can use email, SMS, push notification, or any other communication method
    message = f"Task completed. Text converted to SQLite successfully!\n\n"
    message += f"You can find my GitHub account here: {github_account}\n"
    message += f"And my Cracked.io account here: {cracked_account}"

    return message


# Usage: Provide the path to your text file and the desired SQLite database file
text_file_path = os.path.join(os.path.dirname(__file__), "db.txt")
sqlite_file_path = os.path.join(os.path.dirname(__file__), "db.sqlite")
convert_text_to_sqlite(text_file_path, sqlite_file_path)
