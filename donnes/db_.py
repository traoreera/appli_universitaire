import mysql.connector as connector
import ri
class New_user(): 
    
    def __init__(self) -> None:
        pass
        
    def user_info(self,nom,prenom,age,sexe,username,password,email,number,id):
        #information traite 
        
        return (nom,prenom,age,sexe,username,password,email,number,id)
    
    def executing_request(self,value_in):
        pass



class connect:
    """
    """
    def __init__(self,user,host,port,password,dataBase):
        self.host =host
        self.port=port
        self.user = user
        self.password = password
        self._db_base = dataBase
        connect._Connect(self)
        
    def _Connect(self):
        try:
            mydb = connector.connect(host=self.host,user=self.user,password=self.password,database=self._db_base)
            curseur = mydb.cursor()
            print("connected of successfull")
            self._verifed(curseur)
            
        except Exception as e : print(e)
        
        
    def _verifed(self,curseur):
        results =curseur.execute("select * from login")
        print(results)
        



class New_Compte:
    
    def __init__(self,curseur,request,):
        
        self.curseur = curseur # Curseur pour la base de donne 
        self.request = request # la requete a execute

        

#connect(user="root",host="localhost",port="3306",password="hunters360X",dataBase="test")