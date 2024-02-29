import sqlite3

# Connect to SQLite database (creates a new file if it doesn't exist)
conn = sqlite3.connect('data.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table in the database
#timestamp,domain,query_type,dnssec,protocol,client_ip,status,reasons,destination_country,
#root_domain,device_id,device_name,device_model,device_local_ip,matched_name,client_name

cursor.execute('''
    CREATE TABLE IF NOT EXISTS userdata (
        id INTEGER PRIMARY KEY,
        timestamp TEXT,
        domain TEXT,
        query_type TEXT,
        dnssec TEXT,
        protocol TEXT,
        client_ip TEXT,
        status TEXT,
        reasons TEXT,
        destination_country TEXT,
        root_domain TEXT,
        device_id TEXT,
        device_name TEXT
                   )
''')

f = open("data.csv", "r")
f.readline()
lineList = []
word = ""
wordCounter = 0
innerList = []
user_data = []

line = f.readline()
while line:
    for letter in line:
        if letter != ",":
            word += letter
        if letter == "," and wordCounter <= 11:
            innerList.append(word)
            word = ""
            wordCounter += 1 
        if wordCounter >= 12:
            user_data.append(innerList)
            line = f.readline()  
            wordCounter = 0
            innerList = []
            break    
        

cursor.executemany('''
    INSERT INTO userdata (timestamp, domain, query_type, dnssec, protocol, client_ip, status, reasons, destination_country, root_domain, device_id, device_name )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', user_data)


f.close()

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()