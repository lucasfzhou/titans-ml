function predictImage(form) {
    const data = new FormData(form);

    fetch('/api/predict', {
        method: 'POST',
        body: data
    }).then((response) => {
        return response.json();
    }).then((result) => {
        const resultDiv = document.getElementById('resultDiv');
        resultDiv.innerHTML = '';
        result.forEach((pred) => {
            const roundedConf = Math.round(pred.confidence * 1000) / 1000;
            resultDiv.innerHTML += `<p>${pred.label}: ${roundedConf}<\p>`;
        });
    });

    const resultDiv = document.getElementById('resultDiv');
    resultDiv.innerHTML = '<p>Predicting...<\p>'
    resultDiv.innerHTML += '<div class="loader"></div>'

    // stay on original page
    return false;
}