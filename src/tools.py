from smolagents import tool

@tool
def fetch_ai_news_rss() -> dict:
    """
    Fetches and parses the latest AI news from a specific RSS feed.

    This function retrieves the most recent entry from the AI News RSS feed,
    extracts headlines, their corresponding content, and any links within the content.
    It returns them as a dictionary. The function uses regular expressions to clean
    HTML tags from the text and extract links.

    Returns:
        dict: A dictionary where keys are headlines (str) and values are
        dictionaries containing 'content' (str) and 'links' (list of str)
        for each news item.

    Note:
        - The function relies on the 'feedparser' library to parse the RSS feed.
        - HTML sanitization is applied during parsing.
        - The function assumes a specific structure in the RSS feed's summary field.
        - Links are extracted from the content and added to the dictionary.
    """
    import feedparser
    import re

    result = feedparser.parse("https://buttondown.com/ainews/rss", sanitize_html=True).entries[0].summary

    headlines = re.findall(r"(?s)<h3.*?>(?P<headline>.*?)</h3>(.*?)<hr />", result)

    result_dict = {}
    for headline, content in headlines:
        headline_text = re.sub(r"<[^>]+>", "", headline).strip()
        content_text = re.sub(r"<[^>]+>", "", content).strip()
        links = re.findall(r'https?://\S+', content)
        
        result_dict[headline_text] = {
            'content': content_text,
            'links': links
        }

    return result_dict

@tool
def save_to_text_file(file_path: str, content: str) -> None:
    """
    Saves the given content to a text file at the specified file path.

    Args:
        file_path: A string representing the file path where the content should be saved as a text file.
        content: The content to be written to the file.

    Returns:
        None
    """
    with open(file_path, 'w') as file:
        file.write(content)
 