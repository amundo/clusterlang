You have a file with two languages in it.

Is it possible to automatically group the words by language?

Here's my attempt.

It goes like this:

count up the bigrams in each word. For example, _abracadabra_ gives:

    ca 1
    da 1
    ac 1
    ad 1
    ra 2
    ab 2
    br 2

Let's call this thing a "model." Now, we want to find pairs of words that have "similar" models. 

Believe it or not, you can do that with [Cosine similarity](http://en.wikipedia.org/wiki/Cosine_similarity).

We randomly choose a bunch of pairs of words from the bilingual text, and calculate their similarity according to this formula. Now, words with _very_ similar models are highly likely to be from the same language. So we skim off the pairs of words that have high scores. We assume that in most of these pairs of words, both are from the same language.

Here's the tail end of some example data from a page in Hawaiian and English (http://www.nawahi.org/index.html):

    567:  5.0 hoʻomohala hoʻōla
    568:  5.0 waiwai Hawaiʻi
    569:  5.0 Kālaiʻike ʻike
    570:  5.0 Nāwahī Nāwahīokalaniʻōpuʻu
    571:  5.0 mana ʻAlemanaka
    572:  5.0 Manaʻo ʻohana
    573:  6.0 Hawaiian Hawaiʻi
    574:  6.0 ʻohana Hanana/Hoʻolaha
    575:  6.0 kumu hoʻokumu
    576:  6.0 limahana Kumu/Limahana
    577:  6.0 limahana mana
    578:  6.0 kula Kula
    579:  6.0 ʻano ʻana
    580:  6.0 ʻike like
    581:  6.0 chosen those
    582:  7.0 speak speaking
    583:  7.0 naʻauao hoʻonaʻauao
    584:  7.0 school School
    585:  8.0 main maintain
    586:  9.0 languages language

As you can see, these results are not perfect. _ʻike_ is Hawaiian and _like_ is English. Well actually, _like_ is English _and_ Hawaiian. (There's a freeway called Likelike! Rhymes with _deejay, deejay_ not _spike, spike!_) But the majority of pairs here are from the same language. 

Now it gets tricky. How do we group these pairs into two languages?


