import random
def main():
    quantity = 1
    tense = "past"
    print(f"{get_determiner(quantity)} {get_noun(quantity)} {get_verb(quantity,tense)}.")
    print()
    quantity = 0
    tense = "past"
    print(f"{get_determiner(quantity)} {get_noun(quantity)} {get_verb(quantity,tense)}.")
    print()
    quantity = 1
    tense = "present"
    print(f"{get_determiner(quantity)} {get_noun(quantity)} {get_verb(quantity,tense)}.")
    print()
    quantity = 0
    tense = "present"
    print(f"{get_determiner(quantity)} {get_noun(quantity)} {get_verb(quantity,tense)}.")
    print()
    quantity = 1
    tense = "future"
    print(f"{get_determiner(quantity)} {get_noun(quantity)} {get_verb(quantity,tense)}.")
    print()
    quantity = 0
    tense = "future"
    print(f"{get_determiner(quantity)} {get_noun(quantity)} {get_verb(quantity,tense)}.")
    print()
    quantity = 1
    tense = "past"
    print(f"{get_determiner(quantity)} {get_noun(quantity)} {get_verb(quantity,tense)} {get_prepositional_phrase(quantity)}.")
    print()
    quantity = 0
    tense = "past"
    print(f"{get_determiner(quantity)} {get_noun(quantity)} {get_verb(quantity,tense)} {get_prepositional_phrase(quantity)}.")
    print()
    quantity = 1
    tense = "present"
    print(f"{get_determiner(quantity)} {get_noun(quantity)} {get_verb(quantity,tense)} {get_prepositional_phrase(quantity)}.")
    print()
    quantity = 0
    tense = "present"
    print(f"{get_determiner(quantity)} {get_noun(quantity)} {get_verb(quantity,tense)} {get_prepositional_phrase(quantity)}.")
    print()
    quantity = 1
    tense = "future"
    print(f"{get_determiner(quantity)} {get_noun(quantity)} {get_verb(quantity,tense)} {get_prepositional_phrase(quantity)}.")
    print()
    quantity = 0
    tense = "future"
    print(f"{get_determiner(quantity)} {get_noun(quantity)} {get_verb(quantity,tense)} {get_prepositional_phrase(quantity)}.")
    print()
    
    
def get_determiner(quantity):
    
    if quantity == 1:
        words = ["the","this","that","my","your","his","her","our","their","one", "either", "neither", "each", "every","another","what"]
    else:
        words = ["some", "many","these","those","enough","twelve","most","all","both","other","such","my","your","his","her","our","their"]

    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
        nouns = ["adult", "bird", "boy", "car", "cat","child", "dog", "girl", "man", "woman"]
    else:
        nouns = ["adults", "birds", "boys", "cars", "cats","children", "dogs", "girls", "men", "women"]
    
    word = random.choice(nouns)
    return word

def get_verb(quantity,tense):
    if tense.lower() == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    elif quantity == 1 and tense.lower() == "present":
        verbs = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
    elif quantity == 0 and tense.lower() == "present":
        verbs = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    elif tense.lower() == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    
    word = random.choice(verbs)
    return word
def get_preposition():

    words = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]
    word = random.choice(words)
    return word
def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """
    prep_phrase = get_preposition() + " " +  get_determiner(quantity) + " " + get_noun(quantity)
    return prep_phrase



main()
