import unittest
from unittest.mock import MagicMock

# Import các class từ file book.py của bạn (giả sử code chính nằm trong book.py)
from book import Book, BookRepository, LibraryService

class TestLibraryService(unittest.TestCase):
    
    def setUp(self):
        # Sử dụng Mock cho BookRepository để cô lập quá trình test Service
        self.mock_repository = MagicMock(spec=BookRepository)
        self.library_service = LibraryService(self.mock_repository)

    def test_add_book_success(self):
        # Trường hợp thêm sách thành công (chưa tồn tại trong CSDL)
        self.mock_repository.find_by_id.return_value = None
        
        result = self.library_service.add_book("B001", "Lập trình Python căn bản", "Nguyễn Văn A")
        
        self.assertEqual(result.book_id, "B001")
        self.assertEqual(result.title, "Lập trình Python căn bản")
        self.assertEqual(result.author, "Nguyễn Văn A")
        self.mock_repository.save.assert_called_once()

    def test_add_book_already_exists(self):
        # Trường hợp sách đã tồn tại trong hệ thống -> Phải ném ngoại lệ ValueError
        existing_book = Book("B001", "Sách cũ", "Tác giả cũ")
        self.mock_repository.find_by_id.return_value = existing_book
        
        with self.assertRaises(ValueError) as context:
            self.library_service.add_book("B001", "Lập trình Python mới", "Nguyễn Văn A")
            
        self.assertEqual(str(context.exception), "Sách đã tồn tại trong hệ thống")
        self.mock_repository.save.assert_not_called()

    def test_add_book_empty_title_or_author(self):
        # Trường hợp thiếu thông tin tên sách hoặc tác giả -> Phải ném ngoại lệ ValueError
        with self.assertRaises(ValueError) as context:
            self.library_service.add_book("B002", "", "Nguyễn Văn A")
            
        self.assertEqual(str(context.exception), "Tên sách và tác giả không được để trống")

if __name__ == '__main__':
    unittest.main()