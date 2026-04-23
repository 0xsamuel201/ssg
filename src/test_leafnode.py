import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag_and_props(self):
        node = LeafNode(tag="p", value="Hello, World!", props={"class": "greeting", "id": "greet1"})
        expected_html = '<p class="greeting" id="greet1">Hello, World!</p>'
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_with_tag_no_props(self):
        node = LeafNode(tag="span", value="Just a span")
        expected_html = '<span>Just a span</span>'
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_no_tag(self):
        node = LeafNode(tag=None, value="No tag here")
        expected_html = 'No tag here'
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_empty_value(self):
        node = LeafNode(tag="div", value="")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()