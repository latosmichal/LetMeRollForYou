from django.test import TestCase
from django.urls import reverse
from bs4 import BeautifulSoup
from parameterized import parameterized

class Roll_tests(TestCase):

    def test_main_view(self):
        url = reverse('roll_main')
        resp = self.client.get(url)
        bs = BeautifulSoup(resp.content, features="html.parser")

        self.assertEqual(url, '/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual('Let Me Roll For You', bs.title.string)

    def test_post_error(self):
        url = reverse('roll_main')
        resp = self.client.post(url)

        self.assertEqual(resp.status_code, 405)

    @parameterized.expand([(i, ) for i in [1, 2, 6, 8, 20]])
    def test_rolled_view(self, k):
        url = reverse('roll_main')
        data = {'k': k}
        resp = self.client.get(url, data)
        bs = BeautifulSoup(resp.content, features="html.parser")
        result = bs.findAll('input', {'class': 'roller'})[0]
        
        self.assertEqual(resp.status_code, 200)
        # self.assertEqual(1, resp.request['REQUEST_METHOD'])
        self.assertIn(result['value'], [str(i) for i in range(1, k+1)])

