from flask import Flask, request, send_file
from pytube import YouTube
import os
app = Flask(__name__)
@app.route('/download', methods=['POST'])
def download():
    link = request.form.get('link')
    fileType = request.form.get('fileType')
    resolution = request.form.get('resolution')
    SAVE_PATH = "downloads/"

    try:
        yt = YouTube(link)
        if fileType == 'video':
            streams = yt.streams.filter(file_extension='mp4').order_by('resolution')
        elif fileType == 'audio':
            streams = yt.streams.filter(only_audio=True).order_by('abr')

        if resolution == 'highest':
            d_stream = streams.desc().first()
        else:
            d_stream = streams.asc().first()

        filename = 'downloaded_file.mp4' if fileType == 'video' else 'downloaded_file.mp3'
        d_stream.download(output_path=SAVE_PATH, filename=filename)
        return send_file(os.path.join(SAVE_PATH, filename), as_attachment=True)

    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    app.run(debug=True)
