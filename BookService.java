
public class BookService {

    private BookRepository repository;

    public BookService(BookRepository repository) {
        this.repository = repository;
    }

    public boolean addBook(Book book) {

        if (repository.existsByIsbn(book.getIsbn())) {
            System.out.println("ISBN da ton tai!");
            return false;
        }

        repository.save(book);

        System.out.println("Them sach thanh cong!");
        return true;
    }
}
