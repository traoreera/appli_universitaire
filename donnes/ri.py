
import os


class Reader:
    
    def __init__(self,unloker) :
        files = os.listdir()
        print(files)
        #traitement des dossier
        self.files = [file for file in files if file.endswith('.dat')]
        #files.sort()
        print(self.files)
        self.stoked()
        self.unloker = unloker
        
        if self.unloker == 1:
            
            self.reader()
        
        elif self.unloker == 0:
            
            self.stopreader()

    def stoked(self):
        with open('list','w') as file : file.write(f"{self.files}")
        


    def reader(self):
        
        try:
            self.file1 = open('drif.dat','r')
        except (FileNotFoundError,FileExistsError):
            print("error") 

    def stopreader(self):
        
        try:
            self.file1.close()
        except Exception:
            
            breakpoint()
    
        
    
        
        
    
        
Reader(unloker=1)