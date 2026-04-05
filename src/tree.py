# placeholder -- tree class implementation and smoke test

class TableOfContentsNode:
    def __init__(self, title):
        self.title = title
        self.children = []

    def __str__(self):
        return str(self.title)

class TableOfContents:
    def __init__(self, book_title, source_url):
        self.root = TableOfContentsNode(book_title)
        self.source_url = source_url
        self.children = []

    def add_child(self, parent, child):
        parent.children.append(child)

    def insert(self, path, title):
        """
        Accepts path like [1, 2, 1] for Chapter 1, Section 2, Subsection 1.
        """
        current = self.root
        for step in path:
            index = step - 1
            
            # Fill missing sibling nodes with placeholders if they don't exist yet
            while len(current.children) <= index:
                self.add_child(current, TableOfContentsNode("Untitled Placeholder"))
            
            current = current.children[index]
        current.title = title

    def print_toc(self, mode):
        print(f"Source: {self.source_url}\n")
        for i, child in enumerate(self.root.children, start=1):
            self.dfs_traverse(child, "indented", [i], 1)


    def dfs_traverse(self, node, mode, indices, level):
        indent = "  " * level
        if mode == "numbered":
            print(f"{indent}{'.'.join(map(str, indices))} {node.title}")
        elif mode == "indented":
            print(f"{indent}- {node.title}")
        elif mode == "plain":
            print(node.title)

        for i, child in enumerate(node.children, start=1):
            self.dfs_traverse(child, mode, indices + [i], level + 1)

    def find_node(self, current, title):
        if current.title == title:
            return current
        for child in current.children:
            result = self.find_node(child, title)
            if result:
                return result
        return None

    def get_height(self, node):
        target = self.find_node(self.root, node)
        if not node.children:
            return 0
        return 1 + max(self.get_height(child) for child in node.children)

    def get_depth(self, target_title, node=None, depth=0):
        if node is None:
            node = self.root
        if node.title == target_title:
            return depth
        for child in node.children:
            result = self.get_depth(target_title, child, depth + 1)
            if result is not None:
                return result
        return None


# smoke test
if __name__ == "__main__":
    source = "https://cbwilp-artefacts.s3.ap-south-1.amazonaws.com/AIML/SEM2/FREE_BOOKS/Ronald_T_Kneusel_Math_for_Deep_Learning_What_You_Need_to_Know_to.pdf"
    book = TableOfContents("Math for Deep Learning", source)

    book.insert([1], "SETTING THE STAGE")
    book.insert([1, 1], "Installing the Toolkits")
    book.insert([1, 1, 1], "Linux")
    book.insert([1, 1, 2], "macOS")
    book.insert([1, 1, 3], "Windows")
    book.insert([1, 2], "NumPy")
    book.insert([1, 2, 1], "Defining Arrays")
    book.insert([1, 2, 2], "Data Types")

    book.insert([2], "PROBABILITY")
    book.insert([2, 1], "Basic Concepts")
    book.insert([2, 1, 1], "Sample Space and Events")
    book.insert([2, 1, 2], "Random Variables")
    book.insert([2, 2], "The Rules of Probability")
    book.insert([2, 2, 1], "Probability of an Event")

    # Run Outputs
    print("--- FULL TOC (INDENTED NUMBERED) ---")
    book.print_toc(mode="indented_numbered")
