# betacode-parser
### Introduction
betacode-parser is a Python package that allows one to convert to and from Beta Code for Greek, Coptic, and Hebrew. It is implemented according to the standard of *Thesaurus Linguae Graecae* (TLG) as seen in [this manual](https://stephanus.tlg.uci.edu/encoding/BCM.pdf). In addition, the Hebrew conversion also supports the older CCAT (Center for Computer Analysis of Text, University of Pennsylvania) standard as seen on [this webpage](https://ccat.sas.upenn.edu/beta/key.html). This project is inspired by the PyPI package [`betacode`](https://pypi.org/project/betacode/), which only implemented conversion for Greek.
### Installation
To install, run `pip install betacode-parser`. Import in projects like this:
```python
from betacode_parser import *
```
Alternatively, you can import the following functions separately: `beta_to_coptic`, `coptic_to_beta`, `beta_to_greek`, `greek_to_beta`, `beta_to_hebrew`, and `hebrew_to_beta`.
### Usage
```python
# Greek
print(beta_to_greek("*A)RIS1TOTE/LHS")) # Ἀριστοτέλης
print(greek_to_beta("Ἀριστοτέλης")), # *A)RIS1TOTE/LHS2

# Coptic
print(beta_to_coptic("*PTOLEMAIOS")) # Ⲡⲧⲟⲗⲉⲙⲁⲓⲟⲥ
print(coptic_to_beta("Ⲡⲧⲟⲗⲉⲙⲁⲓⲟⲥ")) # *PTOLEMAIOS

# Hebrew
# Modern (TLG) Standard
print(beta_to_hebrew("ysrAl")) # ישראל
print(hebrew_to_beta("ישראל")) # ysrAl
# Old (CCAT) Standard
print(beta_to_hebrew("Y&R)L", True)) # ישׂראל
print(hebrew_to_beta("ישראל", True)) # Y#R)L
```
You can see how to transcribe to and from Beta Code manually in the TLG manual and CCAT webpage.
### Development
Contributions are welcome.