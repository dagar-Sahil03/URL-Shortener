import pyshorteners

class URLShortener:
    def __init__(self):
        # Initialize the URL shortening service
        self.shortener = pyshorteners.Shortener()

    def shorten_url(self, long_url):
        """
        Shortens the provided long URL using TinyURL service.

        :param long_url: The long URL to shorten.
        :return: The shortened URL.
        """
        try:
            # Use the TinyURL service to shorten the URL
            short_url = self.shortener.tinyurl.short(long_url)
            return short_url
        except Exception as e:
            # Handle any exceptions that may occur
            print(f"An error occurred while shortening the URL: {e}")
            return None

    def expand_url(self, short_url):
        """
        Expands the provided shortened URL back to the original long URL.

        :param short_url: The shortened URL to expand.
        :return: The original long URL.
        """
        try:
            # Expand the shortened URL
            long_url = self.shortener.tinyurl.expand(short_url)
            return long_url
        except Exception as e:
            # Handle any exceptions that may occur
            print(f"An error occurred while expanding the URL: {e}")
            return None

def main():
    url_shortener = URLShortener()

    # Input long URL from user
    long_url = input("Enter the long URL to shorten: ")
    
    # Shorten the URL
    short_url = url_shortener.shorten_url(long_url)
    if short_url:
        print(f"Shortened URL: {short_url}")
    
    # Optionally, expand the URL back to its original form
    expand_choice = input("Do you want to expand the shortened URL? (y/n): ").lower()
    if expand_choice == 'y' and short_url:
        original_url = url_shortener.expand_url(short_url)
        if original_url:
            print(f"Original URL: {original_url}")

if __name__ == "__main__":
    main()
