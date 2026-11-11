books = []
while True:
    print("========== МОЯ БИБЛИОТЕКА ==========")
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Удалить книгу")
    print("4. Редактировать книгу")
    print("5. Найти книгу")
    print("6. Статистика")
    print("7. Выход")
    action = input("выбери действие: ")
    if action == "7":
        print("до свидания")
        break
    elif action == "1":
        name_books = input("введи название книги: ")
        name_author = input("введи имя автора")
        book = {
            "title": name_books,
            "author": name_author
        }
        books.append(book)
        print("книга успешно добавлена!")
    elif action == "2":
        if books == []:
            print("библиотека пока пуста")
        else:
            number = 1
            for book in books:
                print(number, book["title"], "-", book["author"])
                number += 1
    elif action == "3":
        if books == []:
            print("библиотека пуста!")
        else:
            try:
                number_books = input("введи номер книги")
                number_books = int(number_books)
                if number_books < 1:
                    print("неверный номер книги")
                elif number_books > len(books):
                    print("такой книги нет")
                else:
                    index = number_books - 1
                    books.pop(index)
                    print("книга успешна удалена")
            except ValueError:
                print("нужно вводить числа")
    elif action == "4":
        if books == []:
            print("библиотека пуста")
        else:
            try:
                number = 1
                for book in books:
                    print(number, book["title"], "-", book["author"])
                    number +=1 
                choice = input("введи номер книги для редактирования")
            
                choice = int(choice)
                if choice <= 0:
                    print("номер должен быть больше нуля")
                elif choice > len(books):
                    print("такой книги нет")
                else:  
                    index = choice -1
                    book = books[index]
                    print(book["title"])
                    name = input("введи новое название книги: ")
                    book["title"] = name
                    print(book["author"])
                    name_writer = input("введи нового автора: ")
                    book["author"] = name_writer
                    print("книга успешна обнавлена")
            except ValueError:
                print("тут может быть только число")
    eiif action == "5":
        if books == []:
            print("библиотека пустая")
        else:
            nazvanie_books = input("введи название книги: ")
            for book in books:
                if nazvanie_books == book["title"]:
                    print(book["title"], book["author"])
                    break
            else:
                print("книга не найдена")
    elif action == "6":
        if books == []:
            print("библиотека пустая")
        else:
            all_authors = set()
            for book in books:
                all_authors.add((book["author"]))

            print("всего книг: ", len(books))
            print("разных авторов: ", len(all_authors))
                




