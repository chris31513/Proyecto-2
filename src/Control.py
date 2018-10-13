from .Steve import Steve
from .DAO import DAO
from .SQLite import SQLite
class Control(object):
    def mine(self):
        print("...Minando")
        sql = SQLite()
        sql.connect()
        minner = Steve()
        minner.get_mp3()
        minner.get_mp3_tags()
        minner.insertion()
    def consult(self):
        dao = DAO()
        return dao.consult()
