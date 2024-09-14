class Book:
    all_books = []
    
    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)
    
    def contracts(self):
        # Returns a list of contracts associated with this book
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        # Returns a list of authors associated with this book through contracts
        return [contract.author for contract in Contract.all if contract.book == self]


class Author:
    all_authors = []
    
    def __init__(self, name):
        self.name = name
        Author.all_authors.append(self)
    
    def contracts(self):
        # Returns a list of contracts associated with this author
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        # Returns a list of books associated with this author through contracts
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        # Creates a new contract for this author and the specified book
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        # Calculates total royalties earned by this author
        return sum(contract.royalties for contract in Contract.all if contract.author == self)


class Contract:
    all = []
    
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, (int, float)):
            raise Exception("royalties must be a number")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        # Return a list of contracts where the date matches the given date
        return [contract for contract in cls.all if contract.date == date]
