from textnode import TextNode, TextType

def main():
    node = TextNode("Hello, World!", TextType.BOLD_TEXT, "https://example.com")
    print(node)

main()