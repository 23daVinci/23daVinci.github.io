<<<<<<< HEAD
# 23daVinci Portfolio Website

A modern, minimalist portfolio website built with Flask, featuring a clean black and white design inspired by professional portfolio templates.

## Features

- **Modern Design**: Clean, minimalist black and white aesthetic
- **Responsive Layout**: Fully responsive design that works on all devices
- **Smooth Animations**: Subtle hover effects and scroll animations
- **Contact Form**: Functional contact form with backend processing
- **Interactive Navigation**: Smooth scrolling and active section highlighting
- **Project Showcase**: Grid layout for displaying projects with tags
- **Skills Section**: Highlighting technical skills and expertise
- **Resume Section**: Professional experience and education display

## Sections

1. **Hero Section**: Eye-catching introduction with call-to-action buttons
2. **About**: Personal introduction and mission statement
3. **Skills**: Technical expertise and services offered
4. **Projects**: Portfolio of work with detailed descriptions
5. **Resume**: Professional background and certifications
6. **Contact**: Contact form and information

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS with responsive design
- **Fonts**: Inter (Google Fonts)
- **Icons**: CSS-based placeholders (easily replaceable with icon libraries)

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd 23daVinci.github.io
   ```

2. **Install dependencies**:
   ```bash
   pip install flask
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the website**:
   Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
23daVinci.github.io/
├── app.py                 # Flask application
├── config.py             # Configuration settings
├── templates/
│   └── index.html        # Main portfolio page
├── static/
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   └── js/
│       └── main.js       # JavaScript functionality
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

## Customization

### Personal Information
Edit the following sections in `templates/index.html`:
- Hero section content
- About section text
- Skills and expertise
- Project details
- Resume information
- Contact details

### Styling
Modify `static/css/style.css` to:
- Change colors (currently black and white theme)
- Adjust typography
- Modify spacing and layout
- Update animations

### Functionality
Edit `static/js/main.js` to:
- Modify form handling
- Adjust animations
- Change scroll behavior
- Update interactive features

## Features in Detail

### Navigation
- Fixed navigation bar with blur effect
- Smooth scrolling to sections
- Active section highlighting
- Responsive mobile navigation

### Contact Form
- Client-side validation
- Server-side processing via Flask
- Success/error notifications
- Form field validation

### Animations
- Intersection Observer for scroll animations
- Hover effects on cards and buttons
- Smooth transitions
- Loading animations

### Responsive Design
- Mobile-first approach
- Breakpoints for tablets and desktops
- Flexible grid layouts
- Optimized typography scaling

## Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
1. Set environment variables:
   ```bash
   export SECRET_KEY="your-secret-key"
   export FLASK_ENV="production"
   ```

2. Use a production WSGI server:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## Performance

- Optimized CSS and JavaScript
- Minimal dependencies
- Fast loading times
- SEO-friendly structure
- Accessible design

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For questions or support, please reach out through the contact form on the website or via email.

---

Built with ❤️ by 23daVinci
=======
# 23daVinci.github.io
>>>>>>> e5bb555e821e716a7b06a93c4c1e79c0dca7407d
