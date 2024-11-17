// Scroll Reveal Animation for both scrolling up and down
document.addEventListener('DOMContentLoaded', () => {
    const revealElements = document.querySelectorAll('.reveal');

    const revealOnScroll = () => {
        const windowHeight = window.innerHeight;

        revealElements.forEach(el => {
            const elementTop = el.getBoundingClientRect().top;
            const elementBottom = el.getBoundingClientRect().bottom;

            // Check if the element is partially visible in the viewport
            const isVisible = elementTop < windowHeight && elementBottom > 0;

            if (isVisible) {
                el.classList.add('reveal-active');
            } else {
                el.classList.remove('reveal-active'); // Optional: Remove class when out of view
            }
        });
    };

    window.addEventListener('scroll', revealOnScroll);
    revealOnScroll(); // Run on page load to catch any already-visible elements
});
