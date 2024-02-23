from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Recado, Seguidor

class TesteIndex(TestCase):
    def teste(self):
        u1 = User.objects.create_user(username='u1', password='123123')
        u2 = User.objects.create_user(username='u2', password='123123')
        r1 = Recado.objects.create(titulo='t1', texto='recado 1', autor=u1)
        r2 = Recado.objects.create(titulo='t2', texto='recado 2', autor=u1)
        s1 = Seguidor.objects.create(usuario_seguidor=u2, usuario_seguido=u1)

        login = self.client.login(username='u2', password='123123')
        response = self.client.get(reverse('index'))
        print(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 't1')
        self.assertContains(response, 't2')

