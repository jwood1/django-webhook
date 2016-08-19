import simplejson

from django.conf import settings
from django.test import TestCase
from django.test.client import Client

from webhook import WebhookBase


DEBUG = True
ROOT_URLCONF = 'tests'
DATABASES = {'default': {}}
SECRET_KEY = "not so secret"

urlpatterns = [
    url(r'^webhook-receiver', WebhookView.as_view(), name='web_hook'),
]


class WebhookView(WebhookBase):

    def process_webhook(self, data, meta):
        pass


class TestWebhook(TestCase):

  def setUp(self):
      """initialize the Django test client"""
      self.c = Client()
        
  def test_your_test(self):
      python_dict = {
          "eventId": "5c0007",
          "portalId": 999,
          "userEmail": "fake@email.com"
      }
      response = self.c.post('/webhook-receiver/',
                                  json.dumps(python_dict),
                                  content_type="application/json")
