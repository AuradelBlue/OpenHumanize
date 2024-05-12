import spacy, zss
from itertools import combinations

nlp = spacy.load('en_core_web_sm')  # Load the spaCy English model

class Node:
    def __init__(self, label):
        self.label = label
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    @staticmethod
    def get_children(node):
        return node.children

    @staticmethod
    def get_label(node):
        return node.label

def convert_spacy_tree_to_zss(token):
    node = Node(label=token.pos_)
    for child in token.children:
        child_node = convert_spacy_tree_to_zss(child)
        node.add_child(child_node)
    return node

def count_nodes(node):
    if node is None:
        return 0
    return 1 + sum(count_nodes(child) for child in node.children)

def calculate_and_display_distances(sentences):
    distances = []
    node_counts = []
    sentence_pairs = list(combinations(sentences, 2))
    for i, (sent1, sent2) in enumerate(sentence_pairs):
        tree1 = convert_spacy_tree_to_zss(sent1.root)
        tree2 = convert_spacy_tree_to_zss(sent2.root)
        distance = zss.simple_distance(tree1, tree2, Node.get_children, Node.get_label)
        # Calculate the average number of nodes in both trees
        avg_nodes = (count_nodes(tree1) + count_nodes(tree2)) / 2
        normalized_distance = distance / avg_nodes if avg_nodes > 0 else 0
        distances.append(normalized_distance)
        print(f"Pair {i+1}: '{sent1.text}' <-> '{sent2.text}' => Normalized Tree Edit Distance: {normalized_distance:.2f}")
    return sum(distances) / len(distances) if distances else 0

def main():
    text = '''There isn't a strict limit on how long a sentence can be, but generally, sentences that are too long can be hard to read and understand. In writing, a typical sentence might range from 15 to 30 words. However, it's possible to find sentences that are much longer, especially in more complex or technical writing, where they might go over 50 words or more. The key is clarity and readability—long sentences should be structured well to ensure they're easy to follow.'''
    doc = nlp(text)
    sentences = list(doc.sents)
    average_normalized_distance = calculate_and_display_distances(sentences)
    print(f"\nAverage Normalized Tree Edit Distance across all pairs: {average_normalized_distance:.2f}")

if __name__ == "__main__":
    main()
