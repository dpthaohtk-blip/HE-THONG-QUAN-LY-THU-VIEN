
import java.util.ArrayList;
import java.util.List;

public class BookRepository {

    private List<Book> books = new ArrayList<>();

    // Luu sach
    public void save(Book book) {
        books.add(book);
    }

    // Kiem tra ISBN co ton tai khong
    public boolean existsByIsbn(String isbn) {
        for (Book book : books) {
            if (book.getIsbn().equals(isbn)) {
                return true;
            }
        }
        return false;
    }

    // Lay danh sach sach
    public List<Book> findAll() {
        return books;
    }
}
