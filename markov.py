from dictogram import Dictogram
from histogram import file_or_string
import random
import string

def higher_order(word_list, new_words, order=2):
    """
    Parameters:
    word_list: List
    new_words: String
    order: Int

    Returns:
    storage_dict: dict where key is new_words and value is a Dictogram

    Pair programmed with Jon Infante
    """
    storage_dict = dict()

    key_words = new_words.split()
    if len(key_words) != order:
        return "Length of input words does not equal order"

    words = []
    next_words = []
    next_pairs = []

    for i in range(len(word_list) - 1):
        words.clear()
        for j in range(order):
            if i < (len(word_list) - order):
                words.append(word_list[i + j])
        if key_words == words:
            next_words.clear()
            for j in range(order):
                next_words.append(word_list[i + (j + 1)])
            next_words_str = " ".join(next_words)
            next_pairs.append(next_words_str)

    storage_dict[new_words] = Dictogram(next_pairs)
    return storage_dict

def order_sample(word_list, order=2):
    """
    Parameters:
    word_list: List
    order (default = 2): Int 

    Returns:
    words_str: String
    """
    histogram = Dictogram(word_list)
    next_words = []

    # sample a random word from histogram
    next_word_str = histogram.sample()
    # find all the words that come after 
    chain = new_chain(word_list, next_word_str)
    # append both words to a list
    next_words.append(next_word_str)

    for i in range(order - 1):
        if len(chain) > 0:
            next_word_str = chain.sample()
            next_words.append(next_word_str)
            chain = new_chain(word_list, next_word_str)

    # join the words into a string and assign to a variable
    words_str = " ".join(next_words)
    return words_str

def higher_order_walk(word_list, length, order=2):
    """Use order_sample() to generate order number of words. Use those words
       to generate a higher order chain and sample that chain to find the next
       word to append to the sentence. Use that word to generate a new higher 
       order chain and repeat until sentence is complete. Return sentence

    Parameters:
    word_list: List
    length: Int

    Returns:
    sentence: String
    """
    sentence = []
    next_words_list = []
    
    words_str = order_sample(word_list, order)
    # append both words to the sentence
    sentence.append(words_str)

    # repeat until length of sentence == length input
    for i in range(length - order):
        # make sure next_words_list is empty
        next_words_list.clear()
        # get the list of pairs that comes after the previous pair
        chain = higher_order(word_list, words_str, order)
        # if the chain isn't empty
        if len(chain[words_str]) > 0:
            # sample the value in the chain, which is a dictogram
            words_str = chain[words_str].sample()
            # add both words individually to next_words_list
            next_words_list = words_str.split()
            # only append the second word to the sentence
            sentence.append(next_words_list[order - 1])

    return create_sentence(sentence)

def new_chain(word_list, word):
    """If word is in word_list, append the next word to a list.
       Then create a new histogram with the list of following words.
       
       Parameters:
       word_list: List
       word: String

       Returns:
       chain: Dictogram
    """
    chain_list = []
    for i in range(len(word_list) - 1):
        if word == word_list[i]:
            chain_list.append(word_list[i + 1])

    chain = Dictogram(chain_list)
    return chain

def walk(word_list, length):
    """Start sentence with sample word from full histogram. 
       Sample each new histogram chain to get next word, add to sentence. 
       
       Parameters:
       word_list: List
       length: Int

       Returns:
       sentence: List
    """
    sentence = []
    histogram = Dictogram(word_list)
    next_word = histogram.sample()
    sentence.append(next_word)
    for i in range(length - 1):
        chain = new_chain(word_list, next_word)
        if len(chain) > 0:
            next_word = chain.sample()
            sentence.append(next_word)

    return sentence

def create_sentence(words):
    """Joins words in a list, capitalizes the first word and adds a period to the end. 

        Parameters:
        words: List

        Returns:
        formatted_sentence: String
    """
    words[0] = words[0].capitalize()
    last_word = words[len(words) - 1]
    last_char = last_word[len(last_word) - 1]
    formatted_sentence = ' '.join(words)
    if last_char in string.punctuation:
        formatted_sentence = formatted_sentence[:-1]
    formatted_sentence = formatted_sentence + "."
    return formatted_sentence

if __name__ == "__main__":
    words = file_or_string('manifesto.txt')
    word_list = words.split()
    print(higher_order_walk(word_list, 40))