from flask import Flask, render_template, request, redirect, url_for
import hashlib
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('url_shortener.db')
    conn.row_factory = sqlite3.Row
    return conn

def generate_short_url(long_url):
    """Generate a unique short URL using a hash function."""
    hash_object = hashlib.md5(long_url.encode())
    short_hash = hash_object.hexdigest()[:6]  # First 6 characters of MD5 hash
    return short_hash

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form.get('url')
    if long_url:
        short_url = generate_short_url(long_url)
        conn = get_db_connection()
        conn.execute('INSERT OR IGNORE INTO urls (long_url, short_url) VALUES (?, ?)',
                     (long_url, short_url))
        conn.commit()
        conn.close()
        short_url = request.host_url + short_url  # Full URL with host
        return render_template('index.html', short_url=short_url)
    return render_template('index.html', error="Please provide a valid URL")

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    conn = get_db_connection()
    url_row = conn.execute('SELECT long_url FROM urls WHERE short_url = ?',
                          (short_url,)).fetchone()
    conn.close()
    if url_row:
        return redirect(url_row['long_url'])
    return render_template('index.html', error="Shortened URL not found")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
