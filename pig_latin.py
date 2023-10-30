def convert_to_pig_latin(sentence):
    # Split the sentence into words
    words = sentence.split()
    pig_latin_words = []

    for word in words:
        # Check if the word is not empty (e.g., due to extra spaces)
        if word:
            # Remove the first letter from the word
            first_letter = word[0]
            rest_of_word = word[1:]
            
            # Convert to lowercase to handle uppercase words
            first_letter = first_letter.lower()
            
            # Add the first letter at the end and append "ay"
            pig_latin_word = rest_of_word + first_letter + 'ay'
            
            # Capitalize the first letter of the original word if it was capitalized
            if word[0].isupper():
                pig_latin_word = pig_latin_word[0].upper() + pig_latin_word[1:]
            
            pig_latin_words.append(pig_latin_word)
        else:
            pig_latin_words.append('')  # Add an empty string for extra spaces

    # Join the Pig Latin words back into a sentence
    pig_latin_sentence = ' '.join(pig_latin_words)
    
    return pig_latin_sentence

# Example usage:
english_sentence = "I slept most of the night"
pig_latin_result = convert_to_pig_latin(english_sentence)
print("English:", english_sentence)
print("Pig Latin:", pig_latin_result)
