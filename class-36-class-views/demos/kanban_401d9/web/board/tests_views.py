from django.test import TestCase, Client
from ..kanban_project.factories import CategoryFactory, CardFactory, UserFactory


class TestCategoryViews(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('secret')
        self.user.save()
        self.c = Client()

    def test_denied_if_no_login(self):
        res = self.c.get('/board/category', follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'class="login-form container"', res.content)

    def test_view_list_when_logged_in(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )

        category = CategoryFactory(user=self.user)
        res = self.c.get('/board/category')

        self.assertIn(category.name.encode(), res.content)

    def test_lists_only_owned_categories(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )

        own_category = CategoryFactory(user=self.user)
        other_category = CategoryFactory()

        res = self.c.get('/board/category')

        self.assertIn(own_category.name.encode(), res.content)
        self.assertNotIn(other_category.name.encode(), res.content)

    def test_cards_listed_in_view(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )
        category = CategoryFactory(user=self.user)
        card = CardFactory(category=category)
        res = self.c.get('/board/category')

        self.assertIn(card.title.encode(), res.content)


class TestCardViews(TestCase):
    pass


class TestCategoryCreateViews(TestCase):
    """."""

    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('super_secret')
        self.user.save()
        self.c = Client()

    def test_new_category_view(self):
        self.c.login(
            username=self.user.username,
            password='super_secret'
        )

        res = self.c.get('/board/category/new')

        self.assertEqual(res.status_code, 200)
        self.assertIn(b'input type="submit"', res.content)
        self.assertIn(b'name="name"', res.content)
        self.assertIn(b'name="description"', res.content)

    def test_create_view_adds_new_category(self):
        self.c.login(
            username=self.user.username,
            password='super_secret'
        )

        form_data = {
            'name': ' Name thing',
            'description': 'this is description'
        }

        res = self.c.post('/board/category/add', form_data, follow=True)


        self.assertIn(b'Name thing', res.content)

