# Здесь тесты с использованием pytest и ddt
import pytest
from ddt import ddt, data, unpack

@ddt
class TestSpellChecker:

    @data(
        ("teh", "the"),
        ("recieve", "receive"),
        ("adress", "address")
    )
    @unpack
    def test_check_text(self, soap_client, word_pair):
        incorrect_word, correct_word = word_pair
        response = soap_client.check_text(incorrect_word)
        suggestions = [item.s for item in response[0].s]
        assert correct_word in suggestions
