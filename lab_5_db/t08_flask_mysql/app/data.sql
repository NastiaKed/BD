INSERT INTO user (id, userName, email, password, dateOfBirth, profilePicthure, user_friendship_id)
VALUES
(1, 'User1', 'user1@example.com', 'password1', '1980-01-01', 101, 1001),
(2, 'User2', 'user2@example.com', 'password2', '1985-02-02', 102, 1002),
(3, 'User3', 'user3@example.com', 'password3', '1990-03-03', 103, 1003),
(4, 'User4', 'user4@example.com', 'password4', '1995-04-04', 104, 1004),
(5, 'User5', 'user5@example.com', 'password5', '2000-05-05', 105, 1005),
(6, 'User6', 'user6@example.com', 'password6', '2005-06-06', 106, 1006),
(7, 'User7', 'user7@example.com', 'password7', '2010-07-07', 107, 1007),
(8, 'User8', 'user8@example.com', 'password8', '2015-08-08', 108, 1008),
(9, 'User9', 'user9@example.com', 'password9', '2020-09-09', 109, 1009),
(10, 'User10', 'user10@example.com', 'password10', '2025-10-10', 110, 1010),
(11, 'User11', 'user11@example.com', 'password11', '2030-11-11', 111, 1011),
(12, 'User12', 'user12@example.com', 'password12', '2035-12-12', 112, 1012),
(13, 'User13', 'user13@example.com', 'password13', '2040-01-13', 113, 1013),
(14, 'User14', 'user14@example.com', 'password14', '2045-02-14', 114, 1014),
(15, 'User15', 'user15@example.com', 'password15', '2050-03-15', 115, 1015);

INSERT INTO game (id, title, description, releaseDate, developer, publisher, genre, price)
VALUES
    (1, 'The Legend of Zelda: Breath of the Wild', 'An action-adventure game for the Nintendo Switch.', '2017-03-03', 'Nintendo', 'Nintendo', 'Action-Adventure', 59),
    (2, 'Red Dead Redemption 2', 'An open-world western action-adventure game.', '2018-10-26', 'Rockstar Games', 'Rockstar Games', 'Action-Adventure', 49),
    (3, 'The Witcher 3: Wild Hunt', 'A role-playing game with a vast open world.', '2015-05-19', 'CD Projekt', 'CD Projekt', 'RPG', 39),
    (4, 'Grand Theft Auto V', 'An open-world action-adventure game.', '2013-09-17', 'Rockstar North', 'Rockstar Games', 'Action-Adventure', 29),
    (5, 'Minecraft', 'A sandbox game that allows players to build and explore.', '2011-11-18', 'Mojang', 'Mojang', 'Sandbox', 20),
    (6, 'Cyberpunk 2077', 'An open-world RPG set in a dystopian future.', '2020-12-10', 'CD Projekt', 'CD Projekt', 'RPG', 49),
    (7, 'Fortnite', 'A battle royale game with building mechanics.', '2017-07-25', 'Epic Games', 'Epic Games', 'Battle Royale', 0),
    (8, 'Among Us', 'A multiplayer social deduction game.', '2018-06-15', 'InnerSloth', 'InnerSloth', 'Social Deduction', 5),
    (9, 'FIFA 22', 'A sports simulation game for soccer fans.', '2021-10-01', 'EA Sports', 'Electronic Arts', 'Sports', 59),
    (10, 'Overwatch', 'A team-based first-person shooter game.', '2016-05-24', 'Blizzard Entertainment', 'Blizzard Entertainment', 'First-Person Shooter', 39),
    (11, 'Animal Crossing: New Horizons', 'A life simulation game for the Nintendo Switch.', '2020-03-20', 'Nintendo', 'Nintendo', 'Life Simulation', 49),
    (12, 'Counter-Strike: Global Offensive', 'A popular multiplayer first-person shooter game.', '2012-08-21', 'Valve', 'Valve', 'First-Person Shooter', 0),
    (13, 'The Elder Scrolls V: Skyrim', 'An open-world RPG set in a fantasy world.', '2011-11-11', 'Bethesda Game Studios', 'Bethesda Softworks', 'RPG', 29),
    (14, 'Call of Duty: Warzone', 'A free-to-play battle royale game.', '2020-03-10', 'Infinity Ward', 'Activision', 'Battle Royale', 0),
    (15, 'Assassins Creed Valhalla', 'An action RPG set in the Viking Age.', '2020-11-10', 'Ubisoft', 'Ubisoft', 'Action RPG', 49);

INSERT INTO Transaction (id, amount, timestamp)
VALUES
    (1, 100, '2023-10-23 09:30:00'),
    (2, 50, '2023-10-22 14:15:00'),
    (3, 75, '2023-10-21 11:45:00'),
    (4, 120, '2023-10-20 10:30:00'),
    (5, 80, '2023-10-19 13:45:00'),
    (6, 95, '2023-10-18 16:15:00'),
    (7, 110, '2023-10-17 09:30:00'),
    (8, 65, '2023-10-16 12:45:00'),
    (9, 75, '2023-10-15 14:30:00'),
    (10, 90, '2023-10-14 15:15:00'),
    (11, 105, '2023-10-13 18:30:00'),
    (12, 70, '2023-10-12 19:45:00'),
    (13, 85, '2023-10-11 11:30:00'),
    (14, 130, '2023-10-10 14:15:00'),
    (15, 55, '2023-10-09 16:00:00');

INSERT INTO Library (id, purchaseDate, playtime, user_UserID, game_GameID, Transaction_id)
VALUES
    (1, '2023-10-23', '2023-10-23 12:00:00', 1, 1, 1),
    (2, '2023-10-22', '2023-10-22 15:30:00', 2, 2, 2),
    (3, '2023-10-21', '2023-10-23 09:45:00', 1, 3, 3),
    (4, '2023-10-20', '2023-10-20 14:30:00', 3, 4, 4),
    (5, '2023-10-19', '2023-10-19 16:45:00', 2, 5, 5),
    (6, '2023-10-18', '2023-10-18 10:15:00', 4, 6, 6),
    (7, '2023-10-17', '2023-10-17 12:00:00', 1, 7, 7),
    (8, '2023-10-16', '2023-10-16 13:30:00', 3, 8, 8),
    (9, '2023-10-15', '2023-10-15 15:45:00', 2, 9, 9),
    (10, '2023-10-14', '2023-10-14 11:00:00', 4, 10, 10),
    (11, '2023-10-13', '2023-10-13 12:45:00', 1, 11, 11),
    (12, '2023-10-12', '2023-10-12 14:30:00', 3, 12, 12),
    (13, '2023-10-11', '2023-10-11 17:15:00', 2, 13, 13),
    (14, '2023-10-10', '2023-10-10 09:30:00', 1, 14, 14),
    (15, '2023-10-09', '2023-10-09 14:45:00', 3, 15, 15);

INSERT INTO Review (id, rating, reviewText, timestamp, user_UserID, game_GameID)
VALUES
    (1, 5, 'Це найкраща гра, яку я коли-небудь грав!', '2023-10-23 14:30:00', 1, 1),
    (2, 4, 'Дуже цікава гра, але є місця для покращень.', '2023-10-22 17:15:00', 2, 2),
    (3, 5, 'Гра дуже весела та захоплююча.', '2023-10-21 10:00:00', 1, 3),
    (4, 4, 'Забавна гра, але графіка могла б бути кращою.', '2023-10-20 15:30:00', 3, 4),
    (5, 3, 'Середня гра, нічого особливого.', '2023-10-19 12:45:00', 2, 5),
    (6, 5, 'Грається дуже легко, рекомендую!', '2023-10-18 09:30:00', 1, 6),
    (7, 4, 'Сильний сюжет і гарний геймплей.', '2023-10-17 14:15:00', 3, 7),
    (8, 5, 'Прекрасна гра, як для любителів серії.', '2023-10-16 16:30:00', 4, 8),
    (9, 2, 'Не сподобалася гра, відсутність інновацій.', '2023-10-15 18:00:00', 2, 9),
    (10, 5, 'Вражаюча гра, весело грати!', '2023-10-14 10:45:00', 1, 10),
    (11, 3, 'Середня гра, не вражає.', '2023-10-13 12:30:00', 4, 11),
    (12, 4, 'Сильна гра, але трохи коротка.', '2023-10-12 15:15:00', 3, 12),
    (13, 5, 'Дуже гарна гра, рекомендую всім!', '2023-10-11 14:30:00', 2, 13),
    (14, 4, 'Гарна гра, але потребує оновлень.', '2023-10-10 11:30:00', 3, 14),
    (15, 5, 'Неймовірна гра, не можу відірватися!', '2023-10-09 13:45:00', 2, 15);

INSERT INTO user_chat (user_UserID, id, user_id)
VALUES
    (1, 1, 2),
    (1, 2, 3),
    (2, 3, 1),
    (2, 4, 5),
    (3, 5, 1),
    (1, 6, 4),
    (2, 7, 3),
    (4, 8, 2),
    (3, 9, 1),
    (1, 10, 5),
    (4, 11, 3),
    (2, 12, 4),
    (1, 13, 2),
    (4, 14, 1),
    (3, 15, 5),
    (2, 16, 4);

INSERT INTO message (id, content, timestamp, user_chat_id)
VALUES
    (1, 'Привіт, як справи?', '2023-10-23 14:30:00', 1),
    (2, 'Добре, дякую! Як ти?', '2023-10-23 14:35:00', 1),
    (3, 'Теж непогано. Що робиш?', '2023-10-23 14:40:00', 2),
    (4, 'Я просто граю в нову гру.', '2023-10-23 14:45:00', 1),
    (5, 'Це дуже весело!', '2023-10-23 14:50:00', 1),
    (6, 'А я вчуся на іспити.', '2023-10-23 14:55:00', 2),
    (7, 'Важко готуватися?', '2023-10-23 15:00:00', 2),
    (8, 'Трохи. Але це важливо.', '2023-10-23 15:05:00', 1),
    (9, 'Звучить складно, але це важливо.', '2023-10-23 15:10:00', 2),
    (10, 'Так, дійсно.', '2023-10-23 15:15:00', 1),
    (11, 'У тебе є якісь плани на вихідних?', '2023-10-23 15:20:00', 2),
    (12, 'Поки нічого конкретного.', '2023-10-23 15:25:00', 1),
    (13, 'Можливо ми можемо вирушити кудись разом.', '2023-10-23 15:30:00', 2);

INSERT INTO user_friendship (id, user_id, user_2_id)
VALUES
    (1, 1, 2),
    (2, 1, 3),
    (3, 2, 3),
    (4, 2, 4),
    (5, 3, 4),
    (6, 1, 5),
    (7, 2, 5),
    (8, 3, 5),
    (9, 4, 5),
    (10, 1, 4),
    (11, 2, 4),
    (12, 3, 4),
    (13, 1, 5),
    (14, 2, 5),
    (15, 3, 5);

