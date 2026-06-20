document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prediction-form');
    const mainPanel = document.querySelector('.main-panel');
    const resultPanel = document.getElementById('result-container');
    const predictBtn = document.getElementById('predict-btn');
    const btnText = document.querySelector('.btn-text');
    const spinner = document.getElementById('loading-spinner');
    const resetBtn = document.getElementById('reset-btn');
    
    const resultElement = document.getElementById('prediction-result');
    const hoursElement = document.getElementById('hours-result');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Show loading state
        btnText.textContent = 'Calculating...';
        spinner.classList.remove('hidden');
        predictBtn.disabled = true;

        // Gather data
        const formData = {
            distance: document.getElementById('distance').value,
            stops: document.getElementById('stops').value,
            start_time: document.getElementById('start_time').value,
            end_time: document.getElementById('end_time').value
        };

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            const data = await response.json();

            if (data.success) {
                // Hide input, show result
                mainPanel.classList.add('hidden');
                resultPanel.classList.remove('hidden');
                
                // Animate number counter
                animateValue(resultElement, 0, data.prediction, 1500);
                
                // Show hours conversion
                const hours = Math.floor(data.prediction / 60);
                const mins = Math.round(data.prediction % 60);
                hoursElement.textContent = `Approx. ${hours} hours and ${mins} minutes`;
            } else {
                alert('Error: ' + data.error);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to connect to the server.');
        } finally {
            // Reset button state
            btnText.textContent = 'Calculate Duration';
            spinner.classList.add('hidden');
            predictBtn.disabled = false;
        }
    });

    resetBtn.addEventListener('click', () => {
        resultPanel.classList.add('hidden');
        mainPanel.classList.remove('hidden');
        form.reset();
    });

    // Helper for number animation
    function animateValue(obj, start, end, duration) {
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            
            // Ease out cubic
            const easeOut = 1 - Math.pow(1 - progress, 3);
            
            const current = (progress * (end - start) + start).toFixed(2);
            obj.innerHTML = current;
            
            if (progress < 1) {
                window.requestAnimationFrame(step);
            } else {
                obj.innerHTML = end.toFixed(2);
            }
        };
        window.requestAnimationFrame(step);
    }
});
