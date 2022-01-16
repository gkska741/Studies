# Homework Problem_0901

### 1. Model 반영하기

        -> Django가 Model에 생긴 변화를 반영하는 방법 : Migrations

### 2. Model 변경상황 저장하기

        python manage.py migrate
        
        python manage.py sqlmigrate // 
        실제로 넘어가는 SQL문 : CREATE TABLE "articles_article"
        ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULL, "content" text NOT NULL);
        commit;


### 3. Python shell

        -> python manage.py shell_plus


### 4. FIeld type (5가지 이상)

    -> DateField, AutoField CharField, SlugField, TimeField 등



```python

```
