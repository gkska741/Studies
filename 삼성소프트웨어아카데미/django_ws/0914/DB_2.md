# DB_2 - SQL 기초 

## SQL이란?

![](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fch7rQ4%2FbtqWKiRyrwG%2FRDuJmTUtHgO0mujPDUXNrK%2Fimg.jpg)



* 관계형 데이터베이스의 데이터 관리를 위해 고안된 특수 목적 프로그래밍 언어
* DB 스키마 생성 및 수정
* 자료의 검색 및 관리
* DB 객체 접근 조정을 관리



## SQL 분류



|                           분류                           |                          개념                          |             예시             |
| :------------------------------------------------------: | :----------------------------------------------------: | :--------------------------: |
|  DDL - 데이터 정의 언어<br />(Data Definition Language)  |         관계형 데이터베이스를 정의하는 명령어          |      CREATE/DROP/ALTER       |
| DML - 데이터 조작 언어<br />(Data Manipulation Language) |   데이터를 저장, 조회, 수정, 삭제하는 명령어의 집합    | INSERT/SELECT/UPDATE/DELETE  |
|    DCL - 데이터 제어 언어<br/>(Data Control Language)    | 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어 | GRANT/REVOKE/COMMIT/ROLLBACK |



## SQL 명령어



### CREATE

테이블을 생성한다.

```sqlite
CREATE TABLE classmates(
name INTEGER PRIMARY KEY,
age INT
);
```

(필드의 이름, 필드의 데이터 타입) 형태로 쓴 뒤, PRIMARY KEY 등의 추가적인 설정을 적는다. 각 정보는 콤마(,)로 구분한다.

위의 코드는 id와 name으로 구성된 테이블을 만드는 쿼리이다.

### DROP

특정 테이블을 삭제한다.

```sqlite
DROP TABLE classmates
```

### INSERT

테이블에 단일 행을 삽입한다.

```sqlite
INSERT INTO 테이블이름 (컬럼1, 컬럼2, 컬럼3, ...) VALUES (값1, 값2, 값3, ...);
```

위의 classmates테이블에 적용하면 다음과 같이 쓸 수 있다.

```sqlite
INSERT INTO classmates(name, age) VALUES('홍길동', 23);
INSERT INTO classmates(name, address, age) VALUES('박주윤', '광주', 27);

```

빈값을 방지하기 위해 NOT NULL값을 추가할 수 있다. classmates를 지우고 다시 만들어 보자.

```sqlite
DROP TABLE classmates;
CREATE TABLE classmates(
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL,
)
```

## SELECT 

테이블에서 데이터를 조회한다

다양한 절(clause)와 함께 사용된다 

* #### LIMIT : 반환되는 행 수를 제한한다.

* #### WHERE : 검색 조건을 지정한다

* #### DISTINCT : SELECT절 뒤에 오며 조회 결과에서 중복을 제거한다.



#### SELECT문 적용1 - LIMIT

SELECT문은 다음과 같은 기본형을 가진다.

```sqlite
SELECT 컬럼1, 컬럼2, ... FROM 테이블이름;
```

원하는 수 만큼 데이터를 조회하고 싶으면 LIMIT키워드를 넣는다.

```sqlite
SELECT 컬럼1, 컬럼2, ... FROM 테이블이름 LIMIT 숫자;
```

원하는 수만큼 데이터를 건너뛰고 싶으면

```sqlite
SELECT 컬럼1, 컬럼2, ... FROM 테이블이름 LIMIT 숫자 OFFSET 숫자;
```



#### SELECT문 적용2 - WHERE, DISTINCT

where 조건절의 적용은 다음과 같다.

```sqlite
SELECT 컬럼1, 컬럼2, ... FROM 테이블이름 WHERE 조건;
```

위의 구문은 컬럼1, 컬럼2, ...에서 조건에 부합하는 컬럼에 해당하는 행만 반환하여 출력한다.



중복을 제거하고 싶다면 DISTINCT를 추가하여 작성한다.

```sqlite
SELECT DISTINCT 컬럼 FROM 테이블
```

```sqlite
SELECT DISTINCT age FROM classmates;
```



## DELETE

테이블에서 행을 제거한다.

```sqlite
DELETE FROM 테이블이름1 WHERE 조건;
```

DELETE문의 특징중 하나는 중간의 값을 삭제 후 새 값을 INSERT할 경우 새 컬럼에 삽입된다는 점이다.

예를 들어 5개의 행 정보가 있을때, 3번 행의 정보를 삭제한 후 새로운 값을 INSERT하면 rowid는 1, 2, 4, 5, 6번으로 나타낼 수 있다.

기본적으로 SQLITE는 AUTOINCREMENT라는 속성을 통해 이전에 삭제된 행의 값을 재사용하는 것을 방지한다.

```sqlite
CREATE TABLE 테이블이름(
id INTEGER PRIMARY KEY AUTOINCREMENT,
...	    
);
```

위와 같은 형태로 적용할 수 있다.



## UPDATE

기존 행의 데이터를 수정하는 명령어이다.

```sqlite
UPDATE 테이블이름 SET 컬럼1=값1, 컬럼2=값2, ... WHERE 조건;
```

보통 조건은 단일 행을 반환하는 rowid를 기준으로 많이 사용한다. rowid를 사용하는 이유는 중복이 불가능한(UNIQUE)값이기 때문이다.



<hr>



## WHERE 심화

연습을 하기 위해 다음과 같은 테이블을 만든다.

```sqlite
CREATE TABLE users(
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
country TEXT NOT NULL,
Phone TEXT NOT NULL,
balance INTEGER NOT NULL
);
.tables
.schema users
```

미리 준비해 둔 csv파일을 테이블에 IMPORT한다.

```sqlite
.mode csv
.import users.csv users
.tables
```

테이블에서 age가 45이상인 유저만 조회하려면 다음과 같이 작성할 수 있다.

```sqlite
.mode column	
.headers on
SELECT rowid, * FROM users WHERE age >= 45;
```

