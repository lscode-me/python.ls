/**
 * LSCode.me - Main JavaScript
 */

document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const menuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');
    
    if (menuBtn && navLinks) {
        menuBtn.addEventListener('click', function() {
            navLinks.classList.toggle('show');
            this.textContent = navLinks.classList.contains('show') ? '✕' : '☰';
        });
    }

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // Add copy button to code blocks
    document.querySelectorAll('pre code').forEach(block => {
        const wrapper = block.parentElement;
        const copyBtn = document.createElement('button');
        copyBtn.className = 'copy-btn';
        copyBtn.textContent = '📋 Copy';
        copyBtn.addEventListener('click', async function() {
            try {
                await navigator.clipboard.writeText(block.textContent);
                this.textContent = '✓ Copied!';
                setTimeout(() => { this.textContent = '📋 Copy'; }, 2000);
            } catch (err) {
                console.error('Failed to copy:', err);
            }
        });
        wrapper.style.position = 'relative';
        copyBtn.style.cssText = 'position:absolute;top:0.5rem;right:0.5rem;padding:0.25rem 0.5rem;font-size:0.75rem;background:#475569;color:#e2e8f0;border:none;border-radius:0.25rem;cursor:pointer;';
        wrapper.appendChild(copyBtn);
    });

    // Generate lecture navigation in right sidebar
    const lectureContent = document.querySelector('.lecture-content');
    const lectureNavToc = document.querySelector('.lecture-nav-toc');
    
    if (lectureContent && lectureNavToc) {
        const headings = lectureContent.querySelectorAll('h2, h3');
        
        headings.forEach((heading, index) => {
            if (!heading.id) {
                heading.id = 'section-' + index;
            }
            
            const link = document.createElement('a');
            link.href = '#' + heading.id;
            link.textContent = heading.textContent;
            link.className = heading.tagName.toLowerCase();
            lectureNavToc.appendChild(link);
        });
        
        // Scroll spy - highlight active section
        const observerOptions = {
            rootMargin: '-80px 0px -80% 0px',
            threshold: 0
        };
        
        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                const id = entry.target.getAttribute('id');
                const link = lectureNavToc.querySelector(`a[href="#${id}"]`);
                
                if (link) {
                    if (entry.isIntersecting) {
                        lectureNavToc.querySelectorAll('a').forEach(a => a.classList.remove('active'));
                        link.classList.add('active');
                    }
                }
            });
        }, observerOptions);
        
        headings.forEach(heading => observer.observe(heading));
    }

    // Reading progress indicator
    if (document.querySelector('.lecture-content')) {
        const progressBar = document.createElement('div');
        progressBar.className = 'reading-progress';
        progressBar.style.cssText = 'position:fixed;top:0;left:0;height:3px;background:var(--primary-color);z-index:1000;transition:width 0.1s;';
        document.body.appendChild(progressBar);

        window.addEventListener('scroll', function() {
            const scrollTop = window.scrollY;
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            const progress = (scrollTop / docHeight) * 100;
            progressBar.style.width = progress + '%';
        });
    }
});

// Mobile nav styles (add dynamically)
const style = document.createElement('style');
style.textContent = `
    @media (max-width: 768px) {
        .nav-links.show {
            display: flex !important;
            flex-direction: column;
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: white;
            padding: 1rem 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
    }
`;
document.head.appendChild(style);
