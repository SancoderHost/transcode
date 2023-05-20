from flask import Flask, render_template, request
import ffmpeg 
import os 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and file.filename.endswith('.mp4'):
        input_file = file.filename
        output_file = 'output.mp4'

        # Save the input file temporarily
        file.save(input_file)

        try:
            # Transcode the video to 360p resolution
            ffmpeg.input(input_file).output(output_file, vf='scale=640:360').run()

            # Optionally, perform further processing on the transcoded file

            return 'File uploaded and transcoded successfully!'
        except ffmpeg.Error as e:
            return f'Transcoding error: {str(e)}'
        finally:
            # Clean up temporary files
            os.remove(input_file)
    else:
        return 'Invalid file format. Please upload an MP4 file.'

if __name__ == '__main__':
    app.run(debug=True)

