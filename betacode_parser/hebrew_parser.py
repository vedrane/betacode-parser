import re as _re
import unicodedata as _unicodedata
from betacode_parser.parser import _convert_to_beta
from betacode_parser.hebrew_lists import _hebrew_alphabet, _hebrew_special_cases, _old_hebrew_alphabet, _old_hebrew_special_cases

heb_unicode_to_beta = {v: k for k, v in {**_hebrew_alphabet, **_hebrew_special_cases}.items()}
old_heb_unicode_to_beta = {v: k for k, v in {**_old_hebrew_alphabet}.items()}
old_heb_special_unicode_to_beta = {v: k for k, v in {**_old_hebrew_special_cases}.items()}

diacritics_include = {'\u05C1', '\u05C2'}

def _remove_diacritics(text, old):
    normalized = _unicodedata.normalize('NFKD', text)
    return ''.join(
        c for c in normalized
        if not (_unicodedata.combining(c) and (not old or c not in diacritics_include))
    )

def hebrew_to_beta(text, old=False):
    text = _remove_diacritics(text, old)
    
    if old:
        text = _convert_to_beta(text, old_heb_unicode_to_beta)
        text = text.replace(f'#{chr(0x05C1)}', "$").replace(f'#{chr(0x05C2)}', "&")
        return _convert_to_beta(text, old_heb_special_unicode_to_beta)
    
    return _convert_to_beta(text, heb_unicode_to_beta)


def beta_to_hebrew(text, old=False):
    text += ' ' # Handle final letter case
    mapping = _old_hebrew_alphabet if old else _hebrew_alphabet
    special_cases = _old_hebrew_special_cases if old else _hebrew_special_cases
    
    # Apply special case substitutions
    if old:
        for key, value in special_cases.items():
            text = _re.sub(fr'({key})(\s+)', fr'{chr(value)}\2', text)
            text = _re.sub(fr'({key})(?=[.!?#:])', fr'{chr(value)}\2', text)
    else:
        for key, value in special_cases.items():
            text = text.replace(key, chr(value))
    
    # Convert Beta to Hebrew
    for key, value in mapping.items():
        text = text.replace(key, chr(value))
    
    text = text[:-1] # Remove last space
    
    return text