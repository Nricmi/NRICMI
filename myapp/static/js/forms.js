// Ensure only one radio button is selected for Period
document.querySelectorAll('.period-radio').forEach((radio) => {
    radio.addEventListener('change', (event) => {
        document.querySelectorAll('.period-radio').forEach((r) => {
            if (r !== event.target) {
                r.checked = false;
            }
        });
    });
});
