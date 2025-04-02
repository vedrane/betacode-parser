import re, unicodedata
from parser import convert_to_beta
from coptic_lists import coptic_capitals, coptic_lowers

coptic_unicode_to_beta = {v: k for k, v in {**coptic_capitals, **coptic_lowers}.items()}

def coptic_to_beta(text):
    return convert_to_beta(text, coptic_unicode_to_beta)

def beta_to_coptic(text):
    # Replace capital letters first
    for key, value in coptic_capitals.items():
        text = text.replace(key, chr(value))
    
    # Replace lowercase letters
    out = []
    i = 0
    while i < len(text):
        char = text[i]
        if char in coptic_lowers:
            out.append(chr(coptic_lowers[char]))
        else:
            out.append(char)
        i += 1

    # Normalize to compose accents properly
    return unicodedata.normalize('NFC', ''.join(out))