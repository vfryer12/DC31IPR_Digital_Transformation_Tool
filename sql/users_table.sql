-- This code is purely for assessment purposes and is not intended for actual implementation in any real-life system.

SELECT * FROM user;

-- Create the user table
CREATE TABLE user(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, 
    username VARCHAR(50) NOT NULL, 
    userpassword BLOB NOT NULL, 
    useremail VARCHAR(50) NOT NULL
);

-- Insert encrypted data
INSERT INTO user (username, userpassword, useremail) VALUES ('user1', AES_ENCRYPT('password', 'encryption_key'), 'user1@example.com');

-- Insert admin user data
INSERT INTO user (username, userpassword, useremail) VALUES ('victoria', AES_ENCRYPT('123', 'encryption_key'), 'victoria@example.com');

-- Query decrypted data
SELECT username, AES_DECRYPT(userpassword, 'encryption_key') as password FROM user WHERE username = 'user1';