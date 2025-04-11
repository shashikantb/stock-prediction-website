document.getElementById("stockForm").addEventListener("submit", async function(e) {
    e.preventDefault();
    const ticker = document.getElementById("ticker").value;
    const res = await fetch(`/predict?ticker=${ticker}`);
    const data = await res.json();
    
    document.getElementById("predictionResult").innerHTML = `
        <h5>Next Day Trend: <strong>${data.trend}</strong></h5>
        <h6>Predicted Price in ${data.days} days: <strong>$${data.future_price}</strong></h6>
        <h6>Moving Averages: ${data.moving_averages.join(', ')}</h6>
    `;

    const ctx = document.getElementById('stockChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.dates,
            datasets: [{
                label: 'Price',
                data: data.prices,
                borderColor: 'blue',
                fill: false
            }]
        }
    });
});
