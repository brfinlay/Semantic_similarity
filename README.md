                              
                                             **Summary of Each Script**
**1. master_similarity_score.py**
     
   *- Messy starting point script containing all processes. The other scripts are cleaner snippets of what this does*


**2. master_definitions&synsets.py**
      
   *- Takes word list (n = 273) gets their synset definitions, and assigns an appropriate synset to each word. See Google Drive for a spreadsheet of all the synsets, corresponding definitions, and final synsets chosen.*


**3. heatmap_pdf**
      
   *- Assigns variables to the correct synsets determined in* 'master_definitions&synsets.py'.
      
   *- For each category (Huth, Konkle etc.), lists of assigned synset variables were compiled.*
      
   *- Uses Leacock_Chodorow (LCH) similarity function to create a dictionary in form*: {(syn1, syn2): LCH_score}.
      
   *- Converts dictionary into a matrix. Converts matrix into a* respresentational similarity matrix (RSM) *for each category*
      
   Note that these RSM.pdf's are large, and consequently difficult to read.
      
   https://drive.google.com/drive/folders/1ivPSicHmdq38gUWnVMo9msDP8p9N4Xwc


**4. interactive_heatmap.py**
      
   *- Assigns synsets to variable similar to* (3)
      
   *- Variables categorised into Konkle dimensions*
      
   *- Calculates LCH similarity to create a dictionary in form*: {(syn1, syn2): LCH_score}
      
   *- Dictionary saved as matrix.csv, headings added on excel, and reopened in script*
      
   *- Uses* plotly *to create an interactive RSM heatmap*
      
   Does not work on full list of words. Works on a small sample. 
      
   https://drive.google.com/drive/folders/1ivPSicHmdq38gUWnVMo9msDP8p9N4Xwc
       
       
5. WUP_similarity folder
      
      *NOT RELEVANT TO THIS PROJECT*
      
      
6. Normalise_LCH_Scores
      
      *NOT RELEVANT*



                                          **A Guide to Using NLTK's WordNet**
                                              
import wordnet as wn

To get the synset of a word: wn.synsets('word')

A specific synset index can be specified by calling wn.synsets('word')[index]

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
*where (synx) denotes the synset for a particular (wordx)


  
