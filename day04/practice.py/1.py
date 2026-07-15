class book:
    def __init__(self, title , author, pages):
        self.title=title
        self.author=author
        self.pages=pages
    def describe(self):
        print(f"{self.title} by {self.author} has {self.pages} pages")

# Create two books
book1 = book("Atomic Habits", "James Clear", 320)
book2 = book("Python Crash Course", "Eric Matthes", 544)

# Call the describe() method
book1.describe()
book2.describe()