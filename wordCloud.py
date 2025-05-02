#!/usr/bin/env python3

"""
This script creates a wordcloud.
The script takes a textfile called 'wordcloud.txt' and removes stop words, punctuation and numbers.
Then it generates a wordcloud image and saves it as 'wordcloud.png'.
The wordcloud is generated using the WordCloud library and matplotlib for visualization.

Author: Jake the Snake
Date: 2025-05-02
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
from collections import Counter

def create_wordcloud(text_file, output_file='wordcloud.png', 
                     width=800, height=400, max_words=100, 
                     background_color='white'):
    """
    Create a word cloud from a text file
    
    Parameters:
    -----------
    text_file : str
        Path to the text file
    output_file : str
        Path to save the generated word cloud image
    width : int
        Width of the word cloud image
    height : int
        Height of the word cloud image
    max_words : int
        Maximum number of words to include in the word cloud
    background_color : str
        Background color of the word cloud
    """
    # Read the text file
    with open(text_file, 'r') as file:
        text = file.read()
    
    # Data cleaning
    # Convert to lowercase
    text = text.lower()
    
    # Remove numbers and punctuation
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    
    # Split into words
    words = text.split()
    
    # Remove common stopwords
    stopwords = {'and', 'the', 'to', 'of', 'is', 'in', 'a', 'for', 'with', 'on', 
                'by', 'at', 'from', 'as', 'are', 'that', 'be', 'this', 'an', 'we',
                'has', 'have', 'but', 'not', 'no', 'it', 'its', 'can', 'all', 'see',
                'our', 'their', 'there', 'due', 'one', 'two', 'three', 'however',
                'been', 'was', 'will', 'would', 'should', 'could', 'what', 'which',
                'where', 'when', 'how', 'who', 'or', 'if', 'very', 'also', 'than',
                'thou','thy','they','them','he','him','she','her','us','we','you','your',
                'thee','thine','my','me','itself','himself','herself','itself','themselves','those'}
    
    # Create filtered word list
    filtered_words = [word for word in words if word not in stopwords and len(word) > 2]
    
    # Count word frequencies
    word_counts = Counter(filtered_words)
    
    # Create word cloud
    wordcloud = WordCloud(
        width=width,
        height=height,
        max_words=max_words,
        background_color=background_color,
        contour_width=1,
        contour_color='steelblue',
        colormap='viridis',
        prefer_horizontal=0.9,
        relative_scaling=0.5,
    ).generate_from_frequencies(word_counts)
    
    # Plot the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    
    # Save the word cloud
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Word cloud created and saved as {output_file}")
    
    # Return the top 10 most common words
    return word_counts.most_common(10)

if __name__ == "__main__":
    # Create word cloud from the text file
    input_file = "wordcloud.txt"  # Update with your file path if needed
    top_words = create_wordcloud(input_file)
    
    print("\nTop 10 most frequent words:")
    for word, count in top_words:
        print(f"{word}: {count}")