import os
import re

pages = ['index.html', 'about.html', 'services.html', 'support.html', 'contact.html']

for page in pages:
    with open(page, 'r') as f:
        content = f.read()
    
    # Find the header phone section and add button after it
    old_pattern = '''</svg>
        (561) 693-2624
      </a>
      <button class="mobile-menu-btn"'''
    
    new_pattern = '''</svg>
        (561) 693-2624
      </a>
      <a href="contact.html" class="header-cta" style="background: var(--primary); color: white; padding: 0.5rem 1rem; border-radius: 4px; text-decoration: none; font-weight: 600; white-space: nowrap; margin-left: 0.75rem;">Request A Quote</a>
      <button class="mobile-menu-btn"'''
    
    content = content.replace(old_pattern, new_pattern)
    
    with open(page, 'w') as f:
        f.write(content)
    print(f"Updated {page}")
