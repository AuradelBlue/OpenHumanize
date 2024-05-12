document.getElementById('textForm').onsubmit = function(event) {
    event.preventDefault();
    var formData = new FormData(this);
    fetch('/parse', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => displaySentences(data))
    .catch(error => console.error('Error:', error));
};

function displaySentences(data) {
    const container = document.getElementById('sentenceList');
    container.innerHTML = '';  // Clear existing entries

    data.forEach((sentence, index) => {
        // Create sentence header
        const header = document.createElement('div');
        header.className = 'sentence-header';
        header.textContent = `Sentence ${index + 1}`;
        header.style.cursor = 'pointer';
        header.style.fontWeight = 'bold';

        // Create hidden div for sentence details
        const details = document.createElement('div');
        details.className = 'sentence-details';
        details.style.display = 'none';
        details.style.paddingLeft = '20px';

        // Populate details
        sentence.tokens.forEach(token => {
            const tokenDiv = document.createElement('div');
            tokenDiv.textContent = `${token.word} (${token.dep}, ${token.pos})`;
            details.appendChild(tokenDiv);
        });

        // Toggle details on click
        header.onclick = function() {
            const isVisible = details.style.display === 'block';
            details.style.display = isVisible ? 'none' : 'block';
        };

        // Append to container
        container.appendChild(header);
        container.appendChild(details);
    });
}
