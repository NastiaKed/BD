-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2023-09-26 11:10:40.433

-- tables
-- Table: Library
CREATE TABLE Library (
    id int  NOT NULL,
    purchaseDate date  NULL,
    playtime timestamp  NULL,
    user_UserID int  NOT NULL,
    game_GameID int  NOT NULL,
    Transaction_id int  NOT NULL,
    CONSTRAINT Library_pk PRIMARY KEY (id)
);

CREATE INDEX Library_idx_1 ON Library (id);

CREATE INDEX timestamp_library ON Library (playtime);

-- Table: Review
CREATE TABLE Review (
    id int  NOT NULL,
    rating int  NULL,
    reviewText varchar(100)  NULL,
    timestamp timestamp  NULL,
    user_UserID int  NOT NULL,
    game_GameID int  NOT NULL,
    CONSTRAINT Review_pk PRIMARY KEY (id)
);

CREATE INDEX timestamp_review ON Review (timestamp);

-- Table: Transaction
CREATE TABLE Transaction (
    id int  NOT NULL,
    amount int  NULL,
    timestamp timestamp  NULL,
    CONSTRAINT Transaction_pk PRIMARY KEY (id)
);

-- Процедура з курсом
DELIMITER //
CREATE PROCEDURE InsertIntoTransactionWithConversionRate(
    IN id INT,
    IN amount INT,
    IN conversionRate FLOAT
)
BEGIN
    INSERT INTO Transaction(id, amount, timestamp)
    VALUES (id, amount * conversionRate, NOW());
END//
DELIMITER ;


CREATE INDEX timestamp_transaction ON Transaction (timestamp);

-- Table: game
CREATE TABLE game (
    id int  NOT NULL,
    title varchar(80)  NULL,
    description varchar(200)  NULL,
    releaseDate date  NULL,
    developer varchar(100)  NULL,
    publisher varchar(50)  NULL,
    genre varchar(40)  NULL,
    price int  NULL,
    CONSTRAINT game_pk PRIMARY KEY (id)
);

-- Процедура для запису в будь-яку одну таблицю
DELIMITER //
CREATE PROCEDURE InsertIntoGame
    (IN id INT, IN title VARCHAR(80), IN description VARCHAR(200), IN releaseDate DATE, IN developer VARCHAR(100), IN publisher VARCHAR(50), IN genre VARCHAR(40), IN price INT)
BEGIN
    INSERT INTO game(id, title, description, releaseDate, developer, publisher, genre, price)
    VALUES (id, title, description, releaseDate, developer, publisher, genre, price);
END//
DELIMITER ;


-- Процедура для вставки 10 випадкових записів в базу.
DELIMITER //
CREATE PROCEDURE InsertRandomIntoGame()
BEGIN
    DECLARE i INT DEFAULT 0;
    WHILE i < 10 DO
        INSERT INTO game(id, title, description, releaseDate, developer, publisher, genre, price)
        VALUES (i, CONCAT('Game', i), 'This is a random game.', CURDATE(), 'Random Developer', 'Random Publisher', 'Random Genre', RAND() * 100);
        SET i = i + 1;
    END WHILE;
END//
DELIMITER ;


-- Функція, яка викликає агрегатні функції для будь-якої таблиці.
DELIMITER //
CREATE FUNCTION GetGameCount()
RETURNS INT
BEGIN
    RETURN (SELECT COUNT(*) FROM game);
END//
DELIMITER ;




CREATE INDEX game_idx_1 ON game (id);

-- Table: message
CREATE TABLE message (
    id int  NOT NULL,
    content varchar(500)  NULL,
    timestamp timestamp  NULL,
    user_chat_id int  NOT NULL,
    CONSTRAINT message_pk PRIMARY KEY (id)
);

CREATE INDEX timestamp_message ON message (timestamp);

-- Table: user
CREATE TABLE user (
    id int  NOT NULL,
    userName varchar(40)  NULL,
    email varchar(20)  NULL,
    password varchar(10)  NULL,
    dateOfBirth date  NULL,
    profilePicthure int  NULL,
    user_friendship_id int  NOT NULL,
    CONSTRAINT user_pk PRIMARY KEY (id)
);
CREATE INDEX user_id ON user (id);


-- Table: user_chat
CREATE TABLE user_chat (
    user_UserID int  NOT NULL,
    id int  NOT NULL,
    user_id int  NOT NULL,
    CONSTRAINT user_chat_pk PRIMARY KEY (id)
);

-- Table: user_friendship
CREATE TABLE user_friendship (
    id int  NOT NULL,
    user_id int  NOT NULL,
    user_2_id int  NOT NULL,
    CONSTRAINT user_friendship_pk PRIMARY KEY (id)
);

-- Процедура для заповнення основної та проміжної таблиць.
DELIMITER //
CREATE PROCEDURE InsertIntoUserAndUserFriendship
    (IN userId INT, IN userName VARCHAR(40), IN email VARCHAR(20), IN password VARCHAR(10), IN dateOfBirth DATE, IN profilePicthure INT, IN friendshipId INT, IN friendId INT)
BEGIN
    INSERT INTO user(id, userName, email, password, dateOfBirth, profilePicthure, user_friendship_id)
    VALUES (userId, userName, email, password, dateOfBirth, profilePicthure, friendshipId);

    INSERT INTO user_friendship(id, user_id, user_2_id)
    VALUES (friendshipId, userId, friendId);
END//
DELIMITER ;


-- Створення таблиці Favorite Game
CREATE TABLE FavoriteGame (
    id int NOT NULL,
    user_UserID int NOT NULL,
    game_GameID int NOT NULL,
    CONSTRAINT FavoriteGame_pk PRIMARY KEY (id)
);

-- Створення тригера, який перевіряє наявність відповідного запису в таблиці game
DELIMITER //
CREATE TRIGGER check_game_exists
BEFORE INSERT ON FavoriteGame
FOR EACH ROW
BEGIN
    IF NEW.game_GameID NOT IN (SELECT id FROM game) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'This game ID does not exist in the game table';
    END IF;
END//
DELIMITER ;



-- foreign keys
-- Reference: Library_Transaction (table: Library)
ALTER TABLE Library ADD CONSTRAINT Library_Transaction FOREIGN KEY Library_Transaction (Transaction_id)
    REFERENCES Transaction (id);

-- Reference: Library_game (table: Library)
ALTER TABLE Library ADD CONSTRAINT Library_game FOREIGN KEY Library_game (game_GameID)
    REFERENCES game (id);

-- Reference: Library_user (table: Library)
ALTER TABLE Library ADD CONSTRAINT Library_user FOREIGN KEY Library_user (user_UserID)
    REFERENCES user (id);

-- Reference: Review_game (table: Review)
ALTER TABLE Review ADD CONSTRAINT Review_game FOREIGN KEY Review_game (game_GameID)
    REFERENCES game (id);

-- Reference: Review_user (table: Review)
ALTER TABLE Review ADD CONSTRAINT Review_user FOREIGN KEY Review_user (user_UserID)
    REFERENCES user (id);

-- Reference: message_user_chat (table: message)
ALTER TABLE message ADD CONSTRAINT message_user_chat FOREIGN KEY message_user_chat (user_chat_id)
    REFERENCES user_chat (id);

-- Reference: user_chat_user (table: user_chat)
ALTER TABLE user_chat ADD CONSTRAINT user_chat_user FOREIGN KEY user_chat_user (user_UserID)
    REFERENCES user (id);

-- Reference: user_chat_user (table: user_chat)
ALTER TABLE user_chat ADD CONSTRAINT user_chat_user FOREIGN KEY user_chat_user (user_id)
    REFERENCES user (id);

-- Reference: user_friendship_user (table: user_friendship)
ALTER TABLE user_friendship ADD CONSTRAINT user_friendship_user FOREIGN KEY user_friendship_user (user_id)
    REFERENCES user (id);

-- Reference: user_friendship_user (table: user_friendship)
ALTER TABLE user_friendship ADD CONSTRAINT user_friendship_user FOREIGN KEY user_friendship_user (user_2_id)
    REFERENCES user (id);

-- End of file.

