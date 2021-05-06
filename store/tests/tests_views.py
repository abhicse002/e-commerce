# from unittest import skip
#
# from django.http import HttpRequest
# from django.test import TestCase, Client, RequestFactory
# from django.urls import reverse
#
# from store.models import Category,Product
# from django.contrib.auth.models import User
# from django.utils import  timezone
# from store.views import all_products
#
# @skip("demonstrating skipping")
# class TestSkip(TestCase):
#     def test_skip_exmaple(self):
#         pass
#
#
# class TestViewResponses(TestCase):
#     def setUp(self):
#         self.c = Client()
#         self.factory = RequestFactory()
#
#
#         Category.objects.create(name='django', slug='django')
#         User.objects.create(username='admin')
#         self.data1 = Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
#                                                 slug='django-beginners', price='20.00', image='django')
#         self.data2 = Product.objects.create(category_id=2, title='django advanced', created_by_id=1,
#                                                 slug='django-advanced', price='20.00', image='django', is_active=False)
#
#     def test_homepagehtml(self):
#         req = HttpRequest()
#         resp = all_products(req)
#         html = resp.content.decode('utf-8')
#         print(html)
#     def test_url_allowed_hosts(self):
#         """
#         Test allowed hosts
#         """
#
#         response = self.c.get('/')
#         self.assertEqual(response.status_code, 200)
#     #
#     # def test_homepage_url(self):
#     #     """
#     #     Test homepage response status
#     #     """
#     #     response = self.c.get('/')
#     #     self.assertEqual(response.status_code, 200)
#     #
#     # def test_product_list_url(self):
#     #     """
#     #     Test category response status
#     #     """
#     #     response = self.c.get(
#     #         reverse('store:category_list', args=['django']))
#     #     self.assertEqual(response.status_code, 200)
#     #
#     # def test_product_detail_url(self):
#     #     """
#     #     Test items response status
#     #     """
#     #     response = self.c.get(
#     #         reverse('store:product_detail', args=['django-beginners']))
#     #     self.assertEqual(response.status_code, 200)
