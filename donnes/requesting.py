

class Request(object):
    """

    Args:
        object (_type_): _description_
    """
    def __init__(self,request,niveau_etude , **argv):
        
        self.request = request
        self.value = niveau_etude
        
        print(f"{self.request}: {self.value}")
        
        super(Request,self).__init__()
    
    def data_decripting(self):pass
    
    def data_verification(self):pass
    
    def data_connect(self):pass