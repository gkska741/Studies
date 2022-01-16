CREATE TABLE classmates(
id INTEGER PRIMARY KEY,
name TEXT
);

DROP TABLE classmates;

CREATE TABLE classmates(
name TEXT PRIMARY KEY,
age INT,
address TEXT
);

DROP TABLE classmates;
CREATE TABLE classmates(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

INSERT INTO classmates(name, age, address) VALUES ('김길동', 1, '서울');
INSERT INTO classmates(name, age, address) VALUES ('이길동', 2, '서울');
select * from classmates;
INSERT INTO classmates VALUES ('박길동', 3, '서울'); - id값이 없으므로 오류

DROP TABLE classmates;
CREATE TABLE classmates(
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

INSERT INTO classmates VALUES ('홍길동', 30, '서울');
INSERT INTO classmates VALUES ('김철수', 30, '대전');
INSERT INTO classmates VALUES ('이싸피', 30, '광주');
INSERT INTO classmates VALUES ('박삼성', 30, '구미');
INSERT INTO classmates VALUES ('최전자', 30, '부산');
