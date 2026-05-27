CREATE TABLE products (
  id INTEGER PRIMARY KEY,
  name TEXT,
  stock INTEGER DEFAULT 0
);

-- Do not modify above this line --
INSERT INTO products(id, name, stock)
VALUES  (1,	'Apple',	DEFAULT),
        (2,	'Banana',	DEFAULT),
        (3,	'Orange',	DEFAULT);


-- Do not modify below this line --
SELECT * FROM products;
