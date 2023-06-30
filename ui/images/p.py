import os

list_inage = [file for file in os.listdir() if file.endswith('jpg') or file.endswith('png')]


i=0

while i != len(list_inage):
    
    print('avant :' + list_inage[i])
    list_inage[i] = '<file>images/' + list_inage[i] + '</file>'
    
    i+=1
   # print('appres :'+ list_inage[i])
with open('.\\resources.qrc', '+a') as file:
    
    for i in list_inage:
        file.write(i+ '\n')

print('terminer ... ')