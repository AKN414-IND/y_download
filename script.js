document.getElementById("downloadForm").addEventListener("submit", function (event) {
    event.preventDefault();
    const link = document.getElementById("link").value;
    fetch('/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `link=${link}`
    })
    .then(response => response.blob())
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'video.mp4';
        a.click();
    })
    .catch(error => alert('An error occurred: ' + error));
});
