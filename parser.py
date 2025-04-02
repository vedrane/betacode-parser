import unicodedata

def convert_to_beta(text, unicode_to_beta):
    normalized = unicodedata.normalize('NFD', text)  # Decompose accents
    out = [unicode_to_beta.get(ord(c), c) for c in normalized]  # Map each char
    return "".join(out)