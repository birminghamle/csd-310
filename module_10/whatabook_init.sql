/*
    Title: whatabook.init.sql
    Author: Lathan Birmingham
    Date: 20 September 2022
    Description: WhatABook database initialization.
*/

-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('3240 Wilkinson Blvd, Charlotte, North Carolina 28208');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('The Hunger Games', 'Suzanne Collins', 'The first part of The Hunger Games');

INSERT INTO book(book_name, author, details)
    VALUES('Catching Fire', 'Suzanne Collins', 'The second part of The Hunger Games');

INSERT INTO book(book_name, author, details)
    VALUES('Mockingjay', 'Suzanne Collins', "The third part of The Hunger Games");

INSERT INTO book(book_name, author)
    VALUES('The Ballad of Songbirds and Snakes', 'Suzanne Collins');

INSERT INTO book(book_name, author)
    VALUES('The Art of War', 'Sun Tzu');

INSERT INTO book(book_name, author)
    VALUES("Tao Te Ching", 'Lao Tzu');

INSERT INTO book(book_name, author)
    VALUES('The Book of Five Rings', 'Miyamoto Musashi');

INSERT INTO book(book_name, author)
    VALUES('Bhagavad Gita', 'Sage Vyasa');

INSERT INTO book(book_name, author)
    VALUES('The Tibetan Book of the Dead', 'Padmasambhava');

/*
    insert user records
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Lathan', 'Birmingham');

INSERT INTO user(first_name, last_name)
    VALUES('Kendell', 'Smith');

INSERT INTO user(first_name, last_name)
    VALUES('Benjamin', 'Miller');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Lathan'), 
        (SELECT book_id FROM book WHERE book_name = 'The Hunger Games')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Kendell'),
        (SELECT book_id FROM book WHERE book_name = 'Tao Te Ching')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Benjamin'),
        (SELECT book_id FROM book WHERE book_name = 'The Tibetan Book of the Dead')
    );
