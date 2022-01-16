# DB_3 - SQL 심화



## 1. Basic Sqlite Aggregate Functions

* #### count 

  * 그룹의 항목 수를 가져옴

  * ```sqlite
    SELECT COUNT(*) FROM users;
    ```

* #### AVG

  * 값 집합의 평균 값을 계산

  * ```sqlite
    SELECT AVG(age) FROM users; --평균나이
    ```

  * ```sqlite
    SELECT AVG(age) FROM users WHERE age >= 40; --40살 이상인 사람들의 평균나이
    ```

* #### MAX, MIN

  * 최대, 최소값을 가져옴

  * ```sqlite
    SELECT MAX(age) FROM users; --MIN함수도 동일하게 구동
    ```

* #### SUM

  * 합산값을 계산

  * ```sqlite
    SELECT SUM(age) FROM users;
    ```

### Examples

```sqlite
SELECT first_name, Max(balance) FROM users;
```

users에서 balance가 가장 높은 값의 경우를 찾아서 first_name과 balance값을 출력한다.



## 2. LIKE

문자열의 패턴 일치를 기반으로 데이터를 조회하는 방법

sqlite는 2가지의 와일드카드를 제공한다



1.  %(percent sign) : 0개 이상의 문자
2.   _ (underscore) : underscore 하나당 정확하게 1개의 단일 문자



### Examples

* 2% : 2로 시작하는 값
* %2 : 2로 끝나는 값
* 1_ _ _ : 1로 시작하는 4자리 값
* 2_ _ % : 2로 시작하는 적어도 3자리 이상의 값



이를 적용하는 SQL 구문은 다음과 같다.

```sqlite
SELECT * FROM 테이블 WHERE 컬럼 LIKE '와일드카드의패턴';
```

```sqlite
SELECT * FROM users WHERE age LIKE '2_'; --나이가 20대 (2x)인 사람들을 조회하는 SQL
```

```sqlite
SELECT * FROM users WHERE phone LIKE '02-%'; --02로 시작하는 전화번호 탐색 
```



## 3. ORDER BY

* 조회 결과를 정렬한다.
* 오름차순 : ASC / 내림차순 : DESC
* SELECT문에 추가하여 사용한다.



### Examples

```sqlite
SELECT * fROM users ORDER BY age ASC LIMIT 10; --나이 어린 순으로 10명을 조회한다.
```

```sqlite
SELECT * fROM users ORDER BY age, last_name ASC LIMIT 10; --나이, 성 순으로 오름차순 상위 10명을 조회
```



## 4. GROUP BY

* 집합 안에 또 다른 요약 행 집합을 만든다.
* SELECT문의 Optional한 절이다.
* 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만든다.
* 문장에 WHERE절이 포함된 경우, 반드시 WHERE절 뒤에 작성해야 함

```sqlite
SELECT 컬럼1, aggregate_function(컬럼2) FROM 테이블 GROUP BY 컬럼1, 컬럼2;
```

```sqlite
SELECT last_name, COUNT(*) FROM users GROUP BY last_name; --성과 성에 대한 개수를 카운트한값을 반환한다.
```



## 5. ALTER TABLE

테이블의 값을 바꾸는 것은 ALTER 구문을 사용하면 된다.

* Table 이름 변경
* Table에 새로운  column 추가
* column 이름 수정(3.25.0버전에서 추가되었다.)

```sqlite 
--새 테이블 생성--
CREATE TABLE articles(
title TEXT NOT NULL
content TEXT NOT NULL
);
```

```sqlite 
--몇 개의 행 추가--
INSERT INTO articles VALUES('1번제목', '1번내용'),('2번제목', '2번내용'), ('2번제목', '2번내용'), ('2번제목', '2번내용');
```

```sqlite
ALTER TABLE 기존테이블 이름 RENAME TO 새로운 테이블 이름

ALTER TABLE articles RENAME TO articles2 -- articles-> articles2
```



