import sqlite3

#parameters: server=string, server_owner=string, prefix=string
#parameters: server=string, server_owner=string, prefix=string
#parameters: server=string
#parameters: server=string, column=string
#^Notes to consider adding later to specific methods



class sql:
    """
    INSTANCE VARIABLES:
    db: database connected to
    conn: connection to sql database
    crsr: cursor for sql commands
    """

    #constructs sql object to handle data for discord bot
    def __init__(self, database):
        self.db = database
        self.conn = sqlite3.connect(self.db)
        self.crsr = self.conn.cursor()

        print("Connected to SQL database")

    #sets up table for server information to be saved
    def setup(self, needed):
        if needed:
            #sql command to create table
            command = """CREATE TABLE "servers" (
            "guild_id" INTEGER,
            "command" TEXT,
            "admin_role" TEXT,
            PRIMARY KEY("guild_id")
            );"""

            #executes command to create table
            self.crsr.execute(command)

            #commits changes to db
            self.conn.commit()

            print("SQL table setup")

    #adds server info to table servers
    def add(self, server, server_owner):
        #sql command to add values to table
        command = """INSERT INTO servers
        VALUES ("""+server+", ':', 'None');"

        #executes command to add values to table
        self.crsr.execute(command)

        #commits changes to db
        self.conn.commit()

        print("Added server {} to database".format(server))

    #changes values in table servers
    def change(self, server, prefix=None, admin=None):
        #if statements control what is changed based on whether they have values
        if prefix is not None:
            #sql command to change command value in table
            command = """UPDATE servers
            SET admin_role='"""+prefix+"""'
            WHERE guild_id="""+server+";"
            #executes command to change command value in table
            self.crsr.execute(command)

        if admin is not None:
            #sql command to change guild_owner value in table
            command = """UPDATE servers
            SET admin_role='"""+admin+"""'
            WHERE guild_id="""+server+";"
            #executes command to change guild_owner value in table
            self.crsr.execute(command)

        #commits changes to db
        self.conn.commit()

        print("Field changed")

    #deletes values from table servers
    def delete(self, server):
        #sql command to delete entry in table servers
        command = """DELETE FROM servers
        WHERE guild_id="""+server+";"

        #executes command to delete entry in table servers
        self.crsr.execute(command)

        #commits changes to db
        self.conn.commit()

        print("Deleted server {} from database".format(server))

    #reads from sql server based on server and column given
    def read(self, server, column):
        #sql command to read column for server in table servers
        command = "SELECT "+column+""" FROM servers
        WHERE guild_id="""+server+";"

        #executes command to read column for server in table servers
        self.crsr.execute(command)

        #grabbing data from sql command
        data = self.crsr.fetchall()

        #commits changes to db
        self.conn.commit()

        print("read a thing. Specifically: ")
        print(data[0][0])
        print(data)

        #returning data
        return data[0][0]
