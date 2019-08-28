import sqlite3

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
        self.crsr = slef.conn.cursor()

    #sets up table for server information to be saved
    def setup(self):
        #sql command to create table
        command = """CREATE TABLE "servers" (
        "guild_id" INTEGER,
        "guild_owner" INTEGER,
        "command" TEXT,
        "admin_role" TEXT,
        PRIMARY KEY("guild_id")
        );"""

        #executes command to create table
        self.crsr.execute(command)

        #commits changes to db
        self.conn.commit()

    #adds server info to table servers
    def add(server, server_owner):
        #sql command to add values to table
        command = """INSERT INTO servers
        VALUES (?, ?, ':P', 'None');"""

        #executes command to add values to table
        self.crsr.execute(command, (server, server_owner))

        #commits changes to db
        self.conn.commit()

    #changes values in table servers
    def change(server, server_owner=None, prefix=None, admin=None):
        #if statements control what is changed based on whether they have values
        if server_owner is not None:
            #sql command to change guild_owner value in table
            command = """UPDATE servers
            SET guild_owner=?
            WHERE guild_id=?;"""
            #executes command to change guild_owner value in table
            self.crsr.execute(command, (server_owner, server))

        if prefix is not None:
            #sql command to change command value in table
            command = """UPDATE servers
            SET command='?'
            WHERE guild_id=?;"""
            #executes command to change command value in table
            self.crsr.execute(command, (prefix, server))

        if admin is not None:
            #sql command to change guild_owner value in table
            command = """UPDATE servers
            SET admin_role='?'
            WHERE guild_id=?;"""
            #executes command to change guild_owner value in table
            self.crsr.execute(command, (admin, server))

        #commits changes to db
        self.conn.commit()

    #deletes values from table servers
    def delete(server):
        #sql command to delete entry in table servers
        command = """DELETE FROM servers
        WHERE guild_id=?;"""

        #executes command to delete entry in table servers
        self.crsr.execute(command, (server))

        #commits changes to db
        self.conn.commit()

    #reads from sql server based on server and column given
    def read(server, column):
        #sql command to read column for server in table servers
        command = """SELECT ? FROM servers
        WHERE guild_id=?;"""

        #executes command to read column for server in table servers
        self.crsr.execute(command, (column, server))

        #grabbing data from sql command
        data = self.crsr.fetchall()

        #commits changes to db
        self.conn.commit()

        #returning data
        return data[0][0]
