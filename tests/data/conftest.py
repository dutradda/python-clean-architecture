# -*- coding: utf-8 -*-
from mock import Mock
import pytest

from dharma.utils.tests.factories import nature_class_factory


@pytest.fixture
def nature_class():
    return nature_class_factory(trait_name='a_trait', nature_name='ANature')


@pytest.fixture
def nature_instance(nature_class):
    return nature_class()


@pytest.fixture
def nature_instance_with_listener(nature_instance):
    nature_instance.mock = Mock()

    def a_listener(instance, old_value, new_value):
        instance.mock(instance, old_value, new_value)

    nature_instance.dharma['a_trait'].add_instance_listener(
        nature_instance, a_listener)
    return nature_instance