class library:
    def __init__(self, name_library):
        self.__books = {}
        self.__name_library = name_library

    def search_book(self, name):
        if name in self.__books:
            print(f"we have {name}")
        else:
            print(f"we don't have {name}")
        
        
    def show_books(self):
        if not self.__books:
            print("library is empty")
            return
        for shomare, (title, author) in enumerate(self.__books.items(),start=1):
            print(f"{shomare}. Title:{title} | Author:{author}")
                    

    def remove_book(self, title):
        if title in self.__books:
            del self.__books[title]
            print(f"the {title} removed the library ")
        else:
            print(f"we don't have {title}")

    def add_book(self, title, author):
        self.__books[title] = author
        print("Successfully added")     


    def __str__(self):
        return f"we are in {self.__name_library}\n{self.__name_library} is a library in my oop programe\nyou can build an infinite number of other libraries here"

