import unittest
from HighestAverageMethod import HighestAverageMethod
from LargestRemainderMethod import LargestRemainderMethod


class TestSum(unittest.TestCase):
    def test_ham_normal(self):
        d_hondt = HighestAverageMethod({"a": {"votes": 50000, "electorates": 30}, "b": {"votes": 40000, "electorates":
                                       15}}, 90, {"threshold": False, "tag_along": False, "overhang": False,
                                       "levelling": False}, 0, 0, 1)
        self.assertEqual(d_hondt.calculate_party_dict(d_hondt.calculate_seats()), {"a": {"votes": 50000,
                         "electorates": 30, "list": 20, "total": 50}, "b": {"votes": 40000, "electorates": 15, "list":
                                                                            25, "total": 40}})

    def test_ham_no_overhang(self):
        d_hondt = HighestAverageMethod({"a": {"votes": 50000, "electorates": 45}, "b": {"votes": 40000, "electorates":
                                       5}}, 70, {"threshold": False, "tag_along": False, "overhang": False,
                                       "levelling": False}, 0, 0, 1)
        self.assertEqual(d_hondt.calculate_party_dict(d_hondt.calculate_seats()), {"a": {"votes": 50000,
                         "electorates": 45, "list": 0, "total": 45}, "b": {"votes": 40000, "electorates": 5, "list": 20,
                                                                           "total": 25}})

    def test_ham_overhang(self):
        d_hondt = HighestAverageMethod({"a": {"votes": 50000, "electorates": 45}, "b": {"votes": 40000, "electorates":
                                       5}}, 70, {"threshold": False, "tag_along": False, "overhang": True,
                                       "levelling": False}, 0, 0, 1)
        self.assertEqual(d_hondt.calculate_party_dict(d_hondt.calculate_seats()), {"a": {"votes": 50000,
                         "electorates": 45, "list": 0, "total": 45}, "b": {"votes": 40000, "electorates": 5, "list": 26,
                                                                           "total": 31}})

    def test_ham_levelling(self):
        d_hondt = HighestAverageMethod({"a": {"votes": 50000, "electorates": 45}, "b": {"votes": 40000, "electorates":
                                       5}}, 70, {"threshold": False, "tag_along": False, "overhang": False,
                                       "levelling": True}, 0, 0, 1)
        self.assertEqual(d_hondt.calculate_party_dict(d_hondt.calculate_seats()), {"a": {"votes": 50000,
                         "electorates": 45, "list": 0, "total": 45}, "b": {"votes": 40000, "electorates": 5, "list": 31,
                                                                           "total": 36}})

    def test_ham_threshold(self):
        d_hondt = HighestAverageMethod({"a": {"votes": 50000, "electorates": 50}, "b": {"votes": 2000, "electorates":
                                       0}}, 100, {"threshold": True, "tag_along": False, "overhang": False,
                                       "levelling": False}, 5, 0, 1)
        self.assertEqual(d_hondt.calculate_party_dict(d_hondt.calculate_seats()), {"a": {"votes": 50000,
                         "electorates": 50, "list": 50, "total": 100}, "b": {"votes": 2000, "electorates": 0, "list": 0,
                                                                             "total": 0}})

    def test_ham_tag_along(self):
        d_hondt = HighestAverageMethod({"a": {"votes": 50000, "electorates": 49}, "b": {"votes": 2000, "electorates":
                                       1}}, 100, {"threshold": False, "tag_along": True, "overhang": False,
                                       "levelling": False}, 5, 1, 1)
        self.assertEqual(d_hondt.calculate_party_dict(d_hondt.calculate_seats()), {"a": {"votes": 50000,
                         "electorates": 49, "list": 48, "total": 97}, "b": {"votes": 2000, "electorates": 1, "list": 2,
                                                                            "total": 3}})

    def test_lrm_normal(self):
        hare = LargestRemainderMethod({"a": {"votes": 50000, "electorates": 30}, "b": {"votes": 40000, "electorates":
                                       15}}, 90, {"threshold": False, "tag_along": False, "overhang": False,
                                                  "levelling": False}, 0, 0, 0, False)
        self.assertEqual(hare.calculate_party_dict(hare.calculate_seats()), {"a": {"votes": 50000,
                         "electorates": 30, "list": 20, "total": 50}, "b": {"votes": 40000, "electorates": 15, "list":
                                                                            25, "total": 40}})

    def test_lrm_no_overhang(self):
        hare = LargestRemainderMethod({"a": {"votes": 50000, "electorates": 45}, "b": {"votes": 40000, "electorates":
                                       5}}, 70, {"threshold": False, "tag_along": False, "overhang": False,
                                                 "levelling": False}, 0, 0, 0, False)
        self.assertEqual(hare.calculate_party_dict(hare.calculate_seats()), {"a": {"votes": 50000, "electorates": 45,
                         "list": 0, "total": 45}, "b": {"votes": 40000, "electorates": 5, "list": 20, "total": 25}})

    def test_lrm_overhang(self):
        hare = LargestRemainderMethod({"a": {"votes": 50000, "electorates": 45}, "b": {"votes": 40000, "electorates":
                                       5}}, 70, {"threshold": False, "tag_along": False, "overhang": True,
                                                 "levelling": False}, 0, 0, 0, False)
        self.assertEqual(hare.calculate_party_dict(hare.calculate_seats()), {"a": {"votes": 50000, "electorates": 45,
                         "list": 0, "total": 45}, "b": {"votes": 40000, "electorates": 5, "list": 26, "total": 31}})

    def test_lrm_levelling(self):
        hare = LargestRemainderMethod({"a": {"votes": 50000, "electorates": 45}, "b": {"votes": 40000, "electorates":
                                       5}}, 70, {"threshold": False, "tag_along": False, "overhang": False,
                                                 "levelling": True}, 0, 0, 0, False)
        self.assertEqual(hare.calculate_party_dict(hare.calculate_seats()), {"a": {"votes": 50000, "electorates": 45,
                         "list": 0, "total": 45}, "b": {"votes": 40000, "electorates": 5, "list": 31, "total": 36}})

    def test_lrm_threshold(self):
        hare = LargestRemainderMethod({"a": {"votes": 50000, "electorates": 50}, "b": {"votes": 2000, "electorates":
                                      0}}, 100, {"threshold": True, "tag_along": False, "overhang": False,
                                      "levelling": False}, 5, 0, 0, False)
        self.assertEqual(hare.calculate_party_dict(hare.calculate_seats()), {"a": {"votes": 50000, "electorates": 50,
                         "list": 50, "total": 100}, "b": {"votes": 2000, "electorates": 0, "list": 0, "total": 0}})

    def test_lrm_tag_along(self):
        hare = LargestRemainderMethod({"a": {"votes": 50000, "electorates": 49}, "b": {"votes": 2000, "electorates":
                                       1}}, 100, {"threshold": False, "tag_along": True, "overhang": False,
                                                  "levelling": False}, 5, 1, 0, False)
        self.assertEqual(hare.calculate_party_dict(hare.calculate_seats()), {"a": {"votes": 50000, "electorates": 49,
                         "list": 47, "total": 96}, "b": {"votes": 2000, "electorates": 1, "list": 3, "total": 4}})

    def test_no_tag_along_edge_case(self):
        hare = LargestRemainderMethod({"a": {"votes": 50000, "electorates": 49}, "b": {"votes": 2000, "electorates": 1}}
                                      , 100, {"threshold": True, "tag_along": False, "overhang": False,
                                              "levelling": False}, 5, 0, 0, False)
        self.assertEqual(hare.calculate_party_dict(hare.calculate_seats()), {"a": {"votes": 50000, "electorates": 49,
                         "list": 50, "total": 99}, "b": {"votes": 2000, "electorates": 1, "list": 0, "total": 1}})


if __name__ == '__main__':
    unittest.main()
