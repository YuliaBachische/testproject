import requests
from typing import List, Dict, Tuple

SPELLER_API_URL = "https://speller.yandex.net/services/spellservice.json/checkText"


def check_spelling_in_text(title: str, content: str) -> Tuple[str, str, List[Dict[str, str]]]:
    """
    Проверяет орфографию текста и возвращает исправленные тексты и список ошибок.

    :param title: Заголовок заметки
    :param content: Содержание заметки
    :return: Кортеж из исправленного заголовка, исправленного содержания и списка ошибок
    """
    url = "https://speller.yandex.net/services/spellservice.json/checkText"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    data = {
        "text": title + " | " + content,
        "lang": "ru"
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        corrections = response.json()

        corrected_text = title + " | " + content
        offset = 0
        spelling_errors = []

        for correction in corrections:
            pos = correction.get('pos', 0) + offset
            len_corr = correction.get('len', 0)
            replacement = correction.get('s', [corrected_text[pos]])[0]

            corrected_text = corrected_text[:pos] + replacement + corrected_text[pos + len_corr:]
            offset += len(replacement) - len_corr

            spelling_errors.append({
                "pos": pos,
                "len": len_corr,
                "replacement": replacement
            })

        split_index = corrected_text.find(' | ')
        if split_index != -1:
            corrected_title = corrected_text[:split_index]
            corrected_content = corrected_text[split_index + 3:]
        else:
            corrected_title = corrected_text
            corrected_content = ""

        return corrected_title, corrected_content, spelling_errors

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return title, content, []