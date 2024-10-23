import pytest
from faker import Faker
from ..animals import AnimalsProvider
from ..constants import animals

@pytest.fixture
def fake():
    fake = Faker()
    fake.add_provider(AnimalsProvider)
    return fake

@pytest.fixture
def animal_names():
    return [animal['common_name'] for animal in animals]

@pytest.fixture
def animal_scientific_names():
    return [animal['scientific_name'] for animal in animals]


def test_animal_name(fake,animal_names):
    name = fake.animal_name()
    assert name in animal_names


def test_animal_name_scientific(fake,animal_scientific_names):
    name_scientific = fake.animal_name_scientific()
    assert name_scientific in animal_scientific_names


def test_bird(fake):
    animal = fake.bird()
    assert animal['class'] == 'birds'


def test_fish(fake):
    animal = fake.fish()
    assert animal['class'] == 'fish'


def test_mammal(fake):
    animal = fake.mammal()
    assert animal['class'] == 'mammals'


def test_reptile(fake):
    animal = fake.reptile()
    assert animal['class'] == 'reptiles'


def test_amphibian(fake):
    animal = fake.amphibian()
    assert animal['class'] == 'amphibians'


