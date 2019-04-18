from django.db import models

#구글 TOP20을 위한 테이블 생성
#key1(정수형, 기본값은 0) : 날짜  , G_Word(문자형, 최대길이 200) : 검색어 , G_Rating(정수형, 기본값은 0) : 누적된 점수
class Receive_Google_Data(models.Model) :
    key1 = models.IntegerField(default=0)
    G_Word = models.CharField(max_length=200)
    G_Rating = models.IntegerField(default=0) 

# 쿼리문을 통해 호출할때 G_Word를 타이틀로 출력시킨다.        
    def __str__(self):
        return self.G_Word

#네이터 TOP20을 위한 테이블 생성
#key1(정수형, 기본값은 0) : 날짜  , N_Word(문자형, 최대길이 200) : 검색어 , N_Rating(정수형, 기본값은 0) : 누적된 점수
class Receive_Naver_Data(models.Model):
    key1 = models.IntegerField(default=0)
    N_Word = models.CharField(max_length=200)
    N_Rating = models.IntegerField(default=0)


# 쿼리문을 통해 호출할때 N_Word를 타이틀로 출력시킨다.
    def __str__(self):
        return self.N_Word

#누락값을 위한 테이블 생성
#key1(정수형, 기본값은 0) : 날짜  , Word(문자형, 최대길이 200) : 누락단어 , Type(문자형, 최대길이 200) : 누락된 값
class Missing_Data(models.Model):
    key1 = models.IntegerField(default=0)
    Word = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)

# 쿼리문을 통해 호출할때 Word를 타이틀로 출력시킨다.
    def __str__(self):
        return self.Word
