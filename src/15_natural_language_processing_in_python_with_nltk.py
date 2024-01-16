# Part 15: Natural Language Processing (NLP) in Python with NLTK

# Install NLTK: pip install nltk

# 1. Tokenization and Frequency Analysis
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

# Download NLTK resources (run once)
nltk.download('all')

# Sample text
text = ("Journey into the magical world of Harry Potter, "
        "a beloved fantasy series by J.K. Rowling. "
        "This enchanting saga follows the life of a young wizard, Harry, "
        "as he navigates the mysteries of Hogwarts School of Witchcraft and Wizardry. "
        "Alongside his friends Ron and Hermione, Harry faces dark forces, "
        "unravels secrets about his past, and battles the formidable Lord Voldemort. "
        "Filled with spells, magical creatures, and profound themes of friendship and bravery, "
        "the Harry Potter books captivate readers of all ages. "
        "The series has become a global phenomenon, "
        "inspiring a generation and leaving an enduring mark on literature and popular culture.")

# Tokenization
tokens = word_tokenize(text.lower())  # Convert to lowercase for consistency

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]

# Frequency Distribution
freq_dist = FreqDist(filtered_tokens)

# Print Results
print("NLP Results:")
print("Original Text:", text)
print("Tokenization and Filtering:", filtered_tokens)
print("Frequency Distribution:")
print(freq_dist.most_common(5))  # Display the top 5 most common words

# 2. Part-of-Speech Tagging
from nltk import pos_tag

# Part-of-Speech Tagging
pos_tags = pos_tag(filtered_tokens)

# Print Results
print("\nPart-of-Speech Tagging:")
print(pos_tags)

# 3. Named Entity Recognition (NER)
from nltk import ne_chunk

# Named Entity Recognition
ner_result = ne_chunk(pos_tags)

# Print Results
print("\nNamed Entity Recognition:")
print(ner_result)
