import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(tag="div", props={"class": "container"}, children=[HTMLNode(tag="p", children=["Hello, World!"])])
        expected_repr = "HTMLNode(tag=div, value=None, children=[HTMLNode(tag=p, value=None, children=['Hello, World!'], props={})], props={'class': 'container'})"
        self.assertEqual(repr(node), expected_repr)

    def test_props_to_html(self):
        node = HTMLNode("div", props={"class": "container", "id": "main"})
        expected_props_html = ' class="container" id="main"'
        self.assertEqual(node.props_to_html(), expected_props_html)

if __name__ == "__main__":
    unittest.main()