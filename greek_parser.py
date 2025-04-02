import re, unicodedata
from lists import greek_capitals, greek_lowers, greek_special_cases, greek_accents, greek_punctuation

unicode_to_beta = {v: k for k, v in {**greek_capitals, **greek_lowers, **greek_accents, **greek_special_cases, **greek_punctuation}.items()}

def greek_to_beta(text):
    normalized = unicodedata.normalize('NFD', text)  # Decompose accents
    out = [unicode_to_beta.get(ord(c), c) for c in normalized]  # Map each char
    return "".join(out)

def beta_to_greek(text):
    # Handle final sigma case
    text = re.sub(r'(S)(\b)', r'S2', text)

    # Replace capital letters first
    for key, value in greek_capitals.items():
        text = text.replace(key, chr(value))
    
    # Replace special cases
    for key, value in greek_special_cases.items():
        text = text.replace(key, chr(value))
    
    # Replace lowercase letters
    out = []
    i = 0
    while i < len(text):
        char = text[i]
        if char in greek_lowers:
            out.append(chr(greek_lowers[char]))
        elif char in greek_accents:
            out.append(chr(greek_accents[char]))
        elif char in greek_punctuation:
            out.append(chr(greek_punctuation[char]))
        else:
            out.append(char)
        i += 1

    # Normalize to compose accents properly
    return unicodedata.normalize('NFC', ''.join(out))