import sqlite3

#sets up table for discord bot on database given
#parameters: db=string
def setup(db):
    #assigns global variable with database to be used by other commands
    global database
    database = db
    #connecting to database
    connection = sqlite3.connect(database)

    #creates cursor to read commands
    crsr = connection.cursor()

    #sql command to create table
    command = """CREATE TABLE "servers" (
    "guild_id" INTEGER,
    "guild_owner" INTEGER,
    "command" TEXT,
    "admin_role" TEXT,
    PRIMARY KEY("guild_id")
    );"""

    #executes command to create table
    crsr.execute(command)

    #commits changes to db
    connection.commit()

    #closes connection to db
    connection.close()

#adds server info to servers table
#parameters: server=string, server_owner=string, prefix=string
def add(server, server_owner):
    database = "blep.db"
    #connecting to database
    connection = sqlite3.connect(database)

    #creates cursor to read commands
    cursor = connection.cursor()

    #sql command to add values to table
    command = """INSERT INTO servers
    VALUES ("""+server+", "+server_owner+", ':P', 'None');"

    #executes command to add values to table
    cursor.execute(command)

    #commits changes to db
    connection.commit()

    #closes connection to db
    connection.close()

#changes values in table servers
#parameters: server=string, server_owner=string, prefix=string
def change(server, server_owner=None, prefix=None, admin=None):
    database = "blep.db"
    #connecting to database
    connection = sqlite3.connect(database)

    #creates cursor to read commands
    cursor = connection.cursor()

    #if statements control what is changed based on whether they have values
    if server_owner is not None:
        #sql command to change guild_owner value in table
        command = """UPDATE servers
        SET guild_owner="""+server_owner+"""
        WHERE guild_id="""+server+";"
        #executes command to change guild_owner value in table
        cursor.execute(command)

    if prefix is not None:
        #sql command to change command value in table
        command = """UPDATE servers
        SET command='"""+prefix+"""'
        WHERE guild_id="""+server+";"
        #executes command to change command value in table
        cursor.execute(command)

    if admin is not None:
        #sql command to change guild_owner value in table
        command = """UPDATE servers
        SET admin_role='"""+admin+"""'
        WHERE guild_id="""+server+";"
        #executes command to change guild_owner value in table
        cursor.execute(command)

    #commits changes to db
    connection.commit()

    #closes connection to db
    connection.close()

#deletes values from table servers
#parameters: server=string
def delete(server):
    database = "blep.db"
    #connecting to database
    connection = sqlite3.connect(database)

    #creates cursor to read commands
    cursor = connection.cursor()

    #sql command to delete entry in table servers
    command = """DELETE FROM servers
    WHERE guild_id="""+server+";"

    #executes command to delete entry in table servers
    cursor.execute(command)

    #commits changes to db
    connection.commit()

    #closes connection to db
    connection.close()

#reads from sql server based on server and column given
#parameters: server=string, column=string
def read(server, column):
    database = "blep.db"
    #connecting to database
    connection = sqlite3.connect(database)

    #creates cursor to read commands
    cursor = connection.cursor()

    #sql command to read column for server in table servers
    command = "SELECT "+column+""" FROM servers
    WHERE guild_id="""+server+";"

    #executes command to read column for server in table servers
    cursor.execute(command)

    #grabbing data from sql command
    data = cursor.fetchall()

    #commits changes to db
    connection.commit()

    #closes connection to db
    connection.close()

    #returning data
    return data[0][0]
