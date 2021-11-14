![image](https://raw.githubusercontent.com/cobanov/pyturkce/master/assets/pyturkce-logo.png)

# PyTurkce

![image](https://img.shields.io/travis/cobanov/pyturkce.svg%0A%20%20%20%20%20:target:%20https://travis-ci.com/cobanov/pyturkce)

![image](https://readthedocs.org/projects/pyturkce/badge/?version=latest%0A%20%20%20%20%20:target:%20https://pyturkce.readthedocs.io/en/latest/?version=latest%0A%20%20%20%20%20:alt:%20Documentation%20Status)

Python package for Turkish Language.

- Free software: MIT license
- Documentation: <https://pyturkce.readthedocs.io>.

## Introduction to PyTurkce

## Installation

```bash
pip install pyturkce
```

## Usage

```python
from pyturkce import pyturkce

word = pyturkce.Sozluk('kalem')

print(word.anlamlar) # ['Yazma, çizme vb. işlerde kullanılan çeşitli biçimlerde araç', 'Resmî kuruluşlarda yazı işlerinin görüldüğü yer', 'Yontma işlerinde kullanılan ucu sivri veya keskin araç', 'Çeşit, tür', 'Bazı deyimlerde yazı', 'Yazar']

print(word.ornekler) # ['Kâğıt, kalem, mürekkep, hepsi masanın üstündedir.', 'Kalemindeki odacıya aylığını kırdırırmış.', 'Taşçı kalemi.', 'Oymacı kalemi.', 'Üç kalem erzak.', 'Beş kalem ilaç.', 'Kaleme almak.', 'Peyami Safa, edebiyatımızın usta kalemlerindendir.']

```

## Commands

PyTurkce has also CLI support.

```
usage: pyturkce [-h] [-m] [-i] [-i] [-l] [-r NUM]

optional arguments:
  -h, --help            show this help message and exit
  -m, --meaning         ilgili kelimenin anlamini getirir
  -i, --idiom           ilgili kelime ile kullanilan deyimleri getirir
  -s, --sample          ilgili kelime ile kurulan cumle orneklerini getirir
  -r NUM, --random NUM  Num sayida random kelime getirir (default: 1)

```

## To-Do's

- Fiil, sifat, edat ayirma
- Stop words (etkisiz kelimeleri ayirma)
- random n sayida kelime getir
- icinde, basinda veya sonunda belirli harfleri bulunan kelimeleri getir
- kelimelerin icerdigi harf oranlarina gore hatali kelimeleri bulup duzelt
- turkce kripto bolumleri ekle

## Contributors

We welcome contributions that make PyTurkce better and improve the
existing functionalities of the project.

- Mert Cobanov ([\@cobanov](http://twitter.com/mertcobanov))
- Fethi Tekyaygil ([\@tekyaygilfethi](http://twitter.com/fethidev))
