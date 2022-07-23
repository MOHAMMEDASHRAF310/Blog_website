import email
from multiprocessing import set_forkserver_preload
from turtle import title
from urllib import response
from django.test import TestCase
from django.contrib.auth import get_user_model # to reference our active user
from django.urls import reverse
from .models import Post
class BlogTests(TestCase):
    def setUp(self) :
        self.user=get_user_model().objects.create_user(
            username='mohamed',
            password='secret',
            email='test@gmail.com'
        )
        self.post=Post.objects.create(
            title='A good title',
            auther=self.user,
            body='a nice body content'
            
        )
    def test_string_representation(self):
        post=Post(title='A good title')
        self.assertEqual(str(post),post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','A good title')
        self.assertEqual(f'{self.post.auther}','mohamed')
        self.assertEqual(f'{self.post.body}','a nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'a nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_details.html')
        

    def test_post_create_view(self):
        response= self.client.post(reverse('post-new'),{
            'title':'new title',
            'auther':'admin',
            'body':'new body'
        })
        self.assertContains(response,'new title')
        self.assertContains(response,'new body')
        self.assertEqual(response.status_code,200)
    def test_post_update_view(self): # new
        response = self.client.post(reverse('post-edit', args='1'),{
            'title':'Updated title',
            'body':'Updated text',
        })
        self.assertEqual(response.status_code, 302)
    def test_post_delete_view(self):
        response=self.client.get(reverse('post-delete',args='1'))
        self.assertEqual(response.status_code,200)

# Create your tests here.
