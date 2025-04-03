import re, unicodedata
from parser import convert_to_beta
from hebrew_lists import hebrew_alphabet, hebrew_special_cases, old_hebrew_alphabet, old_hebrew_special_cases

heb_unicode_to_beta = {v: k for k, v in {**hebrew_alphabet, **hebrew_special_cases}.items()}
old_heb_unicode_to_beta = {v: k for k, v in {**old_hebrew_alphabet}.items()}
old_heb_special_unicode_to_beta = {v: k for k, v in {**old_hebrew_special_cases}.items()}

diacritics_include = {'\u05C1', '\u05C2'}

def _remove_diacritics(text):
    return ''.join(
        c for c in unicodedata.normalize('NFKD', text)
        if not (unicodedata.combining(c) and c not in diacritics_include)
    )

def hebrew_to_beta(text, old=False):
    text = _remove_diacritics(text)
    
    if old:
        text = convert_to_beta(text, old_heb_unicode_to_beta)
        text = text.replace(f'#{chr(0x05C1)}', "$").replace(f'#{chr(0x05C2)}', "&")
        return convert_to_beta(text, old_heb_special_unicode_to_beta)
    
    return convert_to_beta(text, heb_unicode_to_beta)


def beta_to_hebrew(text, old=False):
    mapping = old_hebrew_alphabet if old else hebrew_alphabet
    special_cases = old_hebrew_special_cases if old else hebrew_special_cases
    
    # Apply special case substitutions
    for key, value in special_cases.items():
        text = re.sub(fr'({key})\b', chr(value), text)
    
    # Convert Beta to Hebrew
    for key, value in mapping.items():
        text = text.replace(key, chr(value))
    
    return text