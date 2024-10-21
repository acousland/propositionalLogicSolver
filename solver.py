class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value  # The proposition at this node
        self.left = left    # Left child node
        self.right = right  # Right child node

    def __str__(self, level=0):
        """Visual representation of the tree."""
        ret = "  " * level + str(self.value) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1)
        if self.right:
            ret += self.right.__str__(level + 1)
        return ret


def parse_formula(formula):
    """Parses simple propositional formulas."""
    if "∧" in formula:
        left, right = formula.split("∧", 1)
        return TreeNode("∧", parse_formula(left.strip()), parse_formula(right.strip()))
    elif "∨" in formula:
        left, right = formula.split("∨", 1)
        return TreeNode("∨", parse_formula(left.strip()), parse_formula(right.strip()))
    elif "→" in formula:
        left, right = formula.split("→", 1)
        # P → Q is equivalent to ¬P ∨ Q
        return TreeNode("∨", parse_formula(f"¬{left.strip()}"), parse_formula(right.strip()))
    elif formula.startswith("¬"):
        # Negations are treated as leaf nodes here
        return TreeNode(formula)
    else:
        # Single proposition (P, Q, etc.)
        return TreeNode(formula)


def generate_tree(formula):
    """Generates the logic tree for a given formula."""
    root = parse_formula(formula)
    print("Logic Tree:")
    print(root)


# Example usage
formula = "P → Q ∧ ¬Q"
generate_tree(formula)
