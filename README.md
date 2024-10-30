# faker-animals
A provider for the python faker library to generate animals data.

## Description

`faker-animals` offers comprehensive and accurate animals data,covering an extensive range of species. It includes info like the common name and the scientific name. This data can be useful for applications requiring realistic representations of biological diversity, educational tools, wildlife databases, or any project that needs accurate animal species data.

## Installation

Install with pip:

``` bash
pip install faker-animals
```

Add as a provider to your Faker instance:

``` python
from faker import Faker
from faker_animals import AnimalsProvider
fake.add_provider(AnimalsProvider)
```

If you already use faker, you probably know the conventional use is:

```python
fake = Faker()
```

## Usage examples

### Animal

``` python
>>> fake.animal()

{
    'common_name': 'Kangaroo',
    'scientific_name': 'Macropodidae',
    'class': 'mammals'
}
```


### Animal Common Name

``` python
>>> fake.animal_name()

'Brown Bear'
```

### Animal Scientific Name

``` python
>>> fake.animal_name_scientific()

'Ursus arctos'
```

### Bird

``` python
>>> fake.bird()

{
  'common_name': 'African Grey Parrot',
  'scientific_name': 'Psittacus erithacus',
  'class': 'birds'
}
```

### Mammal

``` python
>>> fake.mammal()

{
  'common_name': 'Alaskan Husky',
  'scientific_name': 'Canis lupus',
  'class': 'mammals'
}
```

### Fish

``` python
>>> fake.fish()

{
  'common_name': 'White Catfish',
  'scientific_name': 'A. catus',
  'class': 'fish'
}
```

### Reptile

``` python
>>> fake.reptile()

{
  'common_name': 'Black Mamba',
  'scientific_name': 'D. polylepis',
  'class': 'reptiles'
}
```

### Amphibian

``` python
>>> fake.amphibian()

{
  'common_name': 'Green Frog',
  'scientific_name': 'Lithobates clamitans',
  'class': 'amphibians'
}
```