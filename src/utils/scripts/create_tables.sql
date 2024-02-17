CREATE TABLE users (
	id INTEGER NOT NULL, 
	email VARCHAR,
    tg_user_id INTEGER,
    access_token VARCHAR,
	created_at DATETIME NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE events (
	id INTEGER NOT NULL, 
	title VARCHAR NOT NULL, 
	description VARCHAR NOT NULL, 
    created_at DATETIME NOT NULL, 
	expired_at DATETIME NOT NULL, 
    notify_at DATETIME NOT NULL,
	owner_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owner_id) REFERENCES users (id)
);
