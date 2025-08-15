import pytest

from transliteration_ua import transliterate_ua


@pytest.mark.parametrize(
    "text,expected",
    [
        ("", ""),
        ("Алушта", "Alushta"),
        ("Андрій", "Andrii"),
        ("Борщагівка", "Borshchahivka"),
        ("Борисенко", "Borysenko"),
        ("Вінниця", "Vinnytsia"),
        ("Володимир", "Volodymyr"),
        ("Гадяч", "Hadiach"),
        ("Богдан", "Bohdan"),
        ("Згурський", "Zghurskyi"),
        ("Ґалаґан", "Galagan"),
        ("Ґорґани", "Gorgany"),
        ("Донецьк", "Donetsk"),
        ("Дмитро", "Dmytro"),
        ("Рівне", "Rivne"),
        ("Олег", "Oleh"),
        ("Есмань", "Esman"),
        ("Єнакієве", "Yenakiieve"),
        ("Гаєвич", "Haievych"),
        ("Короп'є", "Koropie"),
        ("Житомир", "Zhytomyr"),
        ("Жанна", "Zhanna"),
        ("Жежелів", "Zhezheliv"),
        ("Закарпаття", "Zakarpattia"),
        ("Казимирчук", "Kazymyrchuk"),
        ("Медвин", "Medvyn"),
        ("Михайленко", "Mykhailenko"),
        ("Іванків", "Ivankiv"),
        ("Іващенко", "Ivashchenko"),
        ("Їжакевич", "Yizhakevych"),
        ("Кадиївка", "Kadyivka"),
        ("Мар'їне", "Marine"),
        ("Йосипівка", "Yosypivka"),
        ("Стрий", "Stryi"),
        ("Олексій", "Oleksii"),
        ("Київ", "Kyiv"),
        ("Коваленко", "Kovalenko"),
        ("Лебедин", "Lebedyn"),
        ("Леонід", "Leonid"),
        ("Миколаїв", "Mykolaiv"),
        ("Маринич", "Marynych"),
        ("Ніжин", "Nizhyn"),
        ("Наталія", "Nataliia"),
        ("Одеса", "Odesa"),
        ("Онищенко", "Onyshchenko"),
        ("Полтава", "Poltava"),
        ("Петро", "Petro"),
        ("Решетилівка", "Reshetylivka"),
        ("Рибчинський", "Rybchynskyi"),
        ("Суми", "Sumy"),
        ("Соломія", "Solomiia"),
        ("Тернопіль", "Ternopil"),
        ("Троць", "Trots"),
        ("Ужгород", "Uzhhorod"),
        ("Уляна", "Uliana"),
        ("Фастів", "Fastiv"),
        ("Філіпчук", "Filipchuk"),
        ("Харків", "Kharkiv"),
        ("Христина", "Khrystyna"),
        ("Біла Церква", "Bila Tserkva"),
        ("Стеценко", "Stetsenko"),
        ("Чернівці", "Chernivtsi"),
        ("Шевченко", "Shevchenko"),
        ("Шостка", "Shostka"),
        ("Кишеньки", "Kyshenky"),
        ("Щербухи", "Shcherbukhy"),
        ("Гоща", "Hoshcha"),
        ("Гаращенко", "Harashchenko"),
        ("Юрій", "Yurii"),
        ("Корюківка", "Koriukivka"),
        ("Яготин", "Yahotyn"),
        ("Ярошенко", "Yaroshenko"),
        ("Костянтин", "Kostiantyn"),
        ("Знам'янка", "Znamianka"),
        ("Феодосія", "Feodosiia"),
    ],
)
def test_official_examples(text, expected):
    """
    Official examples from https://zakon.rada.gov.ua/laws/show/55-2010-%D0%BF
    """
    assert transliterate_ua(text) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("Євген", "Yevhen"),
        ("Я Євген", "Ya Yevhen"),
        ("Я,Євген", "Ya,Yevhen"),
        ("1Євген", "1Yevhen"),
        ("Я,1Євген", "Ya,1Yevhen"),
    ],
)
def test_first_char_replacement(text, expected):
    assert transliterate_ua(text) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("ЗГУРСЬКИЙ", "ZGHURSKYI"),
        ("ЗГУР'ЯНКА", "ZGHURIANKA"),
    ],
)
def test_return_uppercase_if_text_is_uppercase(text, expected):
    """
    If the input text is all uppercase, the output should also be all uppercase.
    """
    assert transliterate_ua(text) == expected
