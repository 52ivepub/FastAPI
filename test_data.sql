INSERT INTO hotels(name, location, services, rooms_quantity, image_id) VALUES
('Cosmos Collection Altay', 'Республика Алтай, Майминский район, село Урлу-Аспак, Лесхозная улица, 20', '["WI-FI", "Парковка"]', 10, 4 ),
('Scala', 'Республика Алтай, Майминский район, поселок Барангол, Чуйская улица, 40', '["WI-FI", "Парковка"]', 23, 2 ),
('Ару-кель', 'Республика Алтай, Торрочаский район, село Артыш, Телецкая улица, 33', '["Парковка"]', 30, 3 ),
('Гостиница Сывтыкар', 'Республика Коми, Сыктывкар, Коммунистичекая улица, 67', '["WI-FI", "Парковка", "Тренажерны зал"]', 15, 8 ),
('Palace', 'Республика Коми, Сыктывар, Первомайская улица, 62', '["WI-FI", "Парковка", "Кондиционер"]', 22, 5 ),
('Bridge Resort', 'Поселок городского типа Сириус, Фигурная улица, 45', '["WI-FI", "Парковка", "Кондиционер"]', 27, 7 );


INSERT INTO rooms (hotel_id, name, price, services, image_id) VALUES
(1, 'Улучшенный с терассой и видолм на озеро', 24500, 5 '["Бесплатный WIFI", "Кондиционер"]', 7),
(1, 'Делюкс Плюс', 22450, 10 '["Бесплатный WIFI", "Кондиционер"]', 8),
(2, 'Номер на 2-х человек', 4570, 15 '[]', 9),
(2, 'Номер на 3-х человек', 4350, 8 '[]', 10),
(3, 'Номер полулюкс семейный с 1 двухспальной краватью', 7000, 20 '["Холодильник"]', 11),
(3, '2-комнатный номер люкс комфорт', 9815, 10 '[]', 12),
(4, 'Стандартный двухместный', 4300, 20 '["Бесплатный WIFI", "Холодильник"]', 13),
(4, 'Стандартный двухместный ПЛЮС', 4700, 35 '["Бесплатный WIFI", "Кондиционер", "Ванная комната", "Холодильник"]', 14),
(5, 'Номер страндарт с 2 односпальными кроватями (с завтраком)', 5000, 15 '[]', 16),
(5, 'Номер полулюкс премиум (с завраком)', 8000, 7 '[]', 16),
(6, 'Стандарта (типовой корпус)', 8125, 45 '[]', 17);


INSERT INTO users (email, hashed_password) VALUES
('fedoromoloko.ru', 'tut_budet_hashed_password_1'),
('sharik@moloko.ru', 'tut_budet_hashed_password_2');

INSERT INTO bookings (room_id, user_id, date_from, date_to, price) VALUES
(1, 1, '2023-06-15', '2023-06-30', 24500),
(7, 2, '2023-06-25', '2023-07-10', 4300);
