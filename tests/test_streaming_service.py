import unittest
from streaming.streaming_service import StreamingService


class TestR1(unittest.TestCase):

    def setUp(self) -> None:
        self._ss = StreamingService()

    def test_media_type(self):
        self._ss.add_movie("Documentary", 2021, "Moore", 120)
        self._ss.add_tv_show("Sitcom", 1998, 5, 40)
        self.assertEqual("movie", self._ss.get_media_content("Documentary").get_content_type())
        self.assertEqual("tv show", self._ss.get_media_content("Sitcom").get_content_type())

    def test_str_movie(self):
        self._ss.add_movie("Documentary", 2021, "Moore", 120)
        self.assertEqual("Documentary,2021,Moore,120", str(self._ss.get_media_content("Documentary")))

    def test_str_tv_show(self):
        self._ss.add_tv_show("Sitcom", 1998, 5, 40)
        self.assertEqual("Sitcom,1998,5,40", str(self._ss.get_media_content("Sitcom")))

    def test_media_attributes(self):
        self._ss.add_movie("Documentary", 2021, "Moore", 120)
        self._ss.add_tv_show("Sitcom", 1998, 5, 40)

        m1 = self._ss.get_media_content("Documentary")
        tv1 = self._ss.get_media_content("Sitcom")

        self.assertEqual("Documentary", m1.get_title())
        self.assertEqual("Sitcom", tv1.get_title())
        self.assertEqual(2021, m1.get_year())
        self.assertEqual(1998, tv1.get_year())

    def test_media_attributes_multiple(self):
        self._ss.add_movie("Documentary", 2021, "Moore", 120)
        self._ss.add_movie("Thriller", 2004, "Fincher", 188)
        self._ss.add_tv_show("Sitcom", 1998, 5, 40)
        self._ss.add_tv_show("Soap", 2001, 15, 500)

        m1 = self._ss.get_media_content("Documentary")
        m2 = self._ss.get_media_content("Thriller")
        tv1 = self._ss.get_media_content("Sitcom")
        tv2 = self._ss.get_media_content("Soap")

        self.assertEqual("Documentary", m1.get_title())
        self.assertEqual("Thriller", m2.get_title())
        self.assertEqual("Sitcom", tv1.get_title())
        self.assertEqual("Soap", tv2.get_title())

        self.assertEqual(2021, m1.get_year())
        self.assertEqual(2004, m2.get_year())
        self.assertEqual(1998, tv1.get_year())
        self.assertEqual(2001, tv2.get_year())


class TestR2(unittest.TestCase):

    def setUp(self):
        self._ss = StreamingService()
        self._ss.add_movie("Documentary", 2021, "Moore", 120)
        self._ss.add_movie("Thriller", 2004, "Fincher", 188)
        self._ss.add_tv_show("Sitcom", 1998, 5, 40)
        self._ss.add_tv_show("Soap", 2001, 15, 500)

    def test_get_watched_by_user(self):
        self._ss.add_user("User1", 33)
        self._ss.watch("User1", "Documentary")
        self._ss.watch("User1", "Thriller")
        self._ss.watch("User1", "Sitcom")

        contents = [content.get_title() for content in self._ss.get_watched_by_user("User1")]
        self.assertEqual(3, len(contents))
        self.assertTrue("Documentary" in contents)
        self.assertTrue("Thriller" in contents)
        self.assertTrue("Sitcom" in contents)

    def test_get_watched_by_user_year(self):
        self._ss.add_user("User1", 33)
        self._ss.watch("User1", "Documentary")
        self._ss.watch("User1", "Thriller")
        self._ss.watch("User1", "Sitcom")

        contents = [content.get_title() for content in self._ss.get_watched_by_user("User1", 2000)]
        self.assertEqual(2, len(contents))
        self.assertTrue("Documentary" in contents)
        self.assertTrue("Thriller" in contents)

    def test_get_watchers_of_content(self):
        self._ss.add_user("User1", 33)
        self._ss.add_user("User3", 13)

        self._ss.watch("User1", "Sitcom")
        self._ss.watch("User3", "Sitcom")

        users = self._ss.get_watchers_of_content("Sitcom")
        self.assertEqual(2, len(users))
        self.assertTrue("User1" in users)
        self.assertTrue("User3" in users)

    def test_get_watchers_of_content_complex(self):
        self._ss.add_user("User1", 33)
        self._ss.add_user("User2", 23)
        self._ss.add_user("User3", 13)

        self._ss.watch("User1", "Sitcom")
        self._ss.watch("User1", "Thriller")
        self._ss.watch("User2", "Thriller")
        self._ss.watch("User2", "Documentary")
        self._ss.watch("User3", "Sitcom")

        users = self._ss.get_watchers_of_content("Sitcom")
        self.assertEqual(2, len(users))
        self.assertTrue("User1" in users)
        self.assertTrue("User3" in users)

        users = self._ss.get_watchers_of_content("Thriller")
        self.assertEqual(2, len(users))
        self.assertTrue("User1" in users)
        self.assertTrue("User2" in users)

        users = self._ss.get_watchers_of_content("Documentary")
        self.assertEqual(1, len(users))
        self.assertTrue("User2" in users)

    def test_get_emtpy(self):
        self._ss.add_user("User1", 33)
        self._ss.add_user("User2", 23)
        self._ss.watch("User1", "Sitcom")

        self.assertNotEqual([], len(self._ss.get_watchers_of_content("Sitcom")))
        self.assertNotEqual([], len(self._ss.get_watched_by_user("User1")))
        
        self.assertEqual([], self._ss.get_watchers_of_content("Soap"))
        self.assertEqual([], self._ss.get_watched_by_user("User2"))


class TestR3(unittest.TestCase):

    def setUp(self):
        self._ss = StreamingService()
        self._ss.add_movie("Documentary", 2021, "Moore", 120)
        self._ss.add_movie("Thriller", 2004, "Fincher", 188)
        self._ss.add_tv_show("Sitcom", 1998, 5, 40)
        self._ss.add_tv_show("Soap", 2001, 15, 500)

        self._ss.add_user("User1", 33)
        self._ss.add_user("User2", 23)
        self._ss.add_user("User3", 13)
        self._ss.add_user("User4", 26)

    def test_get_avg_movie_rating(self):
        self._ss.add_rating("User1", "Thriller", 2)
        self._ss.add_rating("User2", "Thriller", 5)
        self._ss.add_rating("User2", "Documentary", 3)
        self.assertAlmostEqual(3.5, self._ss.get_avg_content_rating("Thriller"))

    def test_get_avg_user_rating(self):
        self._ss.add_rating("User1", "Thriller", 4)
        self._ss.add_rating("User1", "Sitcom", 5)
        self._ss.add_rating("User2", "Documentary", 3)
        self.assertAlmostEqual(4.5, self._ss.get_avg_user_rating("User1"))

    def test_get_avg_movie_rating_multiple(self):
        self._ss.add_rating("User1", "Thriller", 2)
        self._ss.add_rating("User2", "Thriller", 4)
        self._ss.add_rating("User3", "Thriller", 7)
        self._ss.add_rating("User4", "Thriller", 3)
        self._ss.add_rating("User2", "Documentary", 3)
        self.assertAlmostEqual(3.5, self._ss.get_avg_content_rating("Thriller"))

    def test_get_avg_tv_show_rating(self):
        self._ss.add_rating("User1", "Soap", 1)
        self._ss.add_rating("User2", "Soap", 3)
        self._ss.add_rating("User2", "Thriller", 8)
        self.assertAlmostEqual(4.5, self._ss.get_avg_content_rating("Soap"))


class TestR4(unittest.TestCase):

    def setUp(self):
        self._ss = StreamingService()
        self._ss.add_movie("Documentary", 2021, "Moore", 120)
        self._ss.add_movie("Thriller", 2004, "Fincher", 188)
        self._ss.add_tv_show("Sitcom", 1998, 5, 40)
        self._ss.add_tv_show("Soap", 2001, 15, 500)
        self._ss.add_tv_show("Quiz show", 2012, 4, 150)
        self._ss.add_tv_show("Anime", 1989, 1, 291)

        self._ss.add_user("User1", 33)
        self._ss.add_user("User2", 23)
        self._ss.add_user("User3", 13)
        self._ss.add_user("User4", 53)
        self._ss.add_user("User5", 53)
        self._ss.add_user("User6", 53)

        self._ss.watch("User1", "Sitcom")
        self._ss.watch("User1", "Thriller")
        self._ss.watch("User2", "Thriller")
        self._ss.watch("User2", "Documentary")
        self._ss.watch("User3", "Sitcom")
        self._ss.watch("User4", "Soap")
        self._ss.watch("User4", "Documentary")
        self._ss.watch("User4", "Thriller")

        self._ss.watch("User5", "Quiz show")
        self._ss.watch("User6", "Quiz show")
        self._ss.watch("User5", "Anime")
        self._ss.watch("User6", "Anime")

    def test_get_recommendations_easy(self):
        rec = self._ss.get_recommendations("User3")
        self.assertEqual(["Thriller"], rec)

    def test_get_recommendation_harder(self):
        rec = self._ss.get_recommendations("User1")
        self.assertEqual(2, len(rec))
        self.assertTrue("Soap" in rec)
        self.assertTrue("Documentary" in rec)

    def test_get_recommendation_empty(self):
        rec = self._ss.get_recommendations("User2")
        self.assertNotEqual([], rec)
        rec = self._ss.get_recommendations("User5")
        self.assertEqual([], rec)


class TestR5(unittest.TestCase):

    def setUp(self):
        self._ss = StreamingService()
        self._ss.add_movie("A", 2023, "?", 120)
        self._ss.add_movie("B", 2023, "?", 120)
        self._ss.add_tv_show("C", 2023, 1, 26)
        self._ss.add_movie("D", 2023, "?", 120)
        self._ss.add_movie("E", 2023, "?", 120)
        self._ss.add_tv_show("F", 2023, 1, 26)
        self._ss.add_movie("G", 2023, "?", 120)
        self._ss.add_movie("H", 2023, "?", 120)
        self._ss.add_tv_show("I", 2023, 1, 26)

        self._ss.set_previous_content("A", "B")
        self._ss.set_previous_content("A", "C")
        self._ss.set_previous_content("A", "D")
        self._ss.set_previous_content("B", "I")
        self._ss.set_previous_content("B", "E")
        self._ss.set_previous_content("B", "H")
        self._ss.set_previous_content("C", "F")
        self._ss.set_previous_content("D", "G")

    def _check_watch_list(self, title, prev_titles, watch_list):
        title_idx = watch_list.index(title)
        for pt in prev_titles:
            if watch_list.index(pt) > title_idx:
                return False
        return True

    def test_watch_list_simple(self):
        watch_list = self._ss.get_watch_list("D")
        self.assertEqual(2, len(watch_list))
        self.assertTrue(self._check_watch_list("D", ["G"], watch_list))
        self.assertEqual(["D", "G"], sorted(watch_list))

    def test_watch_list_medium(self):
        watch_list = self._ss.get_watch_list("B")
        self.assertEqual(4, len(watch_list))
        self.assertTrue(self._check_watch_list("B", ["I", "E", "H"], watch_list))
        self.assertEqual(["B", "E", "H", "I"], sorted(watch_list))

    def test_watch_list_hard(self):
        watch_list = self._ss.get_watch_list("A")
        self.assertEqual(9, len(watch_list))
        self.assertTrue(self._check_watch_list("A", ["B", "C", "D"], watch_list))
        self.assertTrue(self._check_watch_list("B", ["I", "E", "H"], watch_list))
        self.assertTrue(self._check_watch_list("D", ["G"], watch_list))
        self.assertTrue(self._check_watch_list("C", ["F"], watch_list))
        self.assertEqual(["A", "B", "C", "D", "E", "F", "G", "H", "I"], sorted(watch_list))
