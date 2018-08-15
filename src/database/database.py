import database.CloudantDb as db



class Database:
        __instance = None

        @staticmethod
        def getDatabase():
            if Database.__instance == None :
                Database.__instance = db.db()
            return Database.__instance
