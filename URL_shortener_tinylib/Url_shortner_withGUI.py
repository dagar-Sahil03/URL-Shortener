from flask import Flask, render_template, request, redirect, url_for
import pyshorteners

# Initialize Flask app
app = Flask(__name__)

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
            print(f"An error occurred while shortening the URL: {e}")
            return None

    def expand_url(self, short_url):
        """
        Expands the provided shortened URL back to the original long URL.

        :param short_url: The shortened URL to expand.
        :return: The original long URL.
        """
        try:
            long_url = self.shortener.tinyurl.expand(short_url)
            return long_url
        except Exception as e:
            print(f"An error occurred while expanding the URL: {e}")
            return None

# Instantiate the URLShortener class
url_shortener = URLShortener()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form.get('url')
    if long_url:
        short_url = url_shortener.shorten_url(long_url)
        return render_template('index.html', short_url=short_url)
    return render_template('index.html', error="Please provide a valid URL")

@app.route('/expand', methods=['POST'])
def expand():
    short_url = request.form.get('short_url')
    if short_url:
        original_url = url_shortener.expand_url(short_url)
        return render_template('index.html', original_url=original_url)
    return render_template('index.html', error="Please provide a valid shortened URL")

if __name__ == '__main__':
    app.run(debug=True)
