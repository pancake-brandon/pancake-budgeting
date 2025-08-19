# Pancake Landing Page

The official landing page for Pancake - a smart budgeting app that helps you take control of your finances, one stack at a time.

## 🚀 Quick Start

### Local Development (Recommended)

1. **Start the backend server:**
   ```bash
   cd ../pancake-backend
   source venv/bin/activate
   uvicorn app.main:app --reload --port 8000
   ```

2. **Serve the landing page:**
   ```bash
   python3 serve.py
   ```

3. **Open in browser:**
   Navigate to http://localhost:3000

## 📁 Project Structure

```
pancake-budgeting/
├── index.html          # Main landing page
├── serve.py           # Local development server
├── images/            # All image assets
│   ├── PancakeAppLogo/
│   ├── images/        # SVG illustrations
│   └── AppsLogos/     # Social media icons
└── README.md          # This file
```

## 🔧 Features

- **Waitlist Form**: Integrated with Loops.so for email management
- **Responsive Design**: Mobile-first approach using Tailwind CSS
- **Smooth Scrolling**: Navigation between sections
- **Smart Back-to-Top Button**: Changes color based on section background
- **CORS-Compliant**: Proper handling for local development

## 🐛 Troubleshooting

### "Network error" when submitting form

**Issue**: Opening index.html directly as a file causes CORS errors.

**Solution**: Use the provided development server:
```bash
python3 serve.py
```

### "Failed to join waitlist"

**Possible causes:**
1. Backend server not running - Start with `uvicorn app.main:app --reload`
2. Invalid API key - Check LOOPS_API_KEY in backend .env file
3. Network issues - Verify localhost:8000 is accessible

### Form doesn't show success message

Ensure the backend has:
- Loops API key configured
- Forms endpoints enabled
- CORS properly configured for localhost:3000

## 🌐 API Integration

The landing page connects to the backend API for:
- Waitlist submissions (`/api/v1/forms/waitlist`)
- Newsletter signups (future feature)
- Contact form submissions (future feature)

### Environment Detection

The form automatically detects the environment:
- Local development: Uses http://localhost:8000
- Production: Uses https://api.pancakemoney.com

## 🎨 Design System

- **Primary Color**: #279B75 (Pancake Green)
- **Secondary Color**: #2E8B57 (Darker Green on hover)
- **Typography**: Inter font family
- **Spacing**: Tailwind CSS default scale

## 📱 Responsive Breakpoints

- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: > 1024px

## 🚀 Deployment

For production deployment:

1. Update API endpoint in index.html:
   ```javascript
   apiUrl = 'https://api.pancakemoney.com/api/v1/forms/waitlist';
   ```

2. Deploy to your web server or CDN

3. Ensure backend CORS settings include your domain

## 📝 Content Sections

1. **Hero**: Main value proposition with waitlist form
2. **About Us**: Mission statement
3. **Pancake Pro**: AI-powered features
4. **Data Privacy**: Security commitment
5. **Contact**: Support and social links

## 🔒 Security Notes

- Form submissions use HTTPS in production
- No sensitive data stored client-side
- API keys kept on backend only
- CORS restricted to allowed origins

## 📊 Analytics

Future integration points for:
- Google Analytics
- Mixpanel
- Conversion tracking
- A/B testing

## 🤝 Contributing

1. Make changes to index.html
2. Test locally using serve.py
3. Verify form submissions work
4. Check responsive design
5. Submit pull request

## 📞 Support

For issues or questions:
- Email: support@pancakemoney.com
- Instagram: @pancake.money

## 📄 License

© 2024 Pancake. All rights reserved.
