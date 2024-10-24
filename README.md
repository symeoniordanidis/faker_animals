# faker_animals
A provider for the python faker library to generate animals data for testing purpose


## Examples

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