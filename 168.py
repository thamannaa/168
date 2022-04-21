class bookshelf:
    def __init__(self,name,author,price,publishing_year):
        self.book_name=name
        self.book_author=author
        self.book_price=price
        self.book_publishing_year=publishing_year
        
    def add_book(self):
        print("name:"+self.book_name)
        print("author:"+self.book_author)
        print("price:"+str(self.book_price))
        print("publishing_year:"+str(self.book_publishing_year))
        
    def year_since_publish(self):
        years_ago_published=2022-self.book_publishing_year
        print("this book was published "+str(years_ago_published)+" years ago")
        
book1=bookshelf("da vinci code","dan brown",4231,1976)
book1.add_book()
book1.year_since_publish()
book2=bookshelf("akbar and birbal","monisha mukundan",3262,1945)
book2.add_book()
book2.year_since_publish()
        


