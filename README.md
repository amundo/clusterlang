You have a file with two languages in it.

## Is it possible to automatically group the words in a file in two unknown languages by language?

Here's my attempt.

It goes like this:

First, you tally up the bigrams in each word. For example, _abracadabra_ gives:

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


This works more or less independently of language. Here's [Spanish](http://adelanteschool.org/info.html):

    13003 :  8.0 educational education
    13004 :  8.0 están está
    13005 :  9.0 Comité Comite
    13006 :  9.0 School (School
    13007 :  9.0 ensures ensure
    13008 :  9.0 parent parents
    13009 :  9.0 Council Council)
    13010 :  9.0 English (English
    13011 :  9.0 Learners Learner
    13012 :  9.0 asegura asegurar
    13013 :  9.0 drastico drastic
    13014 :  9.0 nuestros nuestro
    13015 :  9.0 program programa
    13016 :  9.0 student students
    13017 :  9.0 Calendar/ Calendar
    13018 :  9.0 programas programa
    13019 :  9.0 Presidente President
    13020 :  9.0 importante important
    13021 :  9.0 voluntarios voluntario
    13022 :  9.0 estudiante estudiantes

and here's [Welsh](http://www.swap.ac.uk/policyregulation/wales.html):

     11711 :  8.0 Wales; Wales
     11712 :  8.0 gwell gwella
     11713 :  9.0 Developmental Development
     11714 :  9.0 addysg addysgu
     11715 :  9.0 Academi (Academi
     11716 :  9.0 Academy) Academy
     11717 :  9.0 Council Councils
     11718 :  9.0 Nghymru; Nghymru
     11719 :  9.0 Students Student
     11720 :  9.0 include includes
     11721 :  9.0 promotes promote
     11722 :  9.0 student students
     11723 :  9.0 supports support
     11724 :  9.0 arbennig’ arbennig
     11725 :  9.0 Department Departments
     11726 :  9.0 ‘Devolution Devolution
     11727 :  9.0 ‘Fframwaith Fframwaith
     11728 :  9.0 developments development

Again, some spurious stuff in there, but it still seems to be legit on the whole.

Now it gets tricky. How do we group these pairs into two languages?


