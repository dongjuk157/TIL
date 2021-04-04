# DATABASE

[toc]

## Database

### DB 사용 이유

- 데이터 무결성

  - 데이터의 정확성, 일관성, 유효성이 유지 되는 것

  1. 개체 무결성: 모든 테이블이 기본 키로 선택된 필드를 가져야 함.
     - 기본키로 선택된 열은 NULL값이 있으면 안됨
  2. 참조 무결성: 참조 관계에 있는 두 테이블의 데이터가 항상 일관된 값을 갖도록 유지되는 것
     - `ForeignKey` 사용시 `on_delete` 값을 설정하는 이유
  3. 범위(도메인) 무결성: 테이블에 존재하는 필드의 무결성을 보장하기 위한 것
     - 필드타입, NULL값의 허용 등에 대한 사항을 정의하여 올바른 데이터가 입력되었는지를 확인함

- 데이터 무결성의 중요성

  - 합리적인 의사결정
  - 데이터 중복 최소화
  - 데이터 신뢰성

### ACID

데이터베이스 트랜잭션이 안전하게 수행된다는 것을 보장하기 위한 성질을 가리키는 약어

1. Atomicity(원자성): 트랜잭션과 관련된 작업들이 부분적으로 실행되다가 중단되지 않는 것을 보장함
2. Consistency(일관성): 트랜잭션이 실행을 성공적으로 완료하면 언제나 일관성 있는 데이터베이스 상태로 유지함
3. Isolation(고립성): 트랜잭션을 수행 시 다른 트랜잭션의 연산 작업이 끼어들지 못하도록 보장함
4. Durability(지속성): 성공적으로 수행된 트랜잭션은 영원히 반영되어야 함. 로그를 이용해 수행전 상태로 되돌릴수 있음



## SQL (Structured Query Language)

관계형 데이터베이스 관리 시스템(RDBMS, Relational DataBase Management System)의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어

### SQL 용어 및 개념

테이블: 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합

스키마: 관계형 데이터베이스에서 구조와 제약조건에 관련한 전반적인 명세를 기술 한 것

레코드: 단일 구조 데이터 항목을 가리키는 행

컬럼: 고유한 데이터 형식이 지정되는 열

기본키(Primary Key): 각 행의 고유값



### SQL 문법 종류

자세한 명령어 사용법은 BASIC SQLITE tutorial 에서 확인

1. DDL - 데이터 정의 언어, Data Definition Language

   - CREATE: DB, TABLE 생성
   
     ```sqlite
     CREATE TABLE table(
         column1 INTEGER PRIMARY KEY,
         column2 datatype,
         column3 datatype,
         ...,
     );
     ```
   
   - DROP: DB, TABLE 삭제
   
     ```sqlite
     DROP TABLE table;
     ```
   
     - 스키마와 디스크 파일에서 테이블 삭제
   
   - ALTER: TABLE 수정.
   
     ```sqlite
     -- 이름 변경
     ALTER TABLE table RENAME TO new_name;
     
     -- 컬럼 추가
     ALTER TABLE table ADD COLUMN new_column datatype;
     ALTER TABLE table ADD COLUMN new_column datatype DEFAULT value;
     ```
   
   - TRUNCATE: TABLE 내 모든 데이터 삭제
     - 스키마는 남음 - DROP이랑 다른점
     - ID 값까지 초기화 - DML DELETE와 다른점
2. DML - 데이터 조작 언어, Data Manipulation Language

    - INSERT: 데이터 삽입

      ```sqlite
      INSERT INTO table (column1, column2)
      VALUES 
      (value1, value2),
      (value1, value2),
      (value1, value2),
      (value1, value2);
      
      -- column 순서대로 넣을땐 column 명 생략가능
      INSERT INTO table 
      VALUES 
      (value1, value2),
      (value1, value2),
      (value1, value2),
      (value1, value2);
      
      -- column 순서대로 넣지 않을땐 column 명 생략 불가능
      INSERT INTO table (column2, column1) 
      VALUES 
      (value2, value1),
      (value2, value1),
      (value2, value1),
      (value2, value1);
      ```

    - UPDATE: 데이터 수정

      ```sqlite
      UPDATE table SET column1=value1, ... WHERE row_filter;
      ```

    - DELETE: 데이터 삭제

      ```sqlite
      -- 전체 데이터 삭제
      DELETE FROM table;
      
      -- 특정 레코드 삭제
      DELETE FROM table WHERE row_filter;
      ```

      - 전체 데이터를 삭제해도 스키마는 남음
      - 자동으로 증가하는 값(auto increment)은 초기화되지 않음

    - SELECT: 데이터 조회

      ```sqlite
      -- 전체 데이터 조회
      SELECT * FROM table;
      
      -- 특정 데이터 조회
      SELECT (DISTINCT) column_list
      FROM table_list
        JOIN table ON join_condition
      WHERE row_filter
      ORDER BY column
      LIMIT count OFFSET offset
      GROUP BY column
      HAVING group_filter;
      ```

    - REPLACE: 데이터가 있으면 DELETE 후 INSERT, 데이터가 없으면 INSERT

      - UPDATE와 다른점은 DELETE후 INSERT하게 되므로 DB에 원래있던 레코드는 사라짐
      - DB를 복제할때 사용

      

3. DCL - 데이터 제어 언어, Data Control Language

    - GRANT: 특정 데이터베이스 사용자에게 특정 작업의 수행 권한을 부여함.
    - REVOKE: 수행 권한을 박탈함.
    - COMMIT: Transaction 처리가 정상적으로 종료되었을때, 변경된 내용을 DB에 반영함.
    - ROLLBACK: Transaction 처리가 비정상적으로 종료되었을때, 모든 변경 내용을 취소함.



## SQLite 특징

1. Serverless:

   기본적인 RDBMS는 클라이언트(어플리케이션, 커넥터)와 서버(서버프로세스, DB 파일)가 존재하고 그 사이에서 송수신을 담당하는 프로토콜을 사용함.

   SQLite는 server를 사용하지 않아서 클라이언트에서 DB파일에 직접적으로 접근함

2. Self-contained

   OS나 외부 라이브러리로부터 최소한의 지원만 요구하므로 임베디드 장치나 다른 환경에서도 사용가능함.

3. Zero-configuration

   설치가 필요하지 않고, 서버 프로세스가 없어서 configure나 시작, 중지 같은 행동을 수행하지 않아도 됨.

4. Transactional

   transaction이 정상적으로 끝났을 경우에만 변화가 되고, 그 외의 상황에서는 전혀 바뀌지 않음.



## 명령어

### SQLite Commands

 [참고](https://www.sqlitetutorial.net/sqlite-commands/)

`.help`: sqlite에서 사용가능한 명령어 설명

`.databases`: 현재 연결되어있는 모든 DB를 보여줌

`.tables`: 현재 DB에 있는 모든 table을 보여줌.

- `.tables '%es'`: 와일드카드를 사용해서 원하는 table만 확인할수 있음

`.schema TABLE`: 해당 테이블의 스키마를 확인할수 있음

`.indexes`: 현재 DB의 모든 index를 보여줌.

- `.indexes TABLE`: 해당 테이블의 인덱스만 보여줌
- `.indexes '%es'`: 와일드카드 사용 가능



### Basic SQLite tutorial

1. Simple query
   **Select** – query data from a single table using SELECT statement.
   
   사칙연산 가능

   ```sqlite
   SELECT 1 + 1;
   > 2
   ```

   다른 명령어를 조합하여 특정값을 가져올수 있음

   ```sqlite
   SELECT DISTINCT column_list
   FROM table_list
     JOIN table ON join_condition
   WHERE row_filter
   ORDER BY column
   LIMIT count OFFSET offset
   GROUP BY column
   HAVING group_filter;
   ```
   
   뒤에 자세히 설명하겠지만 간단히 설명하자면 다음과 같다.
   
   - `SELECT DISTINCT`: 중복되는 값 제외
   
   - `JOIN` : 다른 테이블을 사용
   
   - `WHERE`: 원하는 row에서 값을 확인
   
   - `ORDER BY`: 결과의 정렬 조건
   
   - `LIMIT`: 결과 값을 어디서부터 몇개 보여줄지 설정
   
   - `GROUP BY`: row를 column을 기준으로 그룹화
   
   - `HAVING`: 그룹에 필터를 적용
   
   
   
2. Sorting rows
   **Order By** – sort the result set in ascending or descending order.

   ```sqlite
   SELECT
      select_list
   FROM
      table
   ORDER BY
       column_1 ASC,
       column_2 DESC;
   ```
   
   - 특정 테이블을 조회할때 column에 따라 정렬 조건을 둘수 있음
   - ASC: 오름차순 (Default)
   - DESC: 내림차순
   
   
   
3. Filtering data

   **Select Distinct** – query unique rows from a table

   - 기본 문법
     
     ```sqlite
     SELECT DISTINCT	select_list
     FROM table;
     ```
     
   - 차이점
     
     | SELECT                                                       | SELECT DISTINCT                                              |
     | ------------------------------------------------------------ | ------------------------------------------------------------ |
     | ![SQLite without DISTINCT](https://cdn.sqlitetutorial.net/wp-content/uploads/2015/11/SQLite-without-DISTINCT.jpg) | ![SQLite DISTINCT example](https://cdn.sqlitetutorial.net/wp-content/uploads/2015/11/SQLite-DISTINCT-example.jpg) |

   

   **Where**  – filter rows of a result set using various conditions.

   - 기본문법

     ```sqlite
     SELECT
     	column_list
     FROM
     	table
     WHERE
     	search_condition;
     ```

   - Search_condition에 사용될수 있는 양식

     ```sqlite
     left_expression COMPARISON_OPERATOR right_expression
     
     -- examples
     WHERE column_1 = 100;
     WHERE column_2 IN (1,2,3);
     WHERE column_3 LIKE 'An%';
     WHERE column_4 BETWEEN 10 AND 20;
     ```

   - Comparison operators

     | Operator | Meaning                  |
     | :------- | :----------------------- |
     | =        | Equal to                 |
     | <> or != | Not equal to             |
     | <        | Less than                |
     | >        | Greater than             |
     | <=       | Less than or equal to    |
     | >=       | Greater than or equal to |

   - Logical operators

     | Operator | Meaning                                                      |
     | :------- | :----------------------------------------------------------- |
     | ALL      | returns 1 if all expressions are 1.                          |
     | AND      | returns 1 if both expressions are 1, and 0 if one of the expressions is 0. |
     | ANY      | returns 1 if any one of a set of comparisons is 1.           |
     | BETWEEN  | returns 1 if a value is within a range.                      |
     | EXISTS   | returns 1 if a subquery contains any rows.                   |
     | IN       | returns 1 if a value is in a list of values.                 |
     | LIKE     | returns 1 if a value matches a pattern                       |
     | NOT      | reverses the value of other operators such as NOT EXISTS, NOT IN, NOT BETWEEN, etc. |
     | OR       | returns true if either expression is 1                       |

   - Examples

     ```sqlite
     -- 1. with AND operator
     SELECT
     	name,
     	milliseconds,
     	bytes,
     	albumid
     FROM
     	tracks
     WHERE
     	albumid = 1
     AND milliseconds > 250000;
     
     -- 2. with LIKE operator
     SELECT
     	name,
     	albumid,
     	composer
     FROM
     	tracks
     WHERE
     	composer LIKE '%Smith%'
     ORDER BY
     	albumid;
     
     -- 3. with IN operator
     SELECT
     	name,
     	albumid,
     	mediatypeid
     FROM
     	tracks
     WHERE
     	mediatypeid IN (2, 3);
     ```

     | Oper. | examples                                                     |
     | ----- | ------------------------------------------------------------ |
     | AND   | ![SQLite WHERE clause comparison operator](https://cdn.sqlitetutorial.net/wp-content/uploads/2015/11/SQLite-WHERE-clause-comparison-operator.jpg) |
     | LIKE  | ![SQLite WHERE with LIKE operator](https://cdn.sqlitetutorial.net/wp-content/uploads/2015/11/SQLite-WHERE-with-LIKE-operator.jpg) |
     | IN    | ![SQLite WHERE with IN operator](https://cdn.sqlitetutorial.net/wp-content/uploads/2015/11/SQLite-WHERE-with-IN-operator.jpg) |




   **Limit** – constrain the number of rows returned by a query and how to get only the necessary data from a table.

   - 기본 문법

      ```sqlite
     SELECT
     	column_list
     FROM
     	table
     LIMIT row_count OFFSET offset;
     ```

   - `row_count` 만큼 반환

   - `offset`: 처음 시작하는 부분. Default 0

   - 둘다 positive integer만 사용 가능

   

   **Like** – query data based on pattern matching using wildcard characters: percent sign (%) and underscore (_).

   - 기본 문법

     ```sqlite
     SELECT
     	column_list
     FROM
     	table_name
     WHERE
     	column_1 LIKE pattern ESCAPE espression;
     ```

   - 와일드 카드

     `%`: 문자열이 있을수도 있고 없을수도 있음

     `_`: 해당자리에 문자가 반드시 존재함

   - ESCAPE: `%`나 `_`가 문자열로 쓰이는 경우 사용

     ```sqlite
     ----------------------
     -- table:t column:c
     -- -------------------
     -- 10% increase          
     -- 10 times decrease     
     -- 100% vs. last year    
     -- 20% increase next year
     
     SELECT c FROM t WHERE c LIKE '%10%%';
     ------------------
     -- 출력 column
     -- ---------------
     -- 10% increase      
     -- 10 times decrease 
     -- 100% vs. last year
     
     SELECT c  FROM t WHERE c LIKE '%10\%%' ESCAPE '\';
     ----------------
     -- 출력 column
     -- ------------
     -- 10% increase     
     ```
     



**Glob** – determine whether a string matches a specific UNIX-pattern.

   - `LIKE` 와 비슷하지만 UNIX wildcard를 사용함

     - `*`: wildcard matches any number of characters. `%` 와 비슷함
     - `?`: wildcard matches exactly one character. `_`와 비슷함
     - `[]`: list wildcard 사용 가능

   - Examples

     ```sqlite
     -- 1 두번째가 'ere'로 시작하는 문자열 조회
     SELECT
     	trackid,
     	name
     FROM
     	tracks
     WHERE
     	name GLOB '?ere*';
     
     -- 2 숫자가 들어있지 않은 문자열 조회
     SELECT
     	trackid,
     	name
     FROM
     	tracks
     WHERE
     	name GLOB '*[^1-9]*';
     ```

     | wildcard   | examples                                                     |
     | ---------- | ------------------------------------------------------------ |
     | `*`, `?`   | ![SQLite GLOB asterisk wildcard containing example](https://cdn.sqlitetutorial.net/wp-content/uploads/2015/12/SQLite-GLOB-asterisk-wildcard-containing-example.jpg) |
     | \[\](list) | ![SQLite GLOB list wildcard characters example](https://cdn.sqlitetutorial.net/wp-content/uploads/2015/12/SQLite-GLOB-list-wildcard-characters-example.jpg) |

   

   **IS NULL** – check if a value is null or not.

   

4. Joining tables

   테이블간 겹치는 부분이 있으면 그 부분을 사용해서 합쳐진 테이블을 조회할수 있음

   테이블 간 관계(1 : N, M : N 등)에서 사용 가능

   **Inner Join** – query data from multiple tables using the inner join clause.

   - 테이블간 겹치는 부분을 엮어서 새로운 테이블로 조회

   - 사용 예제

     ```sqlite
     -- 1
     SELECT
     	trackid,
     	name,
     	title
     FROM
     	tracks
     INNER JOIN albums ON albums.albumid = tracks.albumid;
     
     
     -- 2
     SELECT
         trackid,
         name,
         tracks.albumid AS album_id_tracks,
         albums.albumid AS album_id_albums,
         title
     FROM
         tracks
         INNER JOIN albums ON albums.albumid = tracks.albumid;
         
     -- 3. 3 tables
     SELECT
         trackid,
         tracks.name AS track,
         albums.title AS album,
         artists.name AS artist
     FROM
         tracks
         INNER JOIN albums ON albums.albumid = tracks.albumid
         INNER JOIN artists ON artists.artistid = albums.artistid;
     ```

     |      |                                                              |
     | ---- | ------------------------------------------------------------ |
     | 1    | ![SQLite Inner Join 2 Tables Example](https://cdn.sqlitetutorial.net/wp-content/uploads/2015/12/SQLite-Inner-Join-2-Tables-Example.jpg) |
     | 2    | ![SQLite Inner Join Example](https://cdn.sqlitetutorial.net/wp-content/uploads/2015/12/SQLite-Inner-Join-Example.jpg) |
     | 3    | ![SQLite Inner Join 3 tables](https://cdn.sqlitetutorial.net/wp-content/uploads/2015/12/SQLite-Inner-Join-3-tables.jpg) |

     |      | 테이블간 관계                                                |
     | ---- | ------------------------------------------------------------ |
     | 1, 2 | ![img](https://cdn.sqlitetutorial.net/wp-content/uploads/2018/11/tracks_albums.png) |
     | 3    | ![img](https://cdn.sqlitetutorial.net/wp-content/uploads/2018/11/artists_albums_tracks.png) |

   

   **Left Join** – combine data from multiple tables using the left join clause.

   - 왼쪽에 두는 테이블을 기준으로 새로운 테이블 조회

   - 겹치는 컬럼이 있는 경우 연결하고, 없는 경우 NULL값으로 지정

   - ![SQLite left join example](https://cdn.sqlitetutorial.net/wp-content/uploads/2015/12/SQLite-left-join-example.png)

   -  `RIGHT JOIN`은 지원하지 않음

     

   **Cross Join** – show you how to use the cross join clause to produce a cartesian product of result sets of the tables involved in the join.

   - 사용문법

     ```sqlite
     SELECT name,
            date 
     FROM members
     CROSS JOIN dates;
     ```

   - 사용 예제

     ```sqlite
     CREATE TABLE ranks (
         rank TEXT NOT NULL
     );
     
     CREATE TABLE suits (
         suit TEXT NOT NULL
     );
     
     INSERT INTO ranks(rank) 
     VALUES('2'),('3'),('4'),('5'),('6'),('7'),('8'),('9'),('10'),('J'),('Q'),('K'),('A');
     
     INSERT INTO suits(suit) 
     VALUES('Clubs'),('Diamonds'),('Hearts'),('Spades');
     
     SELECT rank,
            suit
       FROM ranks
            CROSS JOIN
            suits
     ORDER BY suit;
     ```

     | rank | suit  | rank | suit     | rank | suit   | rank | suit   |
     | ---- | ----- | ---- | -------- | ---- | ------ | ---- | ------ |
     | 2    | Clubs | 2    | Diamonds | 2    | Hearts | 2    | Spades |
     | 3    | Clubs | 3    | Diamonds | 3    | Hearts | 3    | Spades |
     | 4    | Clubs | 4    | Diamonds | 4    | Hearts | 4    | Spades |
     | 5    | Clubs | 5    | Diamonds | 5    | Hearts | 5    | Spades |
     | 6    | Clubs | 6    | Diamonds | 6    | Hearts | 6    | Spades |
     | 7    | Clubs | 7    | Diamonds | 7    | Hearts | 7    | Spades |
     | 8    | Clubs | 8    | Diamonds | 8    | Hearts | 8    | Spades |
     | 9    | Clubs | 9    | Diamonds | 9    | Hearts | 9    | Spades |
     | 10   | Clubs | 10   | Diamonds | 10   | Hearts | 10   | Spades |
     | J    | Clubs | J    | Diamonds | J    | Hearts | J    | Spades |
     | Q    | Clubs | Q    | Diamonds | Q    | Hearts | Q    | Spades |
     | K    | Clubs | K    | Diamonds | K    | Hearts | K    | Spades |
     | A    | Clubs | A    | Diamonds | A    | Hearts | A    | Spades |

     - 한줄로 하면 테이블이 너무 길어져서 옆으로 합침

   

   **Self Join** – join a table to itself to create a result set that joins rows with other rows within the same table.

   Follow 기능과 같이 User가 user를 참조하는 경우에 사용

   - 사용예제

     ```sqlite
     -- 1. using INNER JOIN
     SELECT m.firstname || ' ' || m.lastname AS 'Manager',
            e.firstname || ' ' || e.lastname AS 'Direct report' 
     FROM employees e
     INNER JOIN employees m ON m.employeeid = e.reportsto
     ORDER BY manager;
     
     -- 2. using LEFT JOIN
     SELECT m.firstname || ' ' || m.lastname AS 'Manager',
            e.firstname || ' ' || e.lastname AS 'Direct report' 
     FROM employees e
     LEFT JOIN employees m ON m.employeeid = e.reportsto
     ORDER BY manager;
     ```

     | INNER JOIN                                                   | LEFT JOIN                                                    |
     | ------------------------------------------------------------ | ------------------------------------------------------------ |
     | ![SQLite self join example](https://cdn.sqlitetutorial.net/wp-content/uploads/2015/12/SQLite-self-join-example.jpg) | ![SQLite self join with left join example](https://cdn.sqlitetutorial.net/wp-content/uploads/2015/12/SQLite-self-join-with-left-join-example.jpg) |

   

   **Full Outer Join** – show you how to emulate the full outer join in the SQLite using left join and union clauses.

   LEFT JOIN과 RIGHT JOIN을 합친 것

   - Full outer join 설명을 위한 예제

     ```sqlite
     -- create and insert data into the dogs table
     CREATE TABLE dogs (
         type       TEXT,
         color TEXT
     );
     
     INSERT INTO dogs(type, color) 
     VALUES('Hunting','Black'), ('Guard','Brown');
     
     -- create and insert data into the cats table
     CREATE TABLE cats (
         type       TEXT,
         color TEXT
     );
     
     INSERT INTO cats(type,color) 
     VALUES('Indoor','White'), 
           ('Outdoor','Black');
     
     -- FULL OUTER JOIN
     SELECT *
     FROM dogs 
     FULL OUTER JOIN cats
         ON dogs.color = cats.color;
     ----------------------------------
     --  Type	Color	Type	Color
     -- -------------------------------
     --  Hunting	Black	Outdoor	Black
     --  Guard	Brown	NULL	NULL
     --  NULL	NULL	Indoor	White
     ----------------------------------
     ```

   - SQLite에서는 `RIGHT JOIN`과 `FULL OUTER JOIN`을 지원하지 않으므로 `LEFT JOIN`과 `UNION`을 조합해서 사용

     ```sqlite
     SELECT d.type,
              d.color,
              c.type,
              c.color
     FROM dogs d
     LEFT JOIN cats c USING(color)
     UNION ALL
     SELECT d.type,
              d.color,
              c.type,
              c.color
     FROM cats c
     LEFT JOIN dogs d USING(color)
     WHERE d.color IS NULL;
     ```

   

5. Grouping data

   **Group By** – combine a set of rows into groups based on specified criteria. The GROUP BY clause helps you summarize data for reporting purposes.

   **Having** – specify the conditions to filter the groups summarized by the GROUP BY clause.

   평균, 그룹 내 개수 등 데이터를 집계할때 사용. [참고](https://docs.microsoft.com/ko-kr/sql/t-sql/functions/aggregate-functions-transact-sql?view=sql-server-ver15)

   - 사용 문법

     ```sqlite
     SELECT 
         column_1,
         aggregate_function(column_2) 
     FROM 
         table
     GROUP BY 
         column_1,
         column_2;
     HAVING
     	search_condition;
     ```

   - 사용 예제

     ```sqlite
     SELECT
     	albumid,
     	COUNT(trackid)
     FROM
     	tracks
     GROUP BY
     	albumid;
     	
     -- using HAVING clause
     SELECT
     	albumid,
     	COUNT(trackid)
     FROM
     	tracks
     GROUP BY
     	albumid
     HAVING albumid = 1;
     ```

     | No HAVING clause                                             | using HAVING clause                                          |
     | ------------------------------------------------------------ | ------------------------------------------------------------ |
     | ![SQLite HAVING clause with COUNT function](https://cdn.sqlitetutorial.net/wp-content/uploads/2015/12/SQLite-HAVING-clause-with-COUNT-function.jpg) | ![SQLite HAVING with WHERE clause](https://cdn.sqlitetutorial.net/wp-content/uploads/2015/12/SQLite-HAVING-with-WHERE-clause.jpg) |

   

6. Set operators

   **Union** – combine result sets of multiple queries into a single result set. We also discuss the differences between UNION and UNION ALL clauses.

   - 합집합

   - UNION: 중복되는 원소 제거
     - {1,2,3} + {3,4,5} => {1,2,3,4,5}
   - UNION ALL: 중복되는 원소 포함
     - {1,2,3} + {3,4,5} => {1,2,3,3,4,5}

   **Except** – compare the result sets of two queries and returns distinct rows from the left query that are not output by the right query.

   - 차집합: {1,2,3} - {3,4,5} => {1,2}

   **Intersect** – compare the result sets of two queries and returns distinct rows that are output by both queries.

   - 교집합

   

7. Subquery

   **Subquery** – introduce you to the SQLite subquery and correlated subquery.

   - WHERE나 FROM 에 subquery를 주어서 사용할수 있음

   - 사용 예제

     ```sqlite
     -- WHERE subquery
     SELECT customerid,
            firstname,
            lastname
       FROM customers
      WHERE supportrepid IN (
                SELECT employeeid
                  FROM employees
                 WHERE country = 'Canada'
            );
     
     -- FROM subquery
     -- 집계함수를 열에 여러번 적용할때 사용
     SELECT
     	AVG(album.size)
     FROM
     	(
     		SELECT
     			SUM(bytes) SIZE
     		FROM
     			tracks
     		GROUP BY
     			albumid
     	) AS album;
     ```

   

   **Exists operator** – test for the existence of rows returned by a subquery.

   - Subquery가 참인 경우만 포함
   - `EXISTS`가 `IN`보다 subquery의 result set이 클때 빠름. 작으면 `IN`이 더 빠름

   

8. More querying techniques

   **Case** – add conditional logic to the query.

   - 사용 문법

     ```sqlite
     CASE case_expression
          WHEN when_expression_1 THEN result_1
          WHEN when_expression_2 THEN result_2
          ...
          [ ELSE result_else ] 
     END
     ```

   - 사용 예제

     ```sqlite
     -- 1
     SELECT
     	trackid,
     	name,
     	CASE
     		WHEN milliseconds < 60000 THEN
     			'short'
     		WHEN milliseconds > 60000 AND milliseconds < 300000 THEN 'medium'
     		ELSE
     			'long'
     		END category
     FROM
     	tracks;
     ```

     ![SQLite Searched CASE example](https://cdn.sqlitetutorial.net/wp-content/uploads/2015/12/SQLite-Searched-CASE-example.png)



9~17은 지금 안봐도 될듯



## Django ORM과 비교

1. 모든 레코드 조회

   ```python
   # orm
   User.objects.all()
   ```

      ```sql
   -- sql
   SELECT * FROM users_user;
      ```

2. user 레코드 생성

   ```python
   # orm
   User.objects.create(first_name='fisrt', last_name='last', age=20, country='Seoul',phone='010-1234-1234',balance=1000)
   ```

   ```sql
   -- sql
   INSERT INTO users_user VALUES (1,'fist','last',20,'Seoul','010-1234-1234',1000);
   ```

3. 특정 레코드 조회

   - `2` 번 id의 전체 레코드 조회

   ```python
   # orm
   User.obejcts.get(pk=2)
   ```

   ```sql
   -- sql
   SELECT * FROM users_user WHERE id=2;
   ```

4. 특정 user 레코드 수정

   ```python
   # orm
   user = User.objects.get(pk=3)
   user.last_name='Kim'
   user.save()
   ```

   ```sql
   -- sql
   UPDATE users_user
   SET last_name= 'Kim'
   WHERE id=3;
   ```
   
5. 특정 user 레코드 삭제

   ```python
   # orm
   user = User.objects.get(pk=4)
   user.delete()
   ```

   ```sql
   -- sql
   DELETE FROM users_user WHERE id=4;
   ```

6. 특정 조건을 만족시키는 column

   - ORM: `User.objects.filter(조건).values(컬럼이름)`

   ```python
   # orm
   User.objects.filter(age=30).values('first_name')
   User.objects.filter(age=30).values('first_name', 'last_name')
   ```

   ```sql
   -- sql
   SELECT first_name FROM users_user WHERE age=30;
   SELECT first_name, last_name FROM users_user WHERE age=30;
   ```

7. 대소관계

   -  ORM Lookup API - `__gte` , `__lte` , `__gt`, `__lt`

   ```python
   # orm
   User.objects.filter(age__gte=30)
   User.objects.filter(age__lte=20)
   ```

      ```sql
   -- sql
   SELECT * FROM users_user WHERE age >= 30;
   SELECT * FROM users_user WHERE age <= 20
      ```

9. Filter 다수 조건 사용

   ```python
   # orm
   from django.db.models import Q
   User.objects.filter(Q(age=30)| Q(last_name='김'))
   ```

   ```sql
   -- sql
   SELECT * FROM users_user WHERE age = 30 or last_name='김';
   ```

10. 시작, 끝 조건

    - ORM: `__startswith`, `__endswith`
    
     ```python
     # orm
     User.objects.filter(phone__startswith='02-')
     ```
     ```sql
     -- sql
     SELECT * FROM users_user WHERE phone LIKE '02-%';
     ```

11. 정렬

    ```python
    # orm
    User.objects.order_by('-age')[:10].values()
    User.objects.order_by('balance')[:10].values()
    User.objects.order_by('balance','-age')[:10].values()
    ```

       ```sql
    -- sql
    SELECT * FROM users_user ORDER BY age DESC LIMIT 10;
    SELECT * FROM users_user ORDER BY balance LIMIT 10;
    SELECT * FROM users_user ORDER BY balance, age DESC LIMIT 10;
       ```

4. OFFSET

   ```python
   # orm
   User.objects.order_by('-last_name','-first_name')[5]
   ```

      ```sql
   -- sql
   SELECT * FROM users_user ORDER BY last_name DESC, first_name DESC LIMIT 1 OFFSET 5;
      ```
   
   
   
13. Aggregation Function

    1. 전체 평균 나이

          ```python
       # orm
       from django.db.models import Avg
       User.objects.all().aggregate(Avg('age'))
       ```

          ```sql
       -- sql
       SELECT AVG(age) FROM users_user;
          ```

    2. 김씨의 평균 나이

          ```python
       # orm
       from django.db.models import Avg
       User.objects.filter(last_name='김').aggregate(Avg('age'))
       ```

          ```sql
       -- sql
       SELECT AVG(age) FROM users_user WHERE last_name="김";
          ```

    3. 강원도에 사는 사람의 평균 계좌 잔고

       ```python
       # orm
       from django.db.models import Avg
       User.objects.filter(country='강원도').aggregate(Avg('balance'))
       ```

       ```sql
       -- sql
       SELECT AVG(balance) FROM users_user WHERE country='강원도';
       ```

    4. 계좌 잔액 중 가장 높은 값

       ```python
       # orm
       from django.db.models import Max
       User.objects.aggregate(Max('balance'))

       User.objects.order_by('-balance')[0]
       ```

          ```sql
       -- sql
       SELECT MAX(balance) FROM users_user;
          ```

    5. 계좌 잔액 총액

       ```python
       # orm
       from django.db.models import Sum
       User.objects.aggregate(Sum('balance'))
       ```

          ```sql
       -- sql
       SELECT SUM(balance) FROM users_user;
          ```

---

