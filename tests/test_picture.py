# encoding: utf-8

"""Test suite for pptx.picture module."""

from hamcrest import assert_that, equal_to, is_

from pptx.constants import MSO

from testdata import test_shapes
from testing import TestCase


class Test_Picture(TestCase):
    """Test _Picture"""
    def test_shape_type_value_correct_for_picture(self):
        """_Shape.shape_type value is correct for picture"""
        # setup ------------------------
        picture = test_shapes.picture
        # verify -----------------------
        assert_that(picture.shape_type, is_(equal_to(MSO.PICTURE)))