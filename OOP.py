class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} 已借出。"
        else:
            return f"{self.title} 已經被借出。"

    def check_in(self):
        if self.checked_out:
            self.checked_out = False
            return f"{self.title} 已歸還。"
        else:
            return f"{self.title} 尚未被借出。"

    def __str__(self):
        return f"書名：{self.title}, 作者：{self.author}, ISBN：{self.ISBN}, 借出狀態：{'已借出' if self.checked_out else '可借閱'}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)


# 創建書籍物件
book1 = Book("Python基礎教程", "John Smith", "978-1234567890")
book2 = Book("物件導向程式設計", "Jane Doe", "978-0987654321")

# 創建圖書館物件
library = Library()

# 將書籍添加到圖書館
library.add_book(book1)
library.add_book(book2)

# 列印圖書館中的書籍列表
print("圖書館中的書籍：")
library.list_books()

# 借出一本書
print("\n借出書籍：")
print(book1.check_out())

# 再次列印書籍列表，以顯示書籍的狀態
print("\n更新後的書籍列表：")
library.list_books()

# 歸還一本書
print("\n歸還書籍：")
print(book1.check_in())

# 再次列印書籍列表，以顯示書籍的狀態
print("\n更新後的書籍列表：")
library.list_books()
