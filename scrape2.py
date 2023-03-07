# Import the libraries
# Import the libraries
import requests
from bs4 import BeautifulSoup
import os 
import string

# Define a function to scrape the website
def scrape_website(url):
    # Try to get the HTML content
    try:
        response = requests.get(url)
        html = response.text
    # If there is a connection error, print a message and return
    except requests.exceptions.ConnectionError:
        print("Connection error. Please check the URL and your internet connection.")
        return
    # If there is any other error, print a message and return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    # Find all p tags
    p_tags = soup.find_all("p")

    # Create a list to store the text from the p tags
    p_text = []

    # Iterate over the p tags and extract their text
    for tag in p_tags:
        p_text.append(tag.get_text())

    # Join the text from the p tags into a single string
    text = "\n".join(p_text)

    # Find the title tag
    title = soup.find("title")

    # Extract the text from the title tag
    title_text = title.get_text()

    # Create the output file name with the title text
    output_folder = r"E:\Python\Scrape"
    allowed_characters = string.ascii_letters + string.digits
    title_text =  "".join([char for char in title_text if char in allowed_characters])
    output_file = os.path.join(output_folder, title_text + ".txt")

    # Try to open the output file and write the text
    try:
        with open(output_file, "w", encoding="uft-8") as f:
            f.write(text)
    # If there is a file error, print a message and return
    except IOError:
        print("File error. Please check the file name and permissions.")
        return
    # If there is any other error, print a message and return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Print a success message
    print(f"Successfully scraped {url} and saved to {output_file}")

# Open the link.txt file and read the URL
with open(r"E:\Python\Scrape\link.txt", "r") as f:
    url = f.read().strip()

# Check the file permissions of the current working directory
mode = os.stat(".").st_mode
# If the current user does not have write permission, change it
if not mode & os.W_OK:
    os.chmod(".", mode | os.W_OK)

# Call the scrape_website function with the URL
scrape_website(url)