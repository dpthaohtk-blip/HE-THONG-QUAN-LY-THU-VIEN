class AddBookUI:
    def __init__(self):
        self.title = ""
        self.author = ""

    def show_form(self):
        print("=== GIAO DIỆN THÊM SÁCH MỚI ===")
        self.title = input("Nhập tên sách: ")
        self.author = input("Nhập tên tác giả: ")
        return self.title, self.author

if __name__ == "__main__":
    ui = AddBookUI()
    book_title, book_author = ui.show_form()
    print(f"Đã nhập thông tin sách: '{book_title}' - Tác giả: {book_author}")