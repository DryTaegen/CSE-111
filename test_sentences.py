from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest

def test_main():
    test_get_determiner()
    test_get_noun()
    test_get_verb()
    test_get_preposition()
    test_get_prepositional_phrase()


def test_get_determiner():
    # Test the singular determiners.
    singular_determiners = ["the","this","that","my","your","his","her","our","their","one", "either", "neither", "each", "every","another","what"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(256):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_determiners

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural determiners.
    plural_determiners = ["some", "many","these","those","enough","twelve","most","all","both","other","such","my","your","his","her","our","their"]
    for _ in range(256):
        word = get_determiner(0)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():

    singular_nouns = ["adult", "bird", "boy", "car", "cat","child", "dog", "girl", "man", "woman"]

    for _ in range(100):
        word = get_noun(1)

        assert word in singular_nouns

    plural_nouns = ["adults", "birds", "boys", "cars", "cats","children", "dogs", "girls", "men", "women"]
    for _ in range(100):
        word = get_noun(0)

        assert word in plural_nouns

def test_get_verb():

    past_verbs = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]

    for _ in range(100):
        word = get_verb(1, "past")

        assert word in past_verbs

    singular_present = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(100):
        word = get_verb(1, "present")

        assert word in singular_present

    plural_present = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    for _ in range(100):
        word = get_verb(0,"present")

        assert word in plural_present

    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    for _ in range(100):
        word = get_verb(1,"future")

        assert word in future_verbs
def test_get_preposition():

    words = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]

    for _ in range(100):
        word = get_preposition()

        assert word in words
def test_get_prepositional_phrase():
    singular_determiners = ["the","this","that","my","your","his","her","our","their","one", "either", "neither", "each", "every","another","what"]
    plural_determiners = ["some", "many","these","those","enough","twelve","most","all","both","other","such","my","your","his","her","our","their"]
    singular_nouns = ["adult", "bird", "boy", "car", "cat","child", "dog", "girl", "man", "woman"]
    plural_nouns = ["adults", "birds", "boys", "cars", "cats","children", "dogs", "girls", "men", "women"]
    words = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]
    for i in range(100):
        preposition, determiner, noun  = get_prepositional_phrase(1).split(" ")
        assert determiner in singular_determiners
        assert noun in singular_nouns
        assert preposition in words
    for i in range(100):
        preposition, determiner, noun = get_prepositional_phrase(0).split(" ")
        assert determiner in plural_determiners
        assert noun in plural_nouns
        assert preposition in words
test_main()