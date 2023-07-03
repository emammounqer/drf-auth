from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Anime


# Create your tests here.

class AnimeTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username='testuser1', password='pass')
        testuser1.save()

        test_thing = Anime.objects.create(
            name='flower', owner=testuser1, desc="test desc ...")
        test_thing.save()

    def test_animes_model(self):
        anime = Anime.objects.get(id=1)
        actual_owner = str(anime.added_by)
        actual_name = str(anime.name)
        actual_desc = str(anime.desc)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "flower")
        self.assertEqual(actual_desc, "test desc ...")
