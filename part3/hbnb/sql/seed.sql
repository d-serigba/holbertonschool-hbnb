-- ---------------------------------------------------
-- HBnB Project: Initial Data Seed
-- File: seed.sql
-- ---------------------------------------------------

-- ------------------ USERS ------------------
-- Création d'un administrateur
INSERT INTO users (id, first_name, last_name, email, password, created_at, updated_at)
VALUES (
    '00000000-0000-0000-0000-000000000001',
    'Admin',
    'User',
    'admin@hbnb.com',
    'admin123',
    datetime('now'),
    datetime('now')
);

-- ------------------ AMENITIES ------------------
INSERT INTO amenities (id, name, description, created_at, updated_at)
VALUES
('11111111-1111-1111-1111-111111111111', 'WiFi', 'Connexion internet sans fil', datetime('now'), datetime('now')),
('22222222-2222-2222-2222-222222222222', 'Piscine', 'Piscine extérieure', datetime('now'), datetime('now')),
('33333333-3333-3333-3333-333333333333', 'Parking', 'Place de parking incluse', datetime('now'), datetime('now')),
('44444444-4444-4444-4444-444444444444', 'Petit-déjeuner', 'Petit-déjeuner offert', datetime('now'), datetime('now'));

-- ------------------ PLACES ------------------
-- Exemple d'une place appartenant à l'admin
INSERT INTO places (id, title, description, price, latitude, longitude, owner_id, created_at, updated_at)
VALUES (
    'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa',
    'Appartement central',
    'Bel appartement au centre-ville',
    100.0,
    48.8566,
    2.3522,
    '00000000-0000-0000-0000-000000000001',
    datetime('now'),
    datetime('now')
);

-- ------------------ PLACE_AMENITY ------------------
-- Lier la place à deux amenities
INSERT INTO place_amenity (place_id, amenity_id)
VALUES
('aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa', '11111111-1111-1111-1111-111111111111'), -- WiFi
('aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa', '22222222-2222-2222-2222-222222222222'); -- Piscine

-- ------------------ REVIEWS ------------------
-- Une review sur cette place par l’admin
INSERT INTO reviews (id, text, user_id, place_id, created_at, updated_at)
VALUES (
    'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb',
    'Super endroit, très propre et confortable!',
    '00000000-0000-0000-0000-000000000001',
    'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa',
    datetime('now'),
    datetime('now')
);
