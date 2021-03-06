from django.test import TestCase
from .models import Category, Photo, Location

class CategoryTestClass(TestCase):
    # set up
    def setUp(self):
        self.category = Category(name="Pet")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name="Thika")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

class PhotoTestClass(TestCase):

    # set up method
    def setUp(self):
        '''
        setUp function creates the instance of class Photo
        '''
        self.category = Category.objects.create(name = 'Pet')
        self.location = Location.objects.create(name = 'Thika')
        self.crispus = Photo.objects.create(id = 2, category = self.category, location = self.location, image ='test.jpg', description="Nice pet")
        

    def test_save(self):
        '''
        test-save function is a function for testing to if objects are added successfully to the database or not!
        '''
        self.crispus.save()
        photos = Photo.objects.all()
        self.assertTrue(len(photos) > 0)
    
    def test_get_image_by_id(self):
        '''
        test_get_image_by_id function gets an id of an image and returns the actual image
        '''
        id = 2
        image = self.crispus.get_image_by_id(id)
        photo = Photo.objects.get(id = 2)
        self.assertEqual(photo, image)

    def test_delete(self):
        '''
        test_delete is a function for testing is objects are deleted successfully from the database
        '''
        self.crispus.delete_image()
        photos = Photo.objects.all()
        self.assertEqual(len(photos), 0)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.crispus, Photo))

