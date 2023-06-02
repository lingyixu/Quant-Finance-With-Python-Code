class DBConnection:
    
    db_conn = None
    
    @classmethod
    def get_instance(cls):
        if cls.db_conn is None:
            cls.db_conn = DBConnection()
        return cls.db_conn

