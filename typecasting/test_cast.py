#!/usr/bin/env python

import unittest

from typecast import to_long


class TestTypecast(unittest.TestCase):

    def _test_cast(self, string, base=10):
        self.assertEqual(to_long(string, base), long(string, base))

    def test_happy_path(self):
        self._test_cast("123")
        self._test_cast("768937")
        self._test_cast("0")

    def test_binary(self):
        self._test_cast("1010101011110", 2)
        self._test_cast("101", 2)
        self._test_cast("1", 2)

    def test_hex(self):
        self._test_cast("12", 16)
        self._test_cast("18ca3e", 16)
        self._test_cast("93BAE12F", 16)
        self._test_cast("0x8D8D20C", 16)

    def test_negatives(self):
        self._test_cast("-0")
        self._test_cast("-12334")
        self._test_cast("-F7A2E12", 16)

    def test_long_notation(self):
        self._test_cast("12456L")
        self._test_cast("21839l")
        self._test_cast("1ae32bL", 16)
        self._test_cast("101111L", 2)

    def test_very_large_number(self):
        self._test_cast("3F6A8885A308D313198A2E03707344A4093822299F31D0083F6A8885A308D313198A2E03707344A4093822299F31D008", 16)

    def test_scientific_notation(self):
        with self.assertRaises(ValueError):
            self._test_cast("1.23E+11")

    def test_invalid_characters(self):
        with self.assertRaises(ValueError):
            self._test_cast("29,218")
        with self.assertRaises(ValueError):
            self._test_cast("$20")
        with self.assertRaises(ValueError):
            self._test_cast("20+1")

    def test_decimals(self):
        with self.assertRaises(ValueError):
            self._test_cast("121.65")

    def test_number_larger_than_base(self):
        with self.assertRaises(ValueError):
            self._test_cast("E1894")
        with self.assertRaises(ValueError):
            self._test_cast("1219", 2)

    def test_non_strings(self):
        with self.assertRaises(TypeError):
            self._test_cast(12)
        with self.assertRaises(TypeError):
            self._test_cast(None)
        with self.assertRaises(TypeError):
            self._test_cast(["123"])

    def test_invalid_base(self):
        with self.assertRaises(TypeError):
            self._test_cast("123", 20)
        with self.assertRaises(TypeError):
            self._test_cast("123", 1)
        with self.assertRaises(TypeError):
            self._test_cast("123", "foo")

if __name__ == '__main__':
    unittest.main()
