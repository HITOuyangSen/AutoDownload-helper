import MySQLdb

class  SqlConn(object):
    def __init__(self):
        self.conn=self.get_conn()
        self.cursor=self.conn.cursor()
        
    def get_conn(self):
        """ 获取连接"""
        conn=MySQLdb.connect(
                # host="localhost",
                host="127.0.0.1",
                port=3306,
                user="root",
                passwd="123456",
                db="students_account",
                charset='utf8')
        return conn
        
    def close_conn(self):
            if self.conn:
                # 关闭连接
                self.conn.close()
            
    def insert(self,acct:str,pswd:str):
        try:
            conn=self.get_conn()
            cursor=conn.cursor()
            cursor.execute('INSERT INTO `students_account`.`accounts`(`username`, `password`) VALUES ("{}", {})'.format(acct,pswd))
            conn.commit()
            cursor.close()
            self.close_conn()  
            return True
        except :
            cursor.close()
            self.close_conn()  
            return False
    
    def update(self,acct:str,pswd:str):
        try:
            self.conn=self.get_conn()
            cursor=self.conn.cursor()
            cursor.execute('UPDATE `students_account`.`accounts` SET `password`= "{}" where `username`="{}"'.format(pswd,acct))
            self.conn.commit()
            self.close_conn()  
            return True
        except :
            cursor.close()
            self.close_conn()  
            return False
    
