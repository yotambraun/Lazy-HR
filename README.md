# Lazy-HR


#### Image for Example:

<img width="622" alt="menu" src="https://user-images.githubusercontent.com/57616193/207872843-717822e3-1bb9-4e27-b12a-96adf495a246.PNG">

<img width="960" alt="resume analyzer result" src="https://user-images.githubusercontent.com/57616193/207872882-549e064e-9885-4586-b0ab-3d9154627e19.PNG">

<img width="532" alt="apply without the web app" src="https://user-images.githubusercontent.com/57616193/207872908-2929f84b-402f-42b1-8327-7da34a82f57d.PNG">

![wordcloud](https://user-images.githubusercontent.com/57616193/207872932-5688ed25-ad68-42d7-b2db-482f099f576d.png)




To use this project, you will need to have Python 3 and the following libraries installed:

FLASK

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

```python resume_analyzer.py /path/to/resume.pdf ```

### This project is a resume analyzer that extracts text from a resume file (in PDF or DOCX format), and then counts the number of occurrences of words related to data science in the extracted text. It does this by using regular expressions to extract words from the text, and then using a set of words related to data science to count the number of occurrences of those words in the extracted text. The project includes a ResumeAnalyzer class that has several methods for loading and processing a resume file, extracting words from the text, and counting the occurrences of words related to data science. This class can be used in other Python projects to analyze resumes for the presence of data science-related words.

## Alternatively, you can import the ResumeAnalyzer class and use it in your own Python code:


```from resume_analyzer import ResumeAnalyzer

resume_file = '/path/to/resume.pdf'

analyzer = ResumeAnalyzer(resume_file)
resume_text = analyzer.load_resume()
processed_text = analyzer.process_text()
words = analyzer.extract_words(processed_text)
data_science_word_count = analyzer.count_data_science_words(words)
processed_words = analyzer.process_word(words)
data_science_word_occurrences = analyzer.count_data_science_words_occurrences(processed_words)```


## or can then use the extracted text, words, and counts in your own analysis.


