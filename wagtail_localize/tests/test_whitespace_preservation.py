from django.test import TestCase
from wagtail_localize.strings import extract_strings, restore_strings, StringValue

class TestWhitespacePreservation(TestCase):
    def test_extract_strings_preserves_double_spaces_between_tags(self):
        html = "<p><b>Hello</b>  <b>World</b></p>"
        template, strings = extract_strings(html)

        # Check that the extracted string preserves the double spaces
        self.assertEqual(strings[0][0].data, "<b>Hello</b>  <b>World</b>")

        restored = restore_strings(template, strings)
        # Check that the restored HTML preserves the double spaces
        self.assertIn("<b>Hello</b>  <b>World</b>", restored)

    def test_string_value_from_source_html_preserves_double_spaces(self):
        html = "<b>Hello</b>  <b>World</b>"
        string_val, attrs = StringValue.from_source_html(html)
        self.assertEqual(string_val.data, "<b>Hello</b>  <b>World</b>")

    def test_string_value_from_translated_html_preserves_double_spaces(self):
        html = "<b>Hello</b>  <b>World</b>"
        string_val = StringValue.from_translated_html(html)
        self.assertEqual(string_val.data, "<b>Hello</b>  <b>World</b>")

    def test_string_value_from_plaintext_preserves_double_spaces(self):
        # This already worked but good to keep for regression
        text = "Hello  World"
        string_val = StringValue.from_plaintext(text)
        self.assertEqual(string_val.data, "Hello  World")
