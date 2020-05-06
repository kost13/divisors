from django.test import SimpleTestCase

import divisors

class DivisorsAlgorithmTest(SimpleTestCase):
    """
    Divisors algorithm test checks if the divisors are
    computed correctly.
    """

    def test_normal_16(self):
        expect = [4, 2, 8, 1, 16]
        ret = divisors.compute_divisors(16)
        self.assertCountEqual(expect, ret)

    def test_normal_31(self):
        expect = [1, 31]
        ret = divisors.compute_divisors(31)
        self.assertCountEqual(expect, ret)

    def test_normal_144(self):
        expect = [1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 36, 48, 72, 144]
        ret = divisors.compute_divisors(144)
        self.assertCountEqual(expect, ret)

    def test_negative(self):
        expect = []
        ret = divisors.compute_divisors(-16)
        self.assertCountEqual(expect, ret)

    def test_big(self):
        expect = [1, 2, 4, 8, 17, 19, 34, 38, 43, 68, 76, 86, 136, 152, 172, 289,
                  323, 344, 361, 578, 646, 722, 731, 817, 1156, 1292, 1444, 1462,
                  1634, 1849, 2312, 2584, 2888, 2924, 3268, 3698, 5491, 5848, 6137,
                  6536, 7396, 10982, 12274, 12427, 13889, 14792, 15523, 21964, 24548,
                  24854, 27778, 31046, 31433, 35131, 43928, 49096, 49708, 55556, 62092,
                  62866, 70262, 99416, 104329, 111112, 124184, 125732, 140524, 208658,
                  236113, 251464, 263891, 281048, 417316, 472226, 527782, 534361,
                  597227, 667489, 834632, 944452, 1055564, 1068722, 1194454, 1334978,
                  1888904, 2111128, 2137444, 2388908, 2669956, 4274888, 4486147, 4777816,
                  5339912, 8972294, 10152859, 11347313, 17944588, 20305718, 22694626,
                  35889176, 40611436, 45389252, 81222872, 90778504, 192904321, 385808642,
                  771617284, 1543234568]
        ret = divisors.compute_divisors(1543234568)
        self.assertCountEqual(expect, ret)

