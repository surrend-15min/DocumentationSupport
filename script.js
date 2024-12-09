// Carica la lista dei file disponibili
fetch('/files') // Route che restituisce la lista dei file
    .then(response => response.json())
    .then(files => {
        const fileList = document.getElementById('file-list');
        files.forEach(file => {
            const li = document.createElement('li');
            li.innerHTML = `<a href="#" onclick="viewFile('${file}')">${file}</a>`;
            fileList.appendChild(li);
        });
    });

function viewFile(fileName) {
    fetch(`/files/${fileName}`) // Route che restituisce il contenuto del file
        .then(response => response.text())
        .then(content => {
            document.getElementById('file-content').innerText = content;
        });
}
