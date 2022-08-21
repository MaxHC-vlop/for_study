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
Выборка данных с сортировкой :
```sql
SELECT author, title
FROM book
WHERE amount BETWEEN 2 AND 14
ORDER BY author DESC, title ASC;
/*
ORDER BY - сортировка по выбранным столбцам
DESC - по убыванию
ASC - по возрастанию
*/
```
Выборка данных, оператор LIKE :
```sql
SELECT title, author
FROM book
WHERE title LIKE "_%_%" AND author LIKE "%С.%"
ORDER BY title;
/*
_ - любой один символ
% - любая, неограниченная последовательность символов
*/
```

# Запросы, групповые операции
Выбор уникальных элементов столбца :
```sql
SELECT DISTINCT amount
FROM book;
```
Выборка данных, групповые функции SUM и COUNT :
```sql
SELECT
    author AS Автор,
    COUNT(DISTINCT title) AS Различных_книг,
    SUM(amount) AS Количество_экземпляров
FROM book
GROUP BY author;
/*
COUNT(имя_столбца) - возвращает количество записей конкретного столбца
SUM(имя_столбца) - считает сумму элементов определенной группы
*/
```
Выборка данных, групповые функции MIN, MAX и AVG :
```sql
SELECT
    DISTINCT author,
    MIN(price) AS Минимальная_цена,
    MAX(price) AS Максимальная_цена,
    AVG(price) AS Средняя_цена
FROM book
GROUP BY author;
/* MIN, MAX, AVR - минимум, максимум, среднее  */
```
Выборка данных c вычислением, групповые функции :
```sql
SELECT
    DISTINCT author,
    SUM(price * amount) AS Стоимость,
    ROUND(SUM(price * amount) * 0.18 / 1.18,2) AS НДС,
    ROUND((SUM(price * amount))-(ROUND(SUM(price * amount) * 0.18 / 1.18,2)),2) AS Стоимость_без_НДС
FROM book
GROUP BY author;
```
Вычисления по таблице целиком :
```sql
SELECT
    MIN(price) AS Минимальная_цена,
    MAX(price) AS Максимальная_цена,
    ROUND(AVG(price), 2) AS Средняя_цена
FROM book;
```
Выборка данных по условию, групповые функции :
```sql
SELECT
    ROUND(AVG(price),2) AS Средняя_цена,
    ROUND(SUM(price * amount),2) AS Стоимость
FROM book
WHERE amount BETWEEN 5 AND 14;
```
Выборка данных по условию, групповые функции, WHERE и HAVING :
```sql
SELECT
    author,
    SUM(amount * price) AS Стоимость
FROM
    book
WHERE
    title NOT IN ('Белая_гвардия','Идиот')
GROUP BY
    author
HAVING
    SUM(amount * price) > 5000
ORDER BY
    SUM(amount * price) DESC;

/*

*/
```