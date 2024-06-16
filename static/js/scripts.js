document.addEventListener('DOMContentLoaded', (event) => {
    const confetti = document.querySelector('.confetti');

    if (confetti) {
        confetti.style.display = 'block';
        setTimeout(() => {
            confetti.style.display = 'none';
        }, 3000);
    }
});
