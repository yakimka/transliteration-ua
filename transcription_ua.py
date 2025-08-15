DEFAULT_REPLACEMENTS = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "h",
    "ґ": "g",
    "д": "d",
    "е": "e",
    "є": "ie",
    "ж": "zh",
    "з": "z",
    "и": "y",
    "і": "i",
    "ї": "i",
    "й": "i",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "kh",
    "ц": "ts",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ю": "iu",
    "я": "ia",
}
DEFAULT_FIRST_CHAR_REPLACEMENTS = {
    "є": "ye",
    "ї": "yi",
    "й": "y",
    "ю": "yu",
    "я": "ya",
}
DEFAULT_MULTIPLE_REPLACEMENTS = {
    "зг": "zgh",
}

UA_CHARS = "AБВГҐДЕЄЖЗИЙІЇКЛМНОПРСТУФХЦЧШЩЬЮЯaбвгґдеєжзийіїклмнопрстуфхцчшщьюя"

def transcript(ua_text: str, replacements: dict[str, str] | None = None, multiple_replacements: dict[str, str] | None = None, first_char_replacements: dict[str, str] | None = None) -> str:
    """
    https://zakon.rada.gov.ua/laws/show/55-2010-%D0%BF
    """
    if replacements is None:
        replacements = DEFAULT_REPLACEMENTS
    if multiple_replacements is None:
        multiple_replacements = DEFAULT_MULTIPLE_REPLACEMENTS
    if first_char_replacements is None:
        first_char_replacements = DEFAULT_FIRST_CHAR_REPLACEMENTS

    if not ua_text:
        return ""
    words = ua_text.split(" ")
    new_text = []
    for word in words:
        search_first_char = True
        for char in word:
            replacements_ = replacements
            if search_first_char and char in UA_CHARS:
                search_first_char = False
                if char.lower() in first_char_replacements:
                    replacements_ = first_char_replacements

            if char in replacements_:
                new_text.append(replacements_[char])
            elif char.isupper() and char.lower() in replacements_:
                new_text.append(replacements_[char.lower()].capitalize())
            elif char in UA_CHARS:
                continue
            else:
                new_text.append(char)
        new_text.append(" ")
    return "".join(new_text[:-1])
