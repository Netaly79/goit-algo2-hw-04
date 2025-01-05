from trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings):
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            raise ValueError("Parameter must be a string array")
        if not strings:
            print("Parameter cannot be empty")
            return ""

        for string in strings:
            self.put(string)

        prefix = []
        node = self.root

        while node and len(node.children) == 1 and node.value is None:
            char, next_node = next(iter(node.children.items()))
            prefix.append(char)
            node = next_node

        return "".join(prefix)


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    # Extra negative cases

    # trie = LongestCommonWord()
    # strings = []
    # assert trie.find_longest_common_word(strings) == ""

    # trie = LongestCommonWord()
    # strings = ["dog", 1, True]
    # assert trie.find_longest_common_word(strings) == ""
