from unittest import TestCase

from data_capture.data_capture import DataCapture, Stats


class TestDataCapture(TestCase):
    def setUp(self) -> None:
        self.data_capture = DataCapture()

    def test_data_capture_init(self):
        self.assertEqual(self.data_capture.data, [])
        self.assertIsNone(self.data_capture.stats)
    
    def test_add_positive_element_to_input(self):
        self.data_capture.add(3)
        self.data_capture.add(5)
        self.assertEqual(self.data_capture.data, [3, 5])
    
    def test_add_non_positive_element_should_fail(self):
        self.data_capture.add(0)
        self.assertEqual(self.data_capture.data, [])
    
    def test_add_negative_element_should_fail(self):
        self.data_capture.add(0)
        self.assertEqual(self.data_capture.data, [])
    
    def test_build_stats_return_stats(self):
        self.data_capture.add(3)
        stats = self.data_capture.build_stats()
        self.assertTrue(isinstance(stats, Stats))
    
    def test_build_stats_return_none_to_no_input(self):
        stats = self.data_capture.build_stats()
        self.assertIsNone(stats)


class TestStats(TestCase):
    def setUp(self) -> None:
        self.data_capture = DataCapture()
        self.data_capture.add(3)
        self.data_capture.add(9)
        self.data_capture.add(3)
        self.data_capture.add(4)
        self.data_capture.add(6)
        self.stats = self.data_capture.build_stats()

    def test_stats_less(self):
        self.assertEqual(self.stats.less(-10), 0)
        self.assertEqual(self.stats.less(0), 0)
        self.assertEqual(self.stats.less(4), 2)
        self.assertEqual(self.stats.less(3), 0)
        self.assertEqual(self.stats.less(9), 4)
        self.assertEqual(self.stats.less(10), 5)

    
    def test_stats_greater(self):
        self.assertEqual(self.stats.greater(4), 2)
        self.assertEqual(self.stats.greater(-10), 5)
        self.assertEqual(self.stats.greater(0), 5)
        self.assertEqual(self.stats.greater(3), 3)
        self.assertEqual(self.stats.greater(9), 0)
        self.assertEqual(self.stats.greater(10), 0)

    def test_stats_between(self):
        self.assertEqual(self.stats.between(-10, 0), 0)
        self.assertEqual(self.stats.between(-10, 10), 5)
        self.assertEqual(self.stats.between(0, 10), 5)
        self.assertEqual(self.stats.between(0, 2), 0)
        self.assertEqual(self.stats.between(2, 4), 3)
        self.assertEqual(self.stats.between(3, 6), 4)
        self.assertEqual(self.stats.between(4, 6), 2)
        self.assertEqual(self.stats.between(6, 8), 1)
        self.assertEqual(self.stats.between(8, 10), 1)
        self.assertEqual(self.stats.between(10, 20), 0)
