# test tree class and methods
from tree import TableOfContentsNode, TableOfContents
import pytest

@pytest.fixture
def toc():
    """ Provides empty instance of TableOfContents class for each test """
    source = "https://cbwilp-artefacts.s3.ap-south-1.amazonaws.com/AIML/SEM2/FREE_BOOKS/Ronald_T_Kneusel_Math_for_Deep_Learning_What_You_Need_to_Know_to.pdf"
    return TableOfContents("Math for Deep Learning", source)


def test_add_child(toc):
    """ TEST IF ADD CHILD METHOD WORKS. """
    # Add child method
    toc.add_child(toc.root, TableOfContentsNode("Chapter 1: SETTING THE STAGE"))
    # Length should be 1 since only one child was added
    assert len(toc.root.children) == 1
    # The title of the first child should match my title
    assert toc.root.children[0].title == "Chapter 1: SETTING THE STAGE"
    
def test_insert(toc):
    """ TEST FOR INSERT METHOD. """
    # Insert the first chapter
    toc.insert([1], "Chapter 1: SETTING THE STAGE")
    # First child title should be equal to my first chapter title
    assert toc.root.children[0].title == "Chapter 1: SETTING THE STAGE"
    
def test_missing_insert(toc):
    """ TEST FOR INSERT METHOD WHEN MISSING PARENTS. """
    # Insert Subsection
    toc.insert([1,1], "Installing the Toolkits")
    # First Parent title should be Untitled Placeholder
    assert toc.root.children[0].title == "Untitled Placeholder"
    # The child of my first parent should be equal to the subsection title
    assert toc.root.children[0].children[0].title == "Installing the Toolkits"
    
def test_findNode(toc):
    """ TEST FOR FIND NODE METHOD """
    # Create Table of Contents
    toc.insert([1], "SETTING THE STAGE")
    toc.insert([1, 1], "Installing the Toolkits")
    toc.insert([1, 1, 1], "Linux")
    # Test to find node
    result1 = toc.find_node(toc.root, "SETTING THE STAGE")
    assert result1 is not None
    assert result1.title == "SETTING THE STAGE"
    # Test for missing title
    result2 = toc.find_node(toc.root, "This Chapter is missing")
    assert result2 is None 

def test_getDepth(toc):
    """ TEST FOR GET DEPTH METHOD """
    # Insert Section
    toc.insert([1, 1, 1], "Linux")
    # Test when Title is in book
    assert toc.get_depth("Linux")  == 3
    # Test when Title is not in book
    assert toc.get_depth("This Chapter is missing") is None

def test_get_height(toc):
   """ TEST FOR GET HEIGHT METHOD """
   # Insert Section
   toc.insert([1, 1, 1], "Linux")
   LinuxNode = toc.find_node(toc.root, "Linux")
   # The LinuxNode has no children so it should return 0
   assert toc.get_height(LinuxNode) == 0
   # The root node to LinuxNode is 3 levels deep so it should return 3
   assert toc.get_height(toc.root) == 3
