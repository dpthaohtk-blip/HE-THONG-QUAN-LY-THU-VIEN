CREATE TABLE Book (
    id INT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    isbn VARCHAR(20) UNIQUE
);