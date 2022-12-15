# Lazy-HR

To use this project, you will need to have Python 3 and the following libraries installed:

re

matplotlib

wordcloud

pdfminer

docx2pdf

nltk

stop_words

pythoncom

win32com

Once you have these installed, you can clone the repository and run the script with the following command:

### python resume_analyzer.py /path/to/resume.pdf

### This will generate a word cloud of the most frequently used words in the resume, as well as a count of the number of occurrences of words related to data science.

## Alternatively, you can import the ResumeAnalyzer class and use it in your own Python code:


from resume_analyzer import ResumeAnalyzer

resume_file = '/path/to/resume.pdf'

analyzer = ResumeAnalyzer(resume_file)
resume_text = analyzer.load_resume()
processed_text = analyzer.process_text()
words = analyzer.extract_words(processed_text)
data_science_word_count = analyzer.count_data_science_words(words)
processed_words = analyzer.process_word(words)
data_science_word_occurrences = analyzer.count_data_science_words_occurrences(processed_words)


ou can then use the extracted text, words, and counts in your own analysis.
