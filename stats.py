

class Stats():
    def __init__(self, filepath):
        self.filepath = filepath

    def get_book_text(self):
        with open(self.filepath) as f:
            contents = f.read()

        return contents

    def num_of_words(self, text):

        return len(text.split())

    def num_of_chars(self, text):
        text_lower = text.lower()
        count_of_chars = {char: text_lower.count(char) for char in set(text_lower)}

        return count_of_chars
         
    
    def sort_characters(self, dict):
        sorted_count = []
        for k,v in dict.items():
            sorted_count.append({"char": k, "num": v})
        
        def sort_on(item):
            return item["num"]
        
        sorted_count.sort(reverse=True, key=sort_on)

        return sorted_count

    
    def output(self):
        contents = self.get_book_text()
        count = self.num_of_words(contents)
        char_count = self.num_of_chars(contents)
        sorted_count = self.sort_characters(char_count)

        print(f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {count} total words'
--------- Character Count -------""")
        for item in sorted_count:
            if item["char"].isalpha():
                print(f'{item["char"]}: {item["num"]}')
        print(f'============= END ===============')