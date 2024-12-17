
bookColection = [
    {
        "author": "<NAME>",
        "bookName":"<BookNAME>",
        "genre":"<Genre>",
        "dataTime":"<2000>",
        "countPages":"100",
        "editions":"<EditionsName>",
    }
]

def addBookColection(bookColection):
    author = input("input your author: ")
    bookName = input("input your bookName: ")
    genre = input("input your genre: ")
    dataTime = input("input your dataTime: ")
    countPages = input("input your countPages: ")
    editions = input("input your editions: ")
    bookColection.append({
        "author":author,
        "bookName":bookName,
        "genre":genre,
        "dataTime":dataTime,
        "countPages":countPages,
        "editions":editions
    })
    showBookColection(bookColection)

def showBookColection(bookColection):
    for item in bookColection:
        print(item)

def deleteBookColection(bookColection):
    bookColectionName = input("Input the name of the bookColection to delete: ")
    for item in bookColection:
        if item["author"] == bookColectionName:
            bookColection.remove(item)
            print(f"bookColection '{bookColectionName}' has been deleted.")
            return
    print(f"bookColection '{bookColectionName}' not found.")

def searchBookColection(bookColection):
    bookColectionName = input("Input the name of the bookColection to search: ")
    for item in bookColection:
        if item["author"] == bookColectionName:
            print(f"bookColection '{bookColectionName}' has been found.")
            print(f"bookColection '{item['author']}',{item['bookName']},{item['genre']}',{item['dataTime']},{item['countPages']},{item['editions']}')")
            return

def changeBookColection(bookColection):
    bookColectionName = input("Input the name of the bookColection to change: ")
    for item in bookColection:
        if item["author"] == bookColectionName:
            new_author = input("input your author: ")
            new_bookName = input("input your bookName: ")
            new_genre = input("input your genre: ")
            new_dataTime = input("input your dataTime: ")
            new_countPages = input("input your countPages: ")
            new_editions = input("input your editions: ")
            item["name"] = new_author
            item["phone"] = new_bookName
            item["email"] = new_genre
            item["post"] = new_dataTime
            item["numberRoom"] = new_countPages
            item["skype"] = new_editions
            print(f"bookColection '{bookColectionName}' has been changed.")
            print(f"bookColection '{item['author']}',{item['bookName']},{item['genre']}',{item['dataTime']},{item['countPages']},{item['editions']}')")




addBookColection(bookColection)
addBookColection(bookColection)
searchBookColection(bookColection)
changeBookColection(bookColection)
deleteBookColection(bookColection)