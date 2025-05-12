from typing import Dict, List

def get_word_count(text: str) -> int:
    return len(text.split())

def get_character_count(text: str) -> Dict[str, int]:
    counts = {}
    for char in text.lower():
        if char not in counts:
            counts[char] = 0
        counts[char] += 1
    return counts

def transform_character_count(char_count: Dict[str, int]):
    entries = list(char_count.items())
    entries.sort(key=lambda e: e[1], reverse=True)
    return list(map(lambda e: {"char": e[0], "num": e[1]}, entries))