from flask import Flask, request, render_template,session

app = Flask(__name__, template_folder=r'C:\Users\יותם בראון\Desktop\templates')
IMG_FOLDER = os.path.join('static', 'IMG')
UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/analyze', methods=["GET",'POST'])
def analyze():
    # Get the uploaded file from the request data
    file = request.files['resume_file']
    file_path1 = os.path.join(r'C:\Users\יותם בראון\Desktop\templates',file.filename)
    # Save the file to a temporary location on the server
    file_path = os.path.join(r'C:\Users\יותם בראון\Desktop\templates\tmp', file.filename)
    file.save(file_path)
    print(file_path)
    # Create a ResumeAnalyzer object and analyze the resume
    #analyzer = ResumeAnalyzer(file_path)
    #analysis = analyzer.analyze()
    analysis=apply_word_cloud2(file_path)[0]
    print(analysis)
    analysis1=apply_word_cloud2(file_path)[1]
    print(analysis1)
    analysis_2=apply_word_cloud3(file_path1)
 
    # Render the results page and pass the analysis results as data
    response = render_template('results.html', analysis=analysis,analysis1=analysis1)

    return response

@app.route('/show_image', methods=["GET", "POST"])
def displayImage():
    img_file_path = session.get("uploaded_img_file_path", None)
    # Save uploaded image file to UPLOAD_FOLDER if a file was uploaded
    if request.method == 'POST':
        uploaded_img = request.files['uploaded_img']
        uploaded_img.save(os.path.join(app.config['UPLOAD_FOLDER'], 'Wordcloud.png'))
        session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], 'Wordcloud.png')
    print(img_file_path)
    if not img_file_path:
        img_file_path = r'C:\Users\יותם בראון\Desktop\templates\Wordcloud.png'
    # Render show_image.html template and pass user_image variable
    response = render_template('show_image.html', user_image=img_file_path)
    return response



if __name__ == '__main__':
    app.run()
