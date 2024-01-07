-- In the SQL extension file, were gonna run our commands and querys

-- First we're going to CREATE the Table Users whith 3 columns for each entry
-- CREATE Table USERS(username TEXT NOT NULL PRIMARY KEY,
-- password NOT NULL,email NOT NULL);

-- Next were gonna INSERT some entries to the DB
-- Insert into USERS (username, password,email)
-- VALUES("Thomas","Thomas1221","ThommyK@gmail.com");

-- The SELECT keyword lets you retrive data from the DB 
-- select username,email from USERS
-- WHERE username= "Jake";

-- The WHERE, IN keywords makes it so we can specify which colmns are we interested
-- and wich values are we looking for exactly.
-- SELECT email from USERS where username in("Jake","Kevin");

-- The LIKE keyword allows us to do some fuzzy search into the DB
-- The % is the basis for all the fuzzy search so it will be of great importance 
-- if theres "J%" then it will look up for eveything that contains J as the first letter
-- SELECT email FROM USERS WHERE username LIKE("J%");

-- if theres "%mm%" then it will look up for all the entries that have "mm" anywhere in the string
-- Select email from users where email like ("%mm%");

-- if theres "%m" it will look up for all of the entries that end with m
-- SELECT email from USERS where email like ("%m");

-- The UPDATE keyword lets us rewrite some information into the DB 
-- UPDATE USERS SET email = "RewritingEMAIL@email.com", password = "rewritingPassword" WHERE username LIKE ("j%");

-- The DELETE keyword lets us remove entries from the DB
-- DELETE FROM USERS WHERE username = "Dog";

-- SELECT * from USERS;

SELECT * FROM customers;