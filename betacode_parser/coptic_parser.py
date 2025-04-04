from betacode_parser.parser import _convert_to_beta
from betacode_parser.coptic_lists import _coptic_capitals, _coptic_lowers

coptic_unicode_to_beta = {v: k for k, v in {**_coptic_capitals, **_coptic_lowers}.items()}

def coptic_to_beta(text):
    return _convert_to_beta(text, coptic_unicode_to_beta)

def beta_to_coptic(text):
    # Replace capital letters first
    for key, value in _coptic_capitals.items():
        text = text.replace(key, chr(value))
    
    # Replace lowercase letters
    out = []
    i = 0
    while i < len(text):
        char = text[i]
        if char in _coptic_lowers:
            out.append(chr(_coptic_lowers[char]))
        else:
            out.append(char)
        i += 1

    # Return
    return ''.join(out)