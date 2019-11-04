/* Table Users identified by user_id*/
DROP TABLE IF EXISTS users;
CREATE TABLE users(
  card_uid VARCHAR(20) UNIQUE NOT NULL,
  last_name VARCHAR(20) NOT NULL,
  first_name VARCHAR(20) NOT NULL,
  id INTEGER PRIMARY KEY AUTOINCREMENT
);
