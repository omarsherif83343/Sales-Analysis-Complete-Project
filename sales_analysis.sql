CREATE TABLE customers(
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50)
);


INSERT INTO customers VALUES
(1,'Omar','Cairo'),
(2,'Ahmed','Giza'),
(3,'Sara','Alexandria'),
(4,'Mona','Cairo'),
(5,'Ali','Mansoura'),
(6,'Nour','Tanta'),
(7,'Youssef','Giza'),
(8,'Hana','Cairo'),
(9,'Khaled','Alexandria'),
(10,'Laila','Mansoura');

CREATE TABLE products(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

INSERT INTO products VALUES
(1,'Laptop','Electronics',30000),
(2,'Mouse','Electronics',500),
(3,'Keyboard','Electronics',1000),
(4,'Desk','Furniture',4000),
(5,'Chair','Furniture',2500),
(6,'Monitor','Electronics',7000),
(7,'Printer','Electronics',5000),
(8,'Bookshelf','Furniture',3500),
(9,'Tablet','Electronics',12000),
(10,'Lamp','Furniture',800);

CREATE TABLE sales(
    sale_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT
);

INSERT INTO sales VALUES
(1,1,1,1),
(2,2,2,3),
(3,3,3,2),
(4,4,4,1),
(5,5,5,2),
(6,6,6,1),
(7,7,7,1),
(8,8,8,2),
(9,9,9,1),
(10,10,10,4),
(11,1,2,5),
(12,2,3,3),
(13,3,4,2),
(14,4,5,1),
(15,5,1,1),
(16,6,9,2),
(17,7,10,3),
(18,8,6,1),
(19,9,7,2),
(20,10,8,1);









select c.customer_name,p.product_name,s.quantity 
from customers c join sales s join products p
on c.customer_id = s.customer_id
and p.product_id = s.product_id;