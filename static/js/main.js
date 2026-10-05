// Global JS for Textile ERP. Sidebar active-link highlight, shared helpers, etc.
document.addEventListener('DOMContentLoaded', function () {
    const links = document.querySelectorAll('.nav-link');
    const current = window.location.pathname;
    links.forEach(function (link) {
        if (link.getAttribute('href') === current) {
            link.style.background = 'rgba(255,255,255,0.12)';
            link.style.borderLeftColor = 'var(--color-accent)';
        }
    });
});
