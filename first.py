from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and file.filename.endswith('.mp4'):
        # Save the file or perform further processing
        file.save(file.filename)
        return 'File uploaded successfully!'
    else:
        return 'Invalid file format. Please upload an MP4 file.'

if __name__ == '__main__':
    app.run(debug=True)

