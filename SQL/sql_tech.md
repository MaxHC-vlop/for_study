# Создание таблицы

```sql
CREATE TABLE book(
    book_id INT PRIMARY KEY AUTO_INCREMENT, 
    title VARCHAR(50),
    author VARCHAR(30),
    price DECIMAL(8, 2),
    amount INT
);
```

# Вставка записи в таблицу

```sql
INSERT book(title, author, price, amount) 
VALUES ('Мастер и Маргарита', 'Булгаков М.А.', 670.99, 3);
```

# Выборка данных

Выбор всех данных :
```sql
SELECT * FROM book;
```
Выборка отдельных столбцов :
```sql
SELECT title, amount FROM book;
```
Выборка новых столбцов и присвоение им новых имен :
```sql
SELECT title AS Название, amount 
FROM book;
```
Выборка данных с созданием вычисляемого столбца
```sql
SELECT title, author, price, amount, 
     price * amount AS total 
FROM book;
```
Выборка данных, вычисляемые столбцы, математические функции ([link](https://docs.microsoft.com/ru-ru/sql/t-sql/functions/mathematical-functions-transact-sql?view=sql-server-ver15)):
```sql
SELECT title, 
    price, 
    ROUND((price*18/100)/(1+18/100),2) AS tax, 
    ROUND(price/(1+18/100),2) AS price_tax 
    /* ROUND - округляет значение x до k знаков после запятой,
    если k не указано – x округляется до целого */
FROM book;
```
Выборка данных, вычисляемые столбцы, логические функции :
```sql
SELECT author, title,
    ROUND(IF(author = 'Булгаков М.А.', price * 1.1, 
    IF(author = 'Есенин С.А.', price * 1.05, price)), 2)
    /* IF 1, *1.1, else *1.05 > new_price */
    AS new_price
FROM book;
```
Выборка данных по условию :
```sql
SELECT title, price 
FROM book
WHERE price < 600;
/* logic operators >, <>(!=), <, <=, >=  */
```
Выборка данных, логические операции :
```sql
SELECT title, author, price, amount
FROM book
WHERE (price < 500 OR price > 600) AND (price * amount >= 5000);

/*
WHERE - включает в себя следущие операции :
Приоритеты операций:
-круглые скобки
-умножение  (*),  деление (/)
-сложение  (+), вычитание (-)
-операторы сравнения (=, >, <, >=, <=, <>)
-NOT
-AND
-OR
*/
```
Выборка данных, операторы BETWEEN, IN :
```sql
SELECT title, author
FROM book
WHERE (price BETWEEN 540.50 AND 800) AND (amount IN (2, 3, 5, 7));
/*
BETWEEN - включает в себя (от x до y)
IN - позволяет выбрать данные, соответствующие значениям из списка
*/
```