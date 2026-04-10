-- ---------------------------------------------------
-- HBnB Project: Database Schema
-- File: schema.sql
-- ---------------------------------------------------

DROP TABLE IF EXISTS place_amenity;
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS places;
DROP TABLE IF EXISTS amenities;
DROP TABLE IF EXISTS users;

-- ---------------- USERS ----------------
CREATE TABLE users (
    id TEXT PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    is_admin BOOLEAN DEFAULT 0,
    created_at DATETIME,
    updated_at DATETIME
);

-- ---------------- AMENITIES ----------------
CREATE TABLE amenities (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    created_at DATETIME,
    updated_at DATETIME
);

-- ---------------- PLACES ----------------
CREATE TABLE places (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    latitude REAL,
    longitude REAL,
    owner_id TEXT NOT NULL,
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY(owner_id) REFERENCES users(id)
);

-- ---------------- REVIEWS ----------------
CREATE TABLE reviews (
    id TEXT PRIMARY KEY,
    text TEXT NOT NULL,
    user_id TEXT NOT NULL,
    place_id TEXT NOT NULL,
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(place_id) REFERENCES places(id)
);

-- ---------------- PLACE_AMENITY ----------------
CREATE TABLE place_amenity (
    place_id TEXT NOT NULL,
    amenity_id TEXT NOT NULL,
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY(place_id) REFERENCES places(id),
    FOREIGN KEY(amenity_id) REFERENCES amenities(id)
);
