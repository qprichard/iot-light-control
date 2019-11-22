/* Table Users identified by user_id*/
DROP TABLE IF EXISTS users;
CREATE TABLE users(
  card_uid VARCHAR(20) UNIQUE NOT NULL,
  last_name VARCHAR(20) NOT NULL,
  first_name VARCHAR(20) NOT NULL,
  login VARCHAR(8) UNIQUE NOT NULL,
  password VARCHAR(20) NOT NULL,
  id INTEGER PRIMARY KEY AUTOINCREMENT
);

/*Table authentication tokens*/
DROP TABLE IF EXISTS tokens;
CREATE TABLE tokens(
  token VARCHAR(100) NOT NULL
);

/*Table log authentication try*/
DROP TABLE IF EXISTS auth_log;
CREATE TABLE auth_log(
  card_uid VARCHAR(20) NOT NULL,
  log_date DATETIME NOT NULL,
  id INTEGER PRIMARY KEY AUTOINCREMENT
);
