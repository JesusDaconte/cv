#!/usr/bin/env python3
"""Generate English versions of index.html and portafolio.html into en/."""
import os, sys

ROOT = "/home/daconte/Development/Proyectos/CV"
EN = os.path.join(ROOT, "en")
os.makedirs(EN, exist_ok=True)

# (es, en) — ORDER MATTERS: specific/long first, generics later.
BASE = [
    # --- head ---
    ('<html lang="es" class="dark">', '<html lang="en" class="dark">'),
    ("Especialista en SEO Técnico y Desarrollo Web", "Technical SEO & Web Development Specialist"),
    (" con 5 años de experiencia. Reconstruyo webs lentas a 90+ PageSpeed: Core Web Vitals, Schema, WordPress y Astro. Santa Marta, Colombia.",
     " with 5 years of experience. I rebuild slow websites to 90+ PageSpeed: Core Web Vitals, Schema, WordPress and Astro. Santa Marta, Colombia."),
    ("Reconstruyo sitios lentos en experiencias ultrarrápidas 90+ PageSpeed que posicionan en Google. SEO Técnico + Desarrollo a medida.",
     "I rebuild slow sites into ultra-fast 90+ PageSpeed experiences that rank on Google. Technical SEO + custom development."),
    (" con 5 años de experiencia. Core Web Vitals 90+, Schema Markup, WordPress y Astro. Uso IA para automatizar auditorías.",
     " with 5 years of experience. 90+ Core Web Vitals, Schema Markup, WordPress and Astro. I use AI to automate audits."),
    # --- nav / structure ---
    ("Saltar al contenido principal", "Skip to main content"),
    ('aria-label="Volver al inicio"', 'aria-label="Back to home"'),
    ('aria-label="Abrir menú de navegación"', 'aria-label="Open navigation menu"'),
    ("Sobre mí", "About me"),
    ("Experiencia principal", "Main expertise"),
    ("Experiencia", "Experience"),
    ("Habilidades técnicas", "Technical Skills"),
    ("Habilidades", "Skills"),
    ("Contacto", "Contact"),
    ("Portafolio", "Portfolio"),
    ("Hablemos", "Let's talk"),
    # --- hero (index) ---
    ("SEO Técnico y Desarrollo:", "Technical SEO & Development:"),
    ("reconstruyo webs lentas en sitios", "I rebuild slow websites into"),
    ("rápidos", "fast"),
    ("y listos para", "and ready to"),
    ("posicionar", "rank"),
    ("5 años como docente-desarrollador. Core Web Vitals, Schema Markup, WordPress y Astro. Uso IA para automatizar auditorías 10x más rápido.",
     "5 years as an educator-developer. Core Web Vitals, Schema Markup, WordPress and Astro. I use AI to automate audits 10x faster."),
    ("Solicitar consulta →", "Request a consultation →"),
    # --- stats ---
    (">5+ años<", ">5+ years<"),
    ("Como docente-desarrollador web (HTML, CSS, JS, PHP, SQL)", "As an educator-developer (HTML, CSS, JS, PHP, SQL)"),
    ("Proyectos web verificables en portafolio", "Verifiable web projects in the portfolio"),
    ("Certificaciones en LinkedIn, Microsoft, Google y Platzi", "Certifications from LinkedIn, Microsoft, Google and Platzi"),
    # --- about ---
    ("Soy <span class=\"highlight\">", "I'm <span class=\"highlight\">"),
    (" con 5 años como docente-desarrollador.", " with 5 years as an educator-developer."),
    ("No solo optimizo para Google; reconstruyo sitios lentos desde cero para 90+ PageSpeed.",
     "I don't just optimize for Google; I rebuild slow sites from scratch for 90+ PageSpeed."),
    ("Mi base es", "My foundation is"),
    (" con desarrollo moderno en ", " with modern development in "),
    (" para webs ultrarrápidas y apps híbridas.", " for ultra-fast websites and hybrid apps."),
    ("Uso <span class=\"highlight\">", "I use <span class=\"highlight\">"),
    (" como herramienta</span> para automatizar auditorías técnicas masivas y análisis de competencia, no para reemplazar la estrategia.",
     " as a tool</span> to automate large-scale technical audits and competitor analysis — not to replace strategy."),
    ("SEO Técnico & Core Web Vitals 90+", "Technical SEO & 90+ Core Web Vitals"),
    ("Desarrollo Full-Stack: WordPress, PHP, SQL", "Full-Stack Development: WordPress, PHP, SQL"),
    ("Auditorías automatizadas con IA (Gemini, MCPs)", "AI-automated audits (Gemini, MCPs)"),
    # --- experience ---
    (">Maestro<", ">Web Development Instructor<"),
    ("Desarrollador Web", "Web Developer"),
    ("Marzo 2021 — Presente", "Mar 2021 — Present"),
    ("Marzo 2022 — Diciembre 2022", "Mar 2022 — Dec 2022"),
    ("Enseñar a los estudiantes a desarrollar sitios web profesionales con HTML5, CSS3, JavaScript, PHP y SQL",
     "Teaching students to build professional websites with HTML5, CSS3, JavaScript, PHP and SQL"),
    ("Uso de herramientas como Git y Github para el control de versiones",
     "Using tools like Git and GitHub for version control"),
    ("Implementación de sistemas Linux para el proceso de desarrollo",
     "Implementing Linux systems for the development workflow"),
    ("Creación de nuevas características para el sitio web principal y sitios de clientes",
     "Building new features for the main website and client sites"),
    ("Mantenimiento de sitios web y servidor web de la empresa",
     "Maintaining the company's websites and web server"),
    ("Implementación de CI/CD y construcción de landings para campañas de SEM",
     "Implementing CI/CD and building landing pages for SEM campaigns"),
    ("Asesorías web y de servidores", "Web and server consulting"),
    # --- skills ---
    ("IA como herramienta SEO", "AI as an SEO tool"),
    ("Optimización CSS/JS", "CSS/JS Optimization"),
    ("URLs amigables", "Friendly URLs"),
    ("Desarrollo Full-Stack", "Full-Stack Development"),
    ("Stack Moderno", "Modern Stack"),
    ("Auditorías automatizadas", "Automated audits"),
    ("Análisis competencia", "Competitor analysis"),
    ("Entorno de Desarrollo", "Development Environment"),
    # --- certifications ---
    ("Certificaciones", "Certifications"),
    ("Certificado de Inglés", "English Certificate"),
    ("Desarrollador WordPress", "WordPress Developer"),
    ("Fundamentos de Análisis de Datos", "Data Analysis Fundamentals"),
    ("Fundamentos de Desarrollo de Software", "Software Development Fundamentals"),
    ("GitHub para Programadores", "GitHub for Programmers"),
    ("Desarrollo Frontend", "Frontend Development"),
    ("Administración de Servidores", "Server Administration"),
    ("Diseño Web Responsivo", "Responsive Web Design"),
    ("Auxiliar en Análisis y Desarrollo", "Analysis & Development Assistant"),
    ("Certificación de Inglés", "English Certification"),
    ("Microsoft y LinkedIn", "Microsoft & LinkedIn"),
    # generic SEO terms (after all specific ones)
    ("SEO Técnico", "Technical SEO"),
    ("Inglés", "English"),
    ("Certificado ", "Certificate "),
    # --- contact ---
    ("Trabajemos juntos", "Let's work together"),
    ("¿Tienes un proyecto en mente o quieres colaborar? No dudes en contactarme.",
     "Have a project in mind or want to collaborate? Don't hesitate to contact me."),
    ("Perfil de LinkedIn", "LinkedIn Profile"),
    ("Descargar CV (PDF)", "Download Resume (PDF)"),
    ("Envíame un mensaje", "Send me a message"),
    ("Nombre completo", "Full name"),
    ("Tu nombre", "Your name"),
    ("Celular", "Phone"),
    ("Correo electrónico", "Email"),
    ("tu@email.com", "you@email.com"),
    ("Enviar mensaje", "Send message"),
    ("¿En qué puedo ayudarte?", "How can I help you?"),
    ("O escribe directamente por", "Or message me directly on"),
    ("o al correo", "or email me at"),
    (">Mensaje<", ">Message<"),
    # --- footer / whatsapp ---
    ("© 2019 - 2026. Jesús Daconte. Todos los derechos reservados.",
     "© 2019 - 2026. Jesús Daconte. All rights reserved."),
    ("Desarrollado con HTML, CSS y mucho", "Built with HTML, CSS and lots of"),
    ('aria-label="Contactar por WhatsApp"', 'aria-label="Contact me on WhatsApp"'),
    ("?text=Hola%20Jes%C3%BAs,%20vi%20tu%20portafolio%20y%20me%20gustar%C3%ADa%20contactarte.",
     "?text=Hi%20Jes%C3%BAs,%20I%20saw%20your%20portfolio%20and%20would%20like%20to%20get%20in%20touch."),
]

PORT = [
    ("Portafolio de desarrollo web con SEO Técnico: WordPress, HTML, CSS, JavaScript y Astro. Sitios rápidos 90+ PageSpeed en Santa Marta, Colombia.",
     "Web development portfolio with Technical SEO: WordPress, HTML, CSS, JavaScript and Astro. Fast 90+ PageSpeed sites in Santa Marta, Colombia."),
    ("Proyectos web con SEO Técnico: WordPress, código a medida y optimización Core Web Vitals.",
     "Web projects with Technical SEO: WordPress, custom code and Core Web Vitals optimization."),
    ("Proyectos web con SEO Técnico y desarrollo a medida. WordPress, HTML, CSS, JS y Astro.",
     "Web projects with Technical SEO and custom development. WordPress, HTML, CSS, JS and Astro."),
    ("Mi <span>Portafolio</span>", "My <span>Portfolio</span>"),
    ("Proyectos de desarrollo web con SEO Técnico: WordPress, código a medida y optimización Core Web Vitals para posicionar en Google.",
     "Web development projects with Technical SEO: WordPress, custom code and Core Web Vitals optimization to rank on Google."),
    ("Portafolio", "Portfolio"),
    (">Todos<", ">All<"),
    ("Clientes CMS", "CMS Clients"),
    ("Clientes Code", "Code Clients"),
    ("Proyectos Code", "Code Projects"),
    ("Ver Proyecto", "View Project"),
    # project descriptions
    ("Agencia de ecoturismo y etnoturismo especializada en tours a Ciudad Perdida y expediciones por la Sierra Nevada de Santa Marta. Trabajo directo con comunidades Kogui, Arhuaco y Wiwa.",
     "Ecotourism and ethnotourism agency specialized in Lost City tours and expeditions through the Sierra Nevada de Santa Marta. Direct work with the Kogui, Arhuaco and Wiwa communities."),
    ("Plataforma del Sistema Territorial de Ciencia, Tecnología e Innovación del Magdalena. Portal institucional con información sobre el plan de desarrollo departamental con miras al 2040.",
     "Platform for Magdalena's Territorial Science, Technology and Innovation System. Institutional portal covering the departmental development plan toward 2040."),
    ("Sitio corporativo para empresa de diseño, arquitectura y construcción. Portal inmobiliario con galería de proyectos, login de clientes y servicios especializados de ingeniería.",
     "Corporate site for a design, architecture and construction company. Real-estate portal with project gallery, client login and specialized engineering services."),
    ("Operador turístico con rutas exclusivas en la Sierra Nevada. Sistema de reservas en línea, tours a Ciudad Perdida y experiencias de montaña con guías locales certificados.",
     "Tour operator with exclusive Sierra Nevada routes. Online booking system, Lost City tours and mountain experiences with certified local guides."),
    ("Landing page corporativa para empresa de ingeniería civil y construcción residencial en Barranquilla. Catálogo de proyectos destacados, servicios especializados y sistema de cotización.",
     "Corporate landing page for a civil engineering and residential construction company in Barranquilla. Featured project catalog, specialized services and quoting system."),
    ("Guía turística bilingüe (ES/EN) con 72 lugares verificados, blog, buscador e itinerarios. PWA con Schema Markup, sitemap de 1500+ URLs y datos auditados desde Google Maps.",
     "Bilingual (ES/EN) travel guide with 72 verified places, blog, search and itineraries. PWA with Schema Markup, 1500+ URL sitemap and Google Maps-audited data."),
    ("Sitio web para complejo de apartasuites frente al mar en Santa Marta. Diseño moderno con galería interactiva, catálogo de suites y sistema de reservas integrado.",
     "Website for a beachfront aparthotel complex in Santa Marta. Modern design with interactive gallery, suite catalog and integrated booking system."),
    ("Sitio web para espacio de coworking en Santa Marta dirigido a nómadas digitales. Diseño fresco con secciones de servicios, membresías y comunidad de emprendedores.",
     "Website for a coworking space in Santa Marta aimed at digital nomads. Fresh design with services, memberships and entrepreneur community sections."),
    ("Sitio web corporativo para firma de abogados en Bogotá con más de 20 años de trayectoria. Sistema de agendamiento de consultas en línea y presentación de áreas de práctica.",
     "Corporate website for a Bogotá law firm with 20+ years of experience. Online consultation scheduling and practice-area showcase."),
    ("Reproductor de música basado en YouTube. Agrega videos, crea listas de reproducción personalizadas y disfruta de tu música favorita desde una interfaz limpia y funcional.",
     "YouTube-based music player. Add videos, create custom playlists and enjoy your favorite music from a clean, functional interface."),
    ("Generador de códigos QR personalizados con opciones de color, logo y tamaño. Interfaz moderna y responsive para crear QR al instante.",
     "Custom QR code generator with color, logo and size options. Modern responsive interface to create QR codes instantly."),
    # tags
    ("SEO Turismo", "Tourism SEO"),
    ("Ecoturismo", "Ecotourism"),
    ("Turismo", "Tourism"),
    ("Gobierno", "Government"),
    ("SEO Institucional", "Institutional SEO"),
    ("SEO Local", "Local SEO"),
    ("Sitio Web", "Website"),
    # alts
    ("Captura del home Santa Marta Guía - Guía turística con SEO Técnico",
     "Santa Marta Guide home screenshot - Travel guide with Technical SEO"),
    ("Captura del sitio web ", "Screenshot of the "),
    ("Captura del proyecto ", "Screenshot of the "),
    ("Tours a Ciudad Perdida", "Ciudad Perdida tours"),
    ("Arquitectura", "Architecture"),
    ("Rutas Sierra Nevada", "Sierra Nevada routes"),
    ("Ingeniería Civil", "Civil Engineering"),
    ("Sitio web completo", "Full website"),
    ("Firma de abogados", "Law firm"),
    ("Reproductor de YouTube", "YouTube player"),
    ("Códigos QR personalizados", "Custom QR codes"),
    # cta + comments
    ("¿Tu web es lenta y no posiciona?", "Is your website slow and not ranking?"),
    ("Escríbeme para reconstruir tu sitio a 90+ PageSpeed, corregir SEO Técnico (Core Web Vitals, Schema, mobile-first) o crear tu web a medida en WordPress o Astro.",
     "Contact me to rebuild your site to 90+ PageSpeed, fix Technical SEO (Core Web Vitals, Schema, mobile-first) or create your custom website in WordPress or Astro."),
    ("Iniciar conversación →", "Start a conversation →"),
    ("// Interactive Tab Filter logic", "// Tab filter logic"),
    ("// Remove active class from all buttons", "// Remove the active class from all buttons"),
    ("// Add active class to clicked button", "// Add the active class to the clicked button"),
]

PATHS = [
    ('href="css/style.css"', 'href="../css/style.css"'),
    ('src="js/main.js"', 'src="../js/main.js"'),
    ('src="img/', 'src="../img/'),
]

PATHS_INDEX = [
    ('href="img/', 'href="../img/'),
    ('href="Jesus_Daconte_Hoja_de_Vida.pdf"', 'href="../Jesus_Daconte_Resume.pdf"'),
    ('<li class="mobile-lang"><a href="en/index.html" hreflang="en">🌐 English</a></li>',
     '<li class="mobile-lang"><a href="../index.html" hreflang="es">🌐 Español</a></li>'),
    ('\n            <a href="en/index.html" class="lang-btn" hreflang="en" aria-label="Switch to English">EN</a>', ''),
    ('\n    <link rel="alternate" hreflang="es" href="https://jesusdaconte.github.io/cv/">\n    <link rel="alternate" hreflang="en" href="https://jesusdaconte.github.io/cv/en/">\n    <link rel="alternate" hreflang="x-default" href="https://jesusdaconte.github.io/cv/">\n    <meta property="og:locale" content="es_CO">', ''),
]

PATHS_PORT = [
    ('<li class="mobile-lang"><a href="en/portafolio.html" hreflang="en">🌐 English</a></li>',
     '<li class="mobile-lang"><a href="../portafolio.html" hreflang="es">🌐 Español</a></li>'),
    ('\n            <a href="en/portafolio.html" class="lang-btn" hreflang="en" aria-label="Switch to English">EN</a>', ''),
    ('\n    <link rel="alternate" hreflang="es" href="https://jesusdaconte.github.io/cv/portafolio.html">\n    <link rel="alternate" hreflang="en" href="https://jesusdaconte.github.io/cv/en/portafolio.html">\n    <link rel="alternate" hreflang="x-default" href="https://jesusdaconte.github.io/cv/portafolio.html">\n    <meta property="og:locale" content="es_CO">', ''),
]

HEAD_INDEX = (
    '<link rel="canonical" href="https://jesusdaconte.github.io/cv/">',
    '<link rel="canonical" href="https://jesusdaconte.github.io/cv/en/">\n'
    '    <link rel="alternate" hreflang="es" href="https://jesusdaconte.github.io/cv/">\n'
    '    <link rel="alternate" hreflang="en" href="https://jesusdaconte.github.io/cv/en/">\n'
    '    <link rel="alternate" hreflang="x-default" href="https://jesusdaconte.github.io/cv/">\n'
    '    <meta property="og:locale" content="en_US">',
)
HEAD_PORT = (
    '<link rel="canonical" href="https://jesusdaconte.github.io/cv/portafolio.html">',
    '<link rel="canonical" href="https://jesusdaconte.github.io/cv/en/portafolio.html">\n'
    '    <link rel="alternate" hreflang="es" href="https://jesusdaconte.github.io/cv/portafolio.html">\n'
    '    <link rel="alternate" hreflang="en" href="https://jesusdaconte.github.io/cv/en/portafolio.html">\n'
    '    <link rel="alternate" hreflang="x-default" href="https://jesusdaconte.github.io/cv/portafolio.html">\n'
    '    <meta property="og:locale" content="en_US">',
)

LANG_BTN = {
    "index.html": ('class="nav-btn">Let\'s talk</a>',
                   'class="nav-btn">Let\'s talk</a>\n            <a href="../index.html" class="lang-btn" hreflang="es" aria-label="Cambiar a español">ES</a>'),
    "portafolio.html": ('class="nav-btn">Let\'s talk</a>',
                        'class="nav-btn">Let\'s talk</a>\n            <a href="../portafolio.html" class="lang-btn" hreflang="es" aria-label="Cambiar a español">ES</a>'),
}


def build(src_name, extra, head, misses, extra_paths=None):
    with open(os.path.join(ROOT, src_name), encoding="utf-8") as f:
        html = f.read()
    for es, en in extra + BASE + PATHS + (extra_paths or []):
        n = html.count(es)
        if n == 0:
            misses.append((src_name, es[:70]))
        html = html.replace(es, en)
    old, new = head
    assert old in html, f"canonical missing in {src_name}"
    html = html.replace(old, new)
    old, new = LANG_BTN[src_name]
    assert old in html, f"nav-btn anchor missing in {src_name}"
    html = html.replace(old, new)
    with open(os.path.join(EN, src_name), "w", encoding="utf-8") as f:
        f.write(html)
    return html


misses = []
build("index.html", [], HEAD_INDEX, misses, PATHS_INDEX)
build("portafolio.html", PORT, HEAD_PORT, misses, PATHS_PORT)
print(f"MISSES: {len(misses)}")
for src, s in misses:
    print(f"  [{src}] {s!r}")
