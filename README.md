# dbsql
 create a database file first & convert your data that you have in your text file into a database file with these scripts

createdb.py
create_database(): This function creates an SQLite database file named db.sqlite and a table called data with columns username and url. It opens a connection to the database, executes the SQL statement to create the table if it does not exist, and then commits the changes and closes the connection.

texttodb.py
convert_text_to_sqlite(text_file, sqlite_file): This function reads lines from a text file and inserts the data into an SQLite database table named models. It opens a connection to the SQLite database, creates the table if it does not exist, and then iterates through each line in the text file. If a line contains a space, it assumes it has the format "username url" and splits it to extract the username and url values. It then inserts these values into the models table. If a line does not contain a space, it is skipped as an invalid line. After inserting all the valid lines, the function commits the changes and closes the connection.

To use the scripts, you can simply execute them directly. The createdb.py script will create the database and print a success message, while the texttodb.py script will read the lines from a text file and insert the data into the database, also printing a success message.