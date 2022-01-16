# Homework Problem_0902

## 1)models.py

    - python manage.py makemigrations
    - python manage.py migrate

## 2) 정답 : 3

## 3) 정답 : 2(음수는 인덱싱이 되지 않음)


## 4) POST의 저장


    article = Post.objects.get(pk=pk)
    article.title = '안녕하세요'
    article.content = '반갑습니다'
    article.save()


## 5) QuerySet형태로 반환하기 위한 함수

    posts = Post.objects.all()


```python

```
