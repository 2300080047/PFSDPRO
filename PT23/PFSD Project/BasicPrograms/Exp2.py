import string


# Function to read the text file and clean the text
def read_and_clean_file(file_path, exclude_stop_words=True):
    # List of common stop words
    stop_words = {'the', 'is', 'in', 'it', 'and', 'a', 'to', 'of', 'that', 'this', 'with', 'for', 'on', 'as', 'at',
                  'by', 'an', 'be', 'are', 'was', 'were', 'but', 'not'}

    with open(file_path, 'r') as file:
        # Read the file content
        text = file.read()

        # Convert to lower case to ignore case
        text = text.lower()

        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))

        # Split text into words
        words = text.split()

        if exclude_stop_words:
            # Remove stop words
            words = [word for word in words if word not in stop_words]

        return words


# Function to count words in the text
def count_words(words):
    return len(words)


# Main function
def main():
    file_path = 'sample.txt'
    exclude_stop_words = True

    words = read_and_clean_file(file_path, exclude_stop_words)
    word_count = count_words(words)

    print(f"Number of words in the file: {word_count}")


if __name__ == "__main__":
    main()
