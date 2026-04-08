# Tree Implementation
class TableOfContentsNode:
    def __init__(self, title):
        """
        INITIALIZES A SINGLE NODE IN TABLE OF CONTENTS TREE
        PARAMS:
            self - NODE BEING INITIALIZED
            title - TITLE OF CHAPTER OR SUBHEADING
        RETURNS:
            None
        """
        self.title = title
        self.children = []

    def __str__(self):
        """
        RETURNS STRING REPRESENTATION OF NODE
        PARAMS:
          self -  NODE BEING RETURNED
        RETURNS:
          str -  Title of node
        """
        return str(self.title)

class TableOfContents:
    def __init__(self, book_title, source_url):
        """
        INITIALIZES TABLE OF CONTENT WITH ROOT/CHILDREN NODES AND SOURCE URL
        PARAMS:
            self - TREE BEING INITIALIZED
            book_title - TITLE OF CHAPTER OR SUBHEADING
            source_url - URL OF BOOK
        RETURNS:
            None
        """
        self.root = TableOfContentsNode(book_title)
        self.source_url = source_url
        self.children = []

    def add_child(self, parent, child):
        """
        APPENDS CHILD NODE TO GIVEN PARENT NODE
        PARAMS:
            self - TREE BEING MODIFIED
            parent(TableOfContentsNode) - NODE, CHILD IS BEING ADDED TO
            child(TableOfContentsNode) - NEW NODE BEING ADDED
        RETURNS:
            None - MODIFIES PARENT NODE
        """
        parent.children.append(child)

    def insert(self, path, title):
        """
        INSERTS AT GIVEN PATH WITH ITS TITLE, "UNTITLED PLACEHOLDER" IF
        PATH IS SKIPPED.
        PARAMS:
          self - TREE BEING MODIFIED
          path - Accepts path like [1, 2, 1] for Chapter 1, Section 2, Subsection 1.
          title - TITLE OF CHAPTER OR SUBHEADING
        RETURNS:
          None - MODIFIES TREE
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
        """
        PRINTS ENTIRE TABLE OF CONTENTS THROUGH DFS TRAVERSE
        PARAMS:
            self - TREE BEING TRAVERSED
            mode - FORMATING MODE ("indented_numbered", "indented", "plain")
        RETURNS:
            None - PRINTS TABLE OF CONTENTS
        """
        print(f"Source: {self.source_url}\n")
        for i, child in enumerate(self.root.children, start=1):
            self.dfs_traverse(child, mode, [i], 1)


    def dfs_traverse(self, node, mode, indices, level):
        """
        TRAVERSES TREE THROUGH DEPTH-FIRST SEARCH
        PARAMS:
            self - TREE BEING TRAVERSED
            node - CURRENT NODE
            mode - FORMATING MODE ("indented_numbered", "indented", "plain")
            indices - SEQUENCE OF NUMBERS TO NAME CHAPTERS OR SUBHEADINGS
            level - CURRENT DEPTH LEVEL TO INDENT
        RETURNS:
            None - PRINTS TABLE OF CONTENTS
        """
        indent = "  " * level
        if mode == "indented_numbered":
            print(f"{indent}{'.'.join(map(str, indices))} {node.title}\n")
        elif mode == "indented":
            print(f"{indent}- {node.title}\n")
        elif mode == "plain":
            print(node.title,"\n")

        for i, child in enumerate(node.children, start=1):
            self.dfs_traverse(child, mode, indices + [i], level + 1)

    def find_node(self, current, title):
        """
        RETURNS GIVEN NODE IF FOUND IN TREE
        PARAMS:
            self - TREE BEING TRAVERSED
            current - CURRENT NODE
            title - GIVEN TITLE THAT IS BEING SEARCHED
        RETURNS:
            Node - RETURNS TITLE OF NODE IF FOUND, NONE IF NOT FOUND
        """
        if current.title == title:
            return current
        for child in current.children:
            result = self.find_node(child, title)
            if result:
                return result
        return None

    def get_height(self, node):
        """
        RETURNS HEIGHT FROM A GIVEN NODE
        PARAMS:
            self - TREE BEING TRAVERSED
            node - NODE WHERE WE CALCULATE OUR HEIGHT FROM
        RETURNS:
            height - RETURNS THE MAX HEIGHT FROM GIVEN NODE
        """
        if not node.children:
            return 0
        return 1 + max(self.get_height(child) for child in node.children)

    def get_depth(self, target_title, node=None, depth=0):
        """
        RETURNS DEPTH FROM TARGET_TITLE
        PARAMS:
            self - TREE BEING TRAVERSED
            target_title - CALCULATES DEPTH FROM TARGET_TITLE
            node - DEFAULTED TO NONE
            depth - DEFAULTED TO 0
        RETURNS:
            depth - RETURNS depth from given target_title
        """
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
