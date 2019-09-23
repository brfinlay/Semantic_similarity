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
  

  
