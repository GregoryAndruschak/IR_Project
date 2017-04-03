import os


class Book(object):
    amount = 0
    words = []
    titles = []

    def __init__(self, title, text):
        self.id = Book.amount
        Book.amount += 1
        self.title = title
        self.text = text
        Book.titles.append(self.title)


class Word(object):
    amount = 0

    def __init__(self, word, file_id):
        Word.amount += 1
        self.word = word
        self.file_id = [file_id]

    def __cmp__(self, other):
        if self.word > other.word:
            return 1
        elif self.word < other.word:
            return -1
        else:
            return 0

    def tostring(self):
        return str(self.word) + ' ' + str(self.file_id)


def make_array(dir):
    result = []
    for name in os.listdir(dir):
        if name == ".DS_Store":
            continue
        else:
            print(name)
            name = '/Users/Greg/Downloads/BabylonLib/' + name
            temp = open(name, 'r').read()
            result.append(temp)
    return result


def objectify(files):
    books = []
    counter = 0
    for f in files:
        title = ''
        text = ''
        end_of_title = False
        tl = []  # three last
        for char in f:
            tl.append(char)
            if len(tl) == 3 and tl[0] == '\n' and tl[1] == '\n' and tl[2] == '\n':
                break
            if char == '\n' and end_of_title is False:
                end_of_title = True
                continue
            elif end_of_title is False:
                title += char
            else:
                text += char
            if len(tl) == 3:
                del tl[0]
        books.append(Book(title, fws(text)))
        counter += 1
        print('{}) Book is objectified!'.format(counter))
    return books


def fws(file):  # file word splitter
    temp = ''
    file.replace('\n', ' ')
    for i in range(len(file)):
        if not file[i].isalpha() and not file[i] is ' ':
            temp += ' '
        elif file[i].isalpha() or file[i] is ' ':
            temp += file[i]
    almost_result = temp.split(' ')
    result = []
    for w in almost_result:
        if len(w) > 20:
            continue
        else:
            t = Word(w, Book.amount)
            result.append(t)
    return result


def make_dictionary_and_ii(books):
    for b in books:
        t = b.text
        Book.words += t
        Book.words.sort(key=lambda x: x.word)
    res = []
    is_first = True
    for wo in range(len(Book.words)):
        if Book.words[wo].word == '' or Book.words[wo].word == ' ':
            continue
        if is_first:
            res.append(Book.words[wo])
            is_first = False
        else:
            if Book.words[wo].word == res[-1].word:
                if res[-1].file_id not in Book.words[wo].file_id:
                    for id in Book.words[wo].file_id:
                        if id not in res[-1].file_id:
                            res[-1].file_id.append(id)
                    res[-1].file_id.sort()
                continue
            else:
                res.append(Book.words[wo])
    del res[0]
    print("Dictionary and invert index are created")
    Book.words = res


def serialize_dictionary():
    out = open('dictionary with ii.txt', 'w')
    out2 = open('dictionary.txt', 'w')
    out.write('Number of books: {}\n'.format(Book.amount))
    out2.write('Number of books: {}\n'.format(Book.amount))
    out.write('Total amount of words: {}\n'.format(Word.amount))
    out2.write('Total amount of words: {}\n'.format(Word.amount))
    out.write('Amount of words in the dictionary: {}\n\n'.format(len(Book.words)-1))
    out2.write('Amount of words in the dictionary: {}\n\n'.format(len(Book.words)-1))
    for i in range(len(Book.words)):
        if i == 0:
            continue
        else:
            out.write(Book.words[i].tostring() + '\n')
            out2.write(Book.words[i].word + '\n')
    out.close()
    out2.close()


def main():
    print('Loading...')
    files = make_array('/Users/Greg/Downloads/BabylonLib/')
    books = objectify(files)
    make_dictionary_and_ii(books)
    serialize_dictionary()


if __name__ == '__main__':
    main()

