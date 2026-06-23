document.addEventListener('DOMContentLoaded', () => {
  /* =========================================================================
     1. Sticky Header
     ========================================================================= */
  const header = document.querySelector('.header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    });
  }

  /* =========================================================================
     2. Theme Switcher
     ========================================================================= */
  const themeBtns = document.querySelectorAll('.theme-toggle, #theme-toggle');
  const htmlEl = document.documentElement;
  
  // Check local storage for theme
  const savedTheme = localStorage.getItem('aquarium-theme');
  if (savedTheme) {
    htmlEl.setAttribute('data-theme', savedTheme);
    updateThemeIcons(savedTheme);
  } else {
    // Default to dark mode if no preference since it's a deep ocean theme
    htmlEl.setAttribute('data-theme', 'dark');
    updateThemeIcons('dark');
  }

  themeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const currentTheme = htmlEl.getAttribute('data-theme');
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      htmlEl.setAttribute('data-theme', newTheme);
      localStorage.setItem('aquarium-theme', newTheme);
      updateThemeIcons(newTheme);
    });
  });

  function updateThemeIcons(theme) {
    themeBtns.forEach(btn => {
      if (theme === 'dark') {
        btn.innerHTML = '<i class="bi bi-sun-fill"></i>';
      } else {
        btn.innerHTML = '<i class="bi bi-moon-stars-fill"></i>';
      }
    });
  }

  /* =========================================================================
     3. RTL Toggle
     ========================================================================= */
  const rtlBtns = document.querySelectorAll('.rtl-toggle, #rtl-toggle');
  
  const savedDir = localStorage.getItem('aquarium-dir');
  if (savedDir) {
    htmlEl.setAttribute('dir', savedDir);
  }

  rtlBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const currentDir = htmlEl.getAttribute('dir');
      const newDir = currentDir === 'rtl' ? 'ltr' : 'rtl';
      htmlEl.setAttribute('dir', newDir);
      localStorage.setItem('aquarium-dir', newDir);
    });
  });

  /* =========================================================================
     4. Intersection Observer for Scroll Animations
     ========================================================================= */
  const revealElements = document.querySelectorAll(
    '.reveal-fade-up, .reveal-fade-left, .reveal-fade-right, .reveal-zoom-in'
  );

  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.15
  };

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        // Unobserve after revealing to prevent repeating animation continuously
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  revealElements.forEach(el => {
    revealObserver.observe(el);
  });

  /* =========================================================================
     5. Bubble Effect Generator (Optional helper for hero sections)
     ========================================================================= */
  function createBubbles(containerSelector, bubbleCount = 15) {
    const container = document.querySelector(containerSelector);
    if (!container) return;

    for (let i = 0; i < bubbleCount; i++) {
      const bubble = document.createElement('div');
      bubble.classList.add('bubble');
      
      // Randomize size, left position, and animation duration/delay
      const size = Math.random() * 20 + 5 + 'px';
      const left = Math.random() * 100 + '%';
      const duration = Math.random() * 5 + 5 + 's';
      const delay = Math.random() * 5 + 's';

      bubble.style.width = size;
      bubble.style.height = size;
      bubble.style.left = left;
      bubble.style.animationDuration = duration;
      bubble.style.animationDelay = delay;

      container.appendChild(bubble);
    }
  }

  // Example usage for a hero section with ID #hero-bubbles
  createBubbles('#hero-bubbles', 25);

  /* =========================================================================
     6. Active Link in Hamburger Menu
     ========================================================================= */
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  const offcanvasLinks = document.querySelectorAll('.offcanvas-body a:not(.btn)');
  
  offcanvasLinks.forEach(link => {
    const linkHref = link.getAttribute('href');
    if (linkHref === currentPage) {
      // Add active styling, overriding any inline text color
      link.style.color = 'var(--color-secondary)';
      link.classList.add('fw-bold');
    }
  });
});

