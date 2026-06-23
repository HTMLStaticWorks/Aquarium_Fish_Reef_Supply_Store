const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

const mobileButtonsHtml = `                <div class="mobile-toggles mt-auto pt-4 border-top border-secondary d-flex justify-content-center gap-3">
                    <button class="theme-btn theme-toggle btn btn-outline-secondary rounded-circle" style="width: 50px; height: 50px;"><i class="bi bi-sun-fill"></i></button>
                    <button class="rtl-btn rtl-toggle btn btn-outline-secondary rounded-circle" style="width: 50px; height: 50px;"><i class="bi bi-arrow-left-right"></i></button>
                </div>
`;

for (const file of files) {
  let content = fs.readFileSync(file, 'utf8');

  // Fix header theme button
  content = content.replace(
    /<button class="theme-btn" id="theme-toggle"><i class="bi bi-sun-fill"><\/i><\/button>/g,
    '<button class="theme-btn header-controls-btn theme-toggle" id="theme-toggle"><i class="bi bi-sun-fill"></i></button>'
  );

  // Fix header rtl button
  content = content.replace(
    /<button class="rtl-btn" id="rtl-toggle"><i class="bi bi-arrow-left-right"><\/i><\/button>/g,
    '<button class="rtl-btn header-controls-btn rtl-toggle" id="rtl-toggle"><i class="bi bi-arrow-left-right"></i></button>'
  );

  // Add mobile toggles if missing
  if (!content.includes('class="mobile-toggles')) {
    // Append after Login button
    content = content.replace(
      /(<a[^>]*href="login\.html"[^>]*>Login<\/a>\s*<\/div>)/g,
      `$1\n${mobileButtonsHtml}`
    );
    
    // Also, some files might not have the Login button structure exactly like that, let's just append before the end of offcanvas-body
    if (!content.includes('class="mobile-toggles')) {
       content = content.replace(
          /(<a class="btn-primary-custom text-center mt-4" href="login\.html">Login<\/a>)/g,
          `$1\n${mobileButtonsHtml}`
       );
    }
  }

  fs.writeFileSync(file, content);
  console.log('Fixed', file);
}
