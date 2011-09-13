import unittest

from django.utils import text

class TestUtilsText(unittest.TestCase):

    def test_truncate_words(self):
        self.assertEqual('The quick brown fox jumped over the lazy dog.',
            text.truncate_words('The quick brown fox jumped over the lazy dog.', 10))
        self.assertEqual('The quick brown fox ...',
            text.truncate_words('The quick brown fox jumped over the lazy dog.', 4))
        self.assertEqual('The quick brown fox ....',
            text.truncate_words('The quick brown fox jumped over the lazy dog.', 4, '....'))

    def test_truncate_html_words(self):
        self.assertEqual('<p><strong><em>The quick brown fox jumped over the lazy dog.</em></strong></p>',
            text.truncate_html_words('<p><strong><em>The quick brown fox jumped over the lazy dog.</em></strong></p>', 10))
        self.assertEqual('<p><strong><em>The quick brown fox ...</em></strong></p>',
            text.truncate_html_words('<p><strong><em>The quick brown fox jumped over the lazy dog.</em></strong></p>', 4))
        self.assertEqual('<p><strong><em>The quick brown fox ....</em></strong></p>',
            text.truncate_html_words('<p><strong><em>The quick brown fox jumped over the lazy dog.</em></strong></p>', 4, '....'))
        self.assertEqual('<p><strong><em>The quick brown fox</em></strong></p>',
            text.truncate_html_words('<p><strong><em>The quick brown fox jumped over the lazy dog.</em></strong></p>', 4, None))

    def test_wrap(self):
        digits = '1234 67 9'
        self.assertEqual(text.wrap(digits, 100), '1234 67 9')
        self.assertEqual(text.wrap(digits, 9), '1234 67 9')
        self.assertEqual(text.wrap(digits, 8), '1234 67\n9')

        self.assertEqual(text.wrap('short\na long line', 7),
                         'short\na long\nline')

        self.assertEqual(text.wrap('do-not-break-long-words please? ok', 8),
                         'do-not-break-long-words\nplease?\nok')

        long_word = 'l%sng' % ('o' * 20)
        self.assertEqual(text.wrap(long_word, 20), long_word)
        self.assertEqual(text.wrap('a %s word' % long_word, 10),
                         'a\n%s\nword' % long_word)
