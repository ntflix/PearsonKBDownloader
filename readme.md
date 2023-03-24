# Pearson Knowledge Base Downloader

Downloads the entire [Pearson Qualifications, Resource & Digital Support Knowledge Base](https://support.pearson.com/uk/s/).

This was made out of frustration after traditional web scraping proved to be ineffective due to the JavaScript heavy nature of the site.

This will totally slow down your computer as it spins up hundreds of instances of Google Chrome to download the site.
Would give it a couple mins to run on an average computer.

## Usage

Ensure you edit `URLS_FILE`, `OUTPUT_DIR`, and `CHROME_PATH` in `download.py`.
This has already a list of all the URLs to download, but you can add more if you want. This is the purpose of `URLS_FILE`.
I created this list using Screaming Frog SEO Spider.
