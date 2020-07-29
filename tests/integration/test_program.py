#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from unittest import TestCase

from myprogram import program

class TestProgram(TestCase):
    def test_division(self):
        result = program.main_program('division')
        expected = 1
        self.assertEqual(result, expected)

    def test_range_type(self):
        result = program.main_program('range_type')
        self.assertIsInstance(result, list)

    def test_raise_error(self):
        with self.assertRaises(IOError):
            program.main_program('raise_error')

    def test_returns_text(self):
        result = program.main_program('text')
        expected = u'русский текст'
        self.assertEqual(result, expected)
