# ---------- LOCAL AI IMPORTS ----------

# Parser to convert raw text into a structured document format
from sumy.parsers.plaintext import PlaintextParser

# Tokenizer splits text into sentences (required for summarization)
from sumy.nlp.tokenizers import Tokenizer

# TextRank algorithm (extractive summarization method)
from sumy.summarizers.text_rank import TextRankSummarizer


# ---------- ONLINE AI IMPORT ----------
# Cohere API client for accessing external LLM (Large Language Model)
import cohere


# ---------- LOCAL SUMMARIZATION ----------
def summarize_local(text, sentence_count=5):
    """
    Generates a summary using a local algorithm (TextRank).

    Parameters:
        text (str): The input text to summarize
        sentence_count (int): Number of sentences in the summary

    Returns:
        str: A summarized version of the text
    """
    try:
        # Limit text size to prevent performance issues on large inputs
        text = text[:10000]

        # Convert raw text into a structured document using a tokenizer
        # Tokenizer("english") splits the text into sentences
        parser = PlaintextParser.from_string(text, Tokenizer("english"))

        # Initialize the TextRank summarizer
        summarizer = TextRankSummarizer()

        # Generate summary by selecting the most important sentences
        # Returns a sequence of sentence objects
        summary = summarizer(parser.document, sentence_count)

        # Convert sentence objects to strings and join into one paragraph
        result = " ".join([str(sentence) for sentence in summary])

        return result

    except Exception as e:
        # Catch and return any errors instead of crashing the app
        return f"Local AI Error: {str(e)}"


# ---------- ONLINE SUMMARIZATION ----------
def summarize_online(text, api_key):
    """
    Generates a summary using an external AI model via Cohere API.

    Parameters:
        text (str): The input text to summarize
        api_key (str): User-provided API key for authentication

    Returns:
        str: AI-generated summary
    """
    try:
        # Limit text size to comply with API input restrictions
        text = text[:5000]

        # Initialize Cohere client with user's API key
        co = cohere.Client(api_key)

        # Send request to AI model using chat interface
        response = co.chat(
            model="command-a-03-2025",  # Current supported Cohere model

            # Prompt instructing the AI what to do
            message=f"Summarize the following text clearly and concisely:\n\n{text}",

            # Controls randomness: lower = more factual, higher = more creative
            temperature=0.3
        )

        # Extract and return the generated text from the response
        return response.text

    except Exception as e:
        # Handle errors such as invalid API key, network issues, etc.
        return f"Online AI Error: {str(e)}"