from random import * 
import codecs, sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
from math import floor, sqrt
from urllib import urlopen
from clusters import * 

"""
Given a wordlist containing words in two languages, can we come up with an 
unsupervised algorithm to try to group the words by language? 

"""

def freq(seq):
  fq = {}
  for e in seq:
    if e not in fq: fq[e] = 0
    fq[e] += 1
  return fq

def ngrams(n, seq):
  return [seq[i:i+n] for i in range(len(seq)-n+1)]

def bigrams(seq): 
  return ngrams(2, seq) 

  
def scalar(vec):
  return sqrt(sum([k*k for v,k in vec.items()]))

def sim(v, w):
  total = 0 
  for elem in v:
    if elem in w:
      total += v[elem] * w[elem]
  return float(total) / (scalar(v) * scalar(w))

def at_least_n_letters(words, n=3):
  return filter(lambda w: len(w) > n, words)


def model(text):
  return freq(bigrams(text))

def divide(words):
  scored = []
  seen = set()
  for i in words:
    for j in words:
      if i != j and i.lower() != j.lower() and len(set(i).intersection(set(j))) > 2 and (i,j) not in seen and (j,i) not in seen:
        score = sim(model(i),model(j))
        if score > 0:
          scored.append((score, i, j))
          seen.add((i,j))
  return sorted(scored)

def dump_scores(scores):
  for nth, (n,i,j) in enumerate(scores): 
    if n > 0: print nth, ": ", floor(10 * n), i, j
  

if __name__ == "__main__":
  from unicodedata import normalize 
  import sys
  #song =  urlopen('http://localhost/s/languages/hawaiian/facing_future/gloss.henehene').read().decode('utf-8')
  url = sys.argv[1]
  song =  urlopen('http://localhost/s/spider/proxy.php?url=' + url).read().decode('utf-8')
  song = normalize('NFKD', song)
  song = song.replace('.',' ').replace('?',' ').replace(',',' ').replace(':',' ')
  lines = song.splitlines()
  words = [] 
  [words.extend(line.split()) for line in lines]
  shuffle(words)
  words = words[:1000]
  words = at_least_n_letters(words)
  vocab = set(words)
  dump_scores(divide(vocab)) 
  
