
import json



class Laibaray:
    
    def __init__(self):
        self.path=r"Task_python_library/Src/store_book.json"
        # self.remove_book=None
        
    def add_book(self):
        self.list_book=["Paramhans Yoganand",
                        'rich dad and poor dad',
                        'Effective python',
                        'Bhagwat Gita',
                        'Fluent Python'
                        'Python Crash Course'
                        ]
        with open(self.path,'w') as file:
            json.dump(self.list_book,file,indent=4)
          
    
    def display_book(self):
        print('Avilable This book')
       
        
        with open(self.path,'r') as file:
            print(file.read())
            
class Borrow(Laibaray):        
    def brook_book(self):
        with open(self.path,'r') as file:
            self.load_book=json.load(file)
        
        try:
            
            print()
            while True:
                
                self.name=input('please enter your name: ')
                self.__adar_number=(input('please enter your adar number: '))
                if len(self.__adar_number)==11:
                    if self.__adar_number.isdigit():
                        book_name=input('please enter your book name: ')
                        self.remove_book =book_name
                        

                        self.load_book.remove(self.remove_book) 
                        break
                    else:
                        print('please enter only digit number!') 
                else:
                    print('Enter your correct adar number!')        
                    
                    
            with open(self.path,'w') as file:
                json.dump(self.load_book,file,indent=4) 
            return self.remove_book    
        except Exception as e:
            print('My library is not this book')    

  
    
    def return_book(self):
        with open(self.path,'r') as file:
            self.load_book=json.load(file)
        self.hgh=self.brook_book()    
        while True:
            
            self.name=input('pelase enter your name: ')
            self.__adar_number=(input('please enter your adar number: '))
            if len(self.__adar_number)==11:
                if self.__adar_number.isdigit():
                    
                
                    book_name=input('please enter your book name: ')
                    self.add_book=book_name
                    # self.remove_book =book_name
                    
                    if self.add_book ==  self.hgh:
                        
                        self.load_book.append( self.add_book)
                    else:
                        print('your not go this book!')    
                    # for load in self.load_book:
                        

                    break
                else:
                    print('please enter only digit number!')   
            else:
                print(' Enter your correct adar number!')         
        with open(self.path,'w') as file:
            json.dump(self.load_book,file,indent=4)

                 
# data=Laibaray()
# data.add_book()
# data.display_book()
# data.brook_booK()
# data.display_book()
# data.return_book()
# data.display_book()

