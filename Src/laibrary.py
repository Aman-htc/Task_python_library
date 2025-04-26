
import json



class Libaray:
    
    def __init__(self):
        self.path=r"student_registration_task_python/Src/store_book.json"
        
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
    def brook_booK(self):
        with open(self.path,'r') as file:
            self.load_book=json.load(file)
        
        try:
            
            print()
            self.name=input('please enter your name: ')
            self.__adar_number=(input('please enter your adar number: '))
            if len(self.__adar_number)==11:
                if self.__adar_number.isdigit():
                    recive_book=input('please enter your book name: ')

                    self.load_book.remove(recive_book) 
                
                else:
                    print('please enter only digit number!') 
            with open(self.path,'w') as file:
                json.dump(self.load_book,file,indent=4) 
        except Exception as e:
            print('My library is not this book')    

class Return(Libaray):    
    
    def return_book(self):
        with open(self.path,'r') as file:
            self.load_book=json.load(file)
        
        self.name=input('pelase enter your name: ')
        self.__adar_number=(input('please enter your adar number: '))
        if len(self.__adar_number)==11:
            if self.__adar_number.isdigit():
                
            
                book_name=input('please enter your book name: ')

                self.load_book.append(book_name)
            else:
                print('please enter only digit number!')    
        with open(self.path,'w') as file:
            json.dump(self.load_book,file,indent=4)

                 


