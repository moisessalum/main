import re
from corpora_tools import *


def read_conversations(storage_path, storage_dir):
   filename = storage_path + "/" + storage_dir + "/cornell movie-dialogs corpus/movie_conversations.txt"
   with open(filename, "r", encoding="ISO-8859-1") as fh:
       conversations_chunks = [line.split(" +++$+++ ") for line in fh]
   return [re.sub('[[\'\]]', '', el[3].strip()).split(", ") for el in conversations_chunks]

def read_lines(storage_path, storage_dir):
   filename = storage_path + "/" + storage_dir + "/cornell movie-dialogs corpus/movie_lines.txt"
   with open(filename, "r", encoding="ISO-8859-1") as fh:
       lines_chunks = [line.split(" +++$+++ ") for line in fh]
   return {line[0]: line[-1].strip() for line in lines_chunks}

def get_tokenized_sequencial_sentences(list_of_lines, line_text):
   for line in list_of_lines:
       for i in range(len(line) - 1):
           yield (line_text[line[i]].split(' '), line_text[line[i+1]].split(' '))

def cornell_corpora(storage_path="c:/Users/mrodriguez/Documents/github/main", storage_dir="machine_learning"):
    conversations = read_conversations(storage_path, storage_dir)
    lines = read_lines(storage_path, storage_dir)
    return tuple(zip(*list(get_tokenized_sequencial_sentences(conversations,lines))))

if __name__ == '__main__':
    sen_l1, sen_l2 = cornell_corpora()
    clean_sen_l1 = [clean_sentence(s) for s in sen_l1]
    clean_sen_l2 = [clean_sentence(s) for s in sen_l2]

    print(clean_sen_l2)
