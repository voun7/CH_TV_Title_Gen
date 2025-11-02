# CH TV Title Generator

![python version](https://img.shields.io/badge/Python-3.10-blue)

A program that changes chinese tv show titles to english format.

## Setup Instructions

### Install Packages

```commandline
pip install -r requirements.txt
```

### Build Package:

```commandline
python -m build
```

## Usage

### Install using pip:

```
pip install git+https://github.com/voun7/CH_TV_Title_Gen.git
```

Append tag for install of specific version e.g. `@1.1`

``` python
from ch_title_gen import ChineseTitleGenerator

gen = ChineseTitleGenerator()
tv_name = gen.generate_title("peerless 第七季 第四十八集", "peerless")
print(tv_name)
```

output: `peerless S7 EP48`
