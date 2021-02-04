from django.test import TestCase
from .modles import GuessNumbers
# Create your tests here.
class GuessNumberTestCase(TestCase):
    def test_generate(self):
        g = GuessNumbers(name="Test numbers", text = 'selected numbers')
        g.generate()
        # g.lottos
        print(g.update_date)
        print(g.lottos)

        self.assertTure( len(g.lottos) > 20 )
