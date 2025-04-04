import re as _re
import unicodedata as _unicodedata
from betacode_parser.parser import _convert_to_beta
from betacode_parser.greek_lists import _greek_capitals, _greek_lowers, _greek_special_cases, _greek_accents, _greek_punctuation

greek_unicode_to_beta = {v: k for k, v in {**_greek_capitals, **_greek_lowers, **_greek_accents, **_greek_special_cases, **_greek_punctuation}.items()}

def greek_to_beta(text):
    return _convert_to_beta(text, greek_unicode_to_beta).replace(chr(0x02B9), '#')

def beta_to_greek(text):
    text += ' ' # Handle final sigma case
    text = _re.sub(r'(S)(\s+)', r'S2\2', text)
    text = _re.sub(r'S(?=[.!?#:])', r'S2\2', text)

    # Replace capital letters first
    for key, value in _greek_capitals.items():
        text = text.replace(key, chr(value))
    
    # Replace special cases
    for key, value in _greek_special_cases.items():
        text = text.replace(key, chr(value))
    
    # Replace lowercase letters
    out = []
    i = 0
    while i < len(text):
        char = text[i]
        if char in _greek_lowers:
            out.append(chr(_greek_lowers[char]))
        elif char in _greek_accents:
            out.append(chr(_greek_accents[char]))
        elif char in _greek_punctuation:
            out.append(chr(_greek_punctuation[char]))
        else:
            out.append(char)
        i += 1

    # Normalize to compose accents properly
    # Remove last space, replace messed up punctuation
    return _unicodedata.normalize('NFC', ''.join(out[:-1])).replace(chr(0x02B9), chr(0x0374))