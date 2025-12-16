# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-12-16

### Added
- Initial release of hexo-theme-cybermind
- Modern dark theme with orange/amber accents
- Fully responsive design (mobile, tablet, desktop)
- Hero section with customizable stats and CTAs
- Article cards with category-specific colors
- Support for 6 predefined categories (security, kernel, embedded, opensource, iot, tutorials)
- Custom category pages with hero sections
- Archive and tag pages
- SEO optimization with Open Graph and Twitter Cards
- RSS feed support
- Sitemap support
- Syntax highlighting for code blocks
- Copy button for code blocks
- Back-to-top button
- Smooth scrolling
- Streamlit apps integration section
- YouTube playlist integration section
- Contact form with Formspree
- Social links in footer
- About section with profile card
- Pagination support
- Article navigation (prev/next)
- Tag system
- Mobile-friendly navigation
- Lazy loading images
- External links open in new tab
- French localization

### Layout Templates
- `layout.ejs` - Main layout wrapper
- `index.ejs` - Homepage with hero and article grid
- `post.ejs` - Individual article page
- `page.ejs` - Static pages
- `archive.ejs` - Archives listing
- `category.ejs` - Category-specific pages
- `partials/head.ejs` - HTML head section
- `partials/meta.ejs` - SEO meta tags
- `partials/header.ejs` - Navigation header
- `partials/footer.ejs` - Site footer
- `partials/article.ejs` - Article card component

### Styling
- Complete CSS with CSS variables for easy customization
- Typography using Space Grotesk and JetBrains Mono fonts
- Smooth transitions and hover effects
- Card-based design
- Gradient backgrounds
- Category-specific color coding

### JavaScript
- Smooth scroll for anchor links
- Mobile menu toggle
- Back-to-top button with scroll detection
- Code block copy functionality
- External link handling
- Image lazy loading fallback

### Documentation
- Comprehensive README.md
- Quick installation guide (INSTALLATION.md)
- Example configuration files
- Inline code comments
- MIT License

## [Unreleased]

### Planned Features
- Dark/light mode toggle
- Search functionality
- Comments system integration (Disqus, Gitalk, etc.)
- Reading time estimation
- Table of contents for long articles
- Related posts suggestions
- Image zoom on click
- Print-friendly CSS
- PWA support
- i18n support for multiple languages
- Archive by year/month views
- Popular posts widget
- Social share buttons
