from django.test import SimpleTestCase
from django.urls import reverse, resolve
from newsblog.views import PostView, AddView, EditView, Delete,PostDetail, PostLike


class TestUrls(SimpleTestCase):
    def test_post_view(self):
        url = reverse('post_view')
        self.assertEquals(resolve(url).func.view_class, PostView)
    
    def test_add_view(self):
        url = reverse('add')
        self.assertEquals(resolve(url).func.view_class, AddView)
    
    #def test_edit_view(self):
     #   url = reverse('edit', args=['some-pk'])
      #  self.assertEquals(resolve(url).func.view_class, EditView)
    
    def test_post_detail_view(self):
        url = reverse('post_detail', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, PostDetail)
    
    def test_post_like_view(self):
        url = reverse('post_like', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, PostLike)
    
   
    
    


