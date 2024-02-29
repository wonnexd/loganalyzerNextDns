import tkinter as tk
import sqlite3

def fetch_data():
    # Connect to the SQLite database
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    # Fetch 10 lines from the userdata table
    cursor.execute("SELECT count(*) as Count, root_domain FROM userdata where status = 'blocked' group by root_domain order by count(*) desc LIMIT 10")
    rows = cursor.fetchall()

    # Display the data in a new window
    display_window = tk.Toplevel(root)
    display_window.title('User Data')

    # Create a label for each row of data
    for i, row in enumerate(rows):
        label_text = ', '.join(map(str, row))
        label = tk.Label(display_window, text=label_text)
        label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)

    # Close the database connection
    connection.close()

def update_data():
    # Connect to the SQLite database
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    # Fetch 10 lines from the userdata table
    cursor.execute("SELECT count(*), reasons FROM userdata where status = 'blocked' group by reasons order by count(*) desc LIMIT 10")
    rows = cursor.fetchall()

    # Display the data in a new window
    display_window = tk.Toplevel(root)
    display_window.title('User Data')

    # Create a label for each row of data
    for i, row in enumerate(rows):
        label_text = ', '.join(map(str, row))
        label = tk.Label(display_window, text=label_text)
        label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)

    # Close the database connection
    connection.close()

def delete_data():
    # Add code for deleting data here
    pass

# Create the main application window
root = tk.Tk()
root.title('User Data Management')

# Create buttons for different actions
fetch_button = tk.Button(root, text='Most blocked root domains', command=fetch_data)
fetch_button.pack(pady=10)

update_button = tk.Button(root, text='Reason for blocking', command=update_data)
update_button.pack(pady=10)

delete_button = tk.Button(root, text='Delete Data', command=delete_data)
delete_button.pack(pady=10)

exit_button = tk.Button(root, text='Exit', command=root.destroy)
exit_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
