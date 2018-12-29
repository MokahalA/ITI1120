def create_books_2Dlist(file_name):
    '''(str) -> list of sublist
    Returns a list containing a sublist with the info
about each book such as:
    date, author, publisher, genre.'''
    
    alc=open(file_name).read().splitlines()
    alt_alc=[]
    new_list=[]

    alt_alc=[]
    for book in alc:
        book=book.split("\t")
        book[0],book[3]= book[3],book[0]
        book[1],book[3]= book[3],book[1]
        book[2],book[3]= book[3],book[2]
        alt_book=(book[0]).split("/")
        alt_book=alt_book[2]+"-"+"0"+alt_book[0]+"-"+alt_book[1]
        book[0]=alt_book
        new_list.append(book)
        books=new_list
    print(new_list)
    
        

#test example

books=create_books_2Dlist("NYT_short.txt")



def search_by_year(books,yr1,yr2):
    books=create_books_2Dlist("NYT_short.txt")
    list_sub=[]
    print(books[0][0])


#test example
search_by_year(books,2005,2005)
