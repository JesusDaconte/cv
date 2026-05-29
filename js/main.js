// Mobile navigation toggle
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');

if (navToggle && navMenu) {
    navToggle.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        
        // Animate hamburger to X
        const spans = navToggle.querySelectorAll('span');
        spans.forEach(span => span.classList.toggle('active'));
    });
}

// Close mobile menu when clicking a link
document.querySelectorAll('#navMenu a').forEach(link => {
    link.addEventListener('click', () => {
        if (navMenu) navMenu.classList.remove('active');
        if (navToggle) {
            const spans = navToggle.querySelectorAll('span');
            spans.forEach(span => span.classList.remove('active'));
        }
    });
});

// Scroll spy for active nav link
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('#navMenu a');

function updateActiveSection() {
    if (sections.length > 0 && !window.location.pathname.includes('portafolio.html')) {
        let current = '';

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            if (window.scrollY >= sectionTop - 60) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href').substring(1) === current) {
                link.classList.add('active');
            }
        });
    }
}

let scrollTimeout;
window.addEventListener('scroll', () => {
    if (navMenu && navMenu.classList.contains('active')) {
        navMenu.classList.remove('active');
        if (navToggle) {
            const spans = navToggle.querySelectorAll('span');
            spans.forEach(span => span.classList.remove('active'));
        }
    }

    cancelAnimationFrame(scrollTimeout);
    scrollTimeout = requestAnimationFrame(updateActiveSection);
});

// Contact form handler
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const formData = new FormData(contactForm);
        const nombre = formData.get('nombre');
        const celular = formData.get('celular');
        const email = formData.get('email');
        const mensaje = formData.get('mensaje');

        const text = `Hola Jesús, mi nombre es *${nombre}*.\n\n*Celular:* ${celular}\n*Email:* ${email}\n\n*Mensaje:*\n${mensaje}`;
        const whatsappUrl = `https://wa.me/573004712909?text=${encodeURIComponent(text)}`;

        window.open(whatsappUrl, '_blank');
    });
}
