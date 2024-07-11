from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from core import actions


class UserTestCase(TestCase):
    def test_user_was_created(self):
        action =  actions.UserAction({
            'username':'teste',
            'email':'teste@email.com',
            'password':'123456'
        }).createUser()
        result_expected = Response(
                    'Perfil criado com sucesso',
                    status=status.HTTP_201_CREATED
                )
        self.assertAlmostEqual(result_expected.status_code, action.status_code)