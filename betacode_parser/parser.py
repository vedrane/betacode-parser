import unicodedata as _unicodedata

def _convert_to_beta(text, unicode_to_beta):
    normalized = _unicodedata.normalize('NFD', text)  # Decompose accents
    out = [unicode_to_beta.get(ord(c), c) for c in normalized]  # Map each char
    return "".join(out)