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

    // Table of Contents generation for lecture pages
    const lectureContent = document.querySelector('.lecture-content');
    if (lectureContent) {
        const headings = lectureContent.querySelectorAll('h2, h3');
        if (headings.length > 3) {
            const toc = document.createElement('nav');
            toc.className = 'table-of-contents';
            toc.innerHTML = '<h4>📑 Table of Contents</h4>';
            const list = document.createElement('ul');
            
            headings.forEach((heading, index) => {
                if (!heading.id) {
                    heading.id = 'section-' + index;
                }
                const li = document.createElement('li');
                li.className = heading.tagName.toLowerCase();
                li.innerHTML = `<a href="#${heading.id}">${heading.textContent}</a>`;
                list.appendChild(li);
            });
            
            toc.appendChild(list);
            lectureContent.insertBefore(toc, lectureContent.firstChild);
        }
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
    .table-of-contents {
        background: #f8fafc;
        padding: 1rem 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 2rem;
    }
    .table-of-contents h4 {
        margin-bottom: 0.75rem;
    }
    .table-of-contents ul {
        list-style: none;
        margin: 0;
        padding: 0;
    }
    .table-of-contents li {
        margin-bottom: 0.25rem;
    }
    .table-of-contents li.h3 {
        padding-left: 1rem;
        font-size: 0.9rem;
    }
    .table-of-contents a {
        color: var(--text-muted);
    }
    .table-of-contents a:hover {
        color: var(--primary-color);
    }
`;
document.head.appendChild(style);
