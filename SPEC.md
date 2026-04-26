# Portfolio Website Specification

## Project Overview
- **Project Name**: Personal Portfolio
- **Type**: Django Web Application
- **Core Functionality**: A dynamic portfolio website with admin-managed content including home, about, experience, skills, projects, and contact sections
- **Target Users**: Visitors viewing portfolio, Admin managing content

## Technology Stack
- **Backend**: Django 4.x (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (default, easily switchable to PostgreSQL)
- **Authentication**: Django AllAuth for full authentication

## UI/UX Specification

### Layout Structure
- **Header**: Fixed navigation bar (logo left, nav links right)
- **Main Content**: Dynamic sections based on admin content
- **Footer**: Social links, copyright

### Responsive Breakpoints
- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: > 1024px

### Color Palette
- Primary: #1a1a2e (dark navy)
- Secondary: #16213e (deep blue)
- Accent: #0f3460 (royal blue)
- Highlight: #e94560 (coral red)
- Text: #eaeaea (light gray)
- Background: #0f0f1a (near black)

### Typography
- Headings: 'Poppins', sans-serif
- Body: 'Open Sans', sans-serif
- Code: 'Fira Code', monospace

### Visual Effects
- Smooth scroll behavior
- Fade-in animations on scroll
- Hover effects on cards and buttons
- Glassmorphism for cards

## Functionality Specification

### Pages & Features
1. **Home**: Hero section with name, title, tagline (admin editable)
2. **About**: Bio, profile image, social links (admin editable)
3. **Experience**: Timeline of work experience (CRUD via admin)
4. **Skills**: Skill cards with proficiency bars (CRUD via admin)
5. **Projects**: Project gallery with images, links (CRUD via admin)
6. **Contact**: Contact form with validation, email integration

### Authentication & Authorization
- User registration/login/logout
- Role-based access: Admin (superuser) full access
- Custom permissions for content management
- Password reset functionality

### Admin Panel
- Django admin for all models
- Inline editing for related objects
- Image upload for projects/profile

## Models Structure
1. **Profile**: name, title, tagline, bio, profile_image, email, github, linkedin, twitter
2. **Experience**: company, position, start_date, end_date, description, is_current
3. **Skill**: name, category, proficiency_level, icon
4. **Project**: title, description, image, github_link, live_link, is_featured
5. **ContactMessage**: name, email, message, created_at, is_read

## Acceptance Criteria
- [x] All 6 pages render correctly
- [x] Navigation works on all pages
- [x] Admin can CRUD all content
- [x] Authentication works (register, login, logout)
- [x] Contact form submits and saves
- [x] Responsive on all devices
- [x] No console errors