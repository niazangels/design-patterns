"""
Flyweight Coding Exercise
You are given a class called Sentence , which takes a string such as 'hello world'. You need to provide an interface such that the indexer returns a flyweight that can be used to capitalize a particular word in the sentence.

Typical use would be something like:

sentence = Sentence('hello world')
sentence[1].capitalize = True
print(sentence)  # writes "hello WORLD"
"""


class WordFormatter:
    def __init__(self, plaintext):
        self.plaintext_words = plaintext.split(" ")
        self.formatting = {}

    def __getitem__(self, index):
        class Word:
            def __init__(self):
                self.capitalize = False

            def __repr__(self):
                return f"<Word capitalize={self.capitalize}>"

        self.formatting[index] = Word()
        return self.formatting[index]

    def __repr__(self):
        result = []
        print(self.formatting)
        for word_index, word in enumerate(self.plaintext_words):
            if word_index in self.formatting and self.formatting[word_index].capitalize:
                word = word.upper()
            result.append(word)
        return " ".join(result)


if __name__ == "__main__":
    sentence = WordFormatter("Hakuna Mattata! It means no worries :)")
    sentence[2].capitalize = True
    print(sentence)
