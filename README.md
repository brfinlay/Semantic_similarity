Given you have imported wordnet as wn

To get the synset of a word:
wn.synsets('word')

A specific synset index can be specified by calling wn.synsets('word')[num]

----------------------------------------------------------------------------------------------
  
To get the definition of a synset:
wn.synsets('word').definition()
  
or

Assign a variable to the synset, and:

variable.definition()
  
-----------------------------------------------------------------------------------------------
Leacock-Chodorow (LCH) similarity was used as a measure of semantic similarity.
To get LCH similarity fo two words:
syn1.lch_similarity(syn2)
where syn(x) denotes the synset for a particular word(x)


  
