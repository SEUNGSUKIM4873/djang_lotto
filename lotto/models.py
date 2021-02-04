from django.db import models
from django.utils import timezone
import random

# Create your models here.
class GuessNumbers(models.Model):
    name = models.CharField(max_length=24)
    text = models.CharField(max_length=255)
    lottos = models.CharField(max_length=255, default='[1, 2, 3, 4, 5, 6]')
    num_lotto = models.IntegerField(default=5)
    update_date = models.DateTimeField()

    def generate(self): #self가 자기자신 행을 의미
        self.lottos = ""
        origin = list(range(1, 46))
        for _ in range(0, self.num_lotto) :
            random.shuffle(origin)
            guess = origin[:6]
            guess.sort()
            self.lottos += str(guess) + '\n'

        self.update_date = timezone.now()
        self.save() #지금까지 수정사항을 저장

    def __str__(self): #str 함수는 조금 설명적으로 보여줌.
        return "pk {} : {} - {}".format(self.pk, self.name, self.text)
        # 제목 부분에 들어가는 것.
        # pk는 id 값
