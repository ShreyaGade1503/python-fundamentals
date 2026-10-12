books = [
    {
        "book_id": 1,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "available": True
    },
    {
        "book_id": 2,
        "title": "Atomic Habits",
        "author": "James Clear",
        "available": True
    },
    {
        "book_id": 3,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "available": True
    }
]


def add_book():
    book_id = int(input("Enter book ID: "))
    for book in books:
        if book['book_id'] == book_id:
            print("A book with this ID already exists.")
            return
    title = input("Enter book title: ")
    author_name = input("Enter book author: ")
    books.append({
        "book_id": book_id,
        "title": title,
        "author": author_name,
        "available": True
    })

def view_books():
    print("Available Books in the library:")
    for book in books:
        print(f"Book Name : {book['title']} \nAuthor Name : {book['author']} \n")

def search_book():
    search_book = input("Enter the book name to search: ")
    for book in books:
        if book['title'] == search_book:
            print(f"Book Name : {book['title']} \nAuthor Name : {book['author']} \n Available : {book['available']}")
            return
    print(f"Book '{search_book}' not found in the library.")

def issue_book():
    issued_book = input("Enter the book name to issue: ")
    for book in books:
        if book['title'] == issued_book and book['available'] == True:
            book['available'] = False
            print(f"You have successfully issued the book: {book['title']}")
            return
    print(f"The book '{issued_book}' is either not available or does not exist in the library.")

def return_book():
    return_book = input("Enter the book name to return: ")
    for book in books:
        if book['title'] == return_book and book['available'] == False:
            book['available'] = True
            print(f"You have successfully returned the book: {book['title']}")
            return
    print(f"The book '{return_book}' is not issued or does not exist in the library.")

def show_available_books():
    for book in books:
        if book['available'] == True:
            print(f"Book Name : {book['title']} \nAuthor Name : {book['author']} \n")

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Show Available Books")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            issue_book()
        elif choice == '5':
            return_book()
        elif choice == '6':
            show_available_books()
        elif choice == '7':
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice! Please try again.")
            

main()