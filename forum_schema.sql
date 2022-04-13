DROP DATABASE IF EXISTS forum;
CREATE DATABASE forum;
USE forum;

CREATE TABLE Users (
	users_id	INT AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    passcode VARCHAR(255) NOT NULL,
    PRIMARY KEY (users_id)
);

CREATE TABLE posts (
	post_id INT AUTO_INCREMENT,
    users_id INT,
    post_title VARCHAR(255) NOT NULL,
    post_comment varchar(255) not null,
    PRIMARY KEY (post_id),
    FOREIGN KEY (users_id) REFERENCES users(users_id) ON UPDATE CASCADE ON DELETE SET NULL
);