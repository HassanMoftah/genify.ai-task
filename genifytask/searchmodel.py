import csv
class user:
     code=0
     items=""
     def __init__(self, var1, var2):
        self.code = var1
        self.items = var2
       
def searchbycode(code):
    my_list = []

    with open("C:\\Users\\Moftah\\django\\mysite\\sub_xgb_new.csv", 'r') as f:
      reader = csv.reader(f)
      for row in reader:
          my_list.append(user(row[0],row[1]))
    i=1
    while(i<len(my_list)):
        if(my_list[i].code==code):
                 return my_list[i].items
        i=i+1         
    return ''   
  
        
          
         
   
   