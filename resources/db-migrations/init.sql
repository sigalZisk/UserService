DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    age INT(11) NOT NULL,
    joining_date TIMESTAMP DEFAULT NOW(),
    is_registered BOOLEAN DEFAULT FALSE
);

INSERT INTO users (email, first_name, last_name, address, age) VALUES
    ("danwork@mail.com", "Dan", "Row", "19 ThisStreet , New York", 27),
    ("rinawork@mail.com", "Rina", "Barko", "202 ThisDrive , Jerusalem", 31),
    ("galwork@mail.com", "Guy", "Moleck", "78 ThisLane , Dubai", 49);
