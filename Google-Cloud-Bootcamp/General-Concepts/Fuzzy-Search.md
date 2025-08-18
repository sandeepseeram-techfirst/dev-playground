# Fuzzy Search 
Fuzzy search is a search technique that finds matches even when the search query doesn't perfectly match corresponding data.

## How do fuzzy searches work?
Fuzzy searches employ various algorithms and techniques to determine the similarity between two strings of text, the search query, and the potential match in the data. 

These algorithms often rely on concepts like:

### Levenshtein distance: 
This determines the lowest number of edits (like insertions, deletions, or substitutions) required to transform one string into another. A lower Levenshtein distance indicates greater similarity. For instance, "kitten" and "sitting" have a Levenshtein distance of 3.

### Cosine similarity: 
This calculates the cosine of the angle between two vectors representing the words or strings. A cosine similarity of 1 represents an exact match, while 0 indicates no similarity. This is commonly used to compare documents based on their word content.

### Phonetic algorithms: 
These techniques, like Soundex or Metaphone, encode words based on their pronunciation. This helps in finding words that sound similar even if they have different spellings, such as "Smith" and "Smyth."