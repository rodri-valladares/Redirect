from django.test import TestCase,Client
from django.urls import reverse
from django.test.client import RequestFactory
from django.contrib.auth.models import User

from .models import Redirect


# class RedirectViewTest(TestCase):
    
#     client = Client()
#     def login(self) -> None:
#         return self.client.login(username='test',password='test')

#     def setUp(self) -> None:
#         # Creating test user for fetch endpoint services
#         user = User.objects.create(username='test')
#         user.set_password('test')
#         user.save()
        
#         self.redirect1 = Redirect.objects.create(key="111",url="www.google.com") 
#         self.redirect2 = Redirect.objects.create(key="222",url="www.youtube.com") 
#         self.redirect3 = Redirect.objects.create(key="333",url="www.wikipedia.com") 
#         self.factory = RequestFactory()
        

#     def test_redirect(self):
#         url = reverse('redirect',kwargs={"key":"111"})
#         response = self.client.get(url)

#         self.assertEqual(response.data['key'],self.redirect1.key)
#         self.assertEqual(response.data['url'],self.redirect1.url)

class RedirectModelTest(TestCase):
    
    def setUp(self) -> None:
        pass


    def test_get_redirect(self):

        
        data = Redirect.get_redirect("111")
        self.assertEqual()