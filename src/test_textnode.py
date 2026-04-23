import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        expected_repr = "TextNode(This is a text node, bold_text, https://example.com)"
        self.assertEqual(repr(node), expected_repr)

    def test_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        expected_repr = "TextNode(This is a text node, bold_text, None)"
        self.assertEqual(repr(node), expected_repr)

    def test_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        expected_repr = "TextNode(This is a text node, bold_text, https://example.com)"
        self.assertEqual(repr(node), expected_repr)


if __name__ == "__main__":
    unittest.main()