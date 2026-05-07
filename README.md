# Pola Entertainment - Photography Portfolio

A modern, responsive photography portfolio website with a backend server, contact form, and dynamic content management.

## 🚀 Quick Start

### Prerequisites
- Node.js (v14 or higher)
- npm (comes with Node.js)

### Installation

1. **Install Dependencies**
   ```bash
   npm install
   ```

2. **Configure Environment Variables**
   Edit `.env` file to customize:
   ```
   NODE_ENV=development
   PORT=3000
   HOST=localhost
   CONTACT_EMAIL=your-email@example.com
   PHONE=your-phone-number
   ```

3. **Start the Server**
   ```bash
   npm start
   ```

4. **Access the Website**
   Open your browser and navigate to:
   ```
   http://localhost:3000
   ```

## 📁 Project Structure

```
library/
├── public/
│   ├── index.html          # Main website (served as localhost:3000)
│   ├── config.js           # Frontend configuration utility
│   ├── images/             # Portfolio images
│   └── pdfs/               # PDF downloads
├── server.js               # Express backend server
├── package.json            # Dependencies
├── .env                    # Environment configuration
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## 🔧 Configuration

### Development
For local development (default):
- **URL**: `http://localhost:3000`
- **API**: `http://localhost:3000/api`
- **Environment**: `development`

### Production
To deploy to production:

1. Update `.env`:
   ```
   NODE_ENV=production
   PROD_URL=https://your-domain.com
   PROD_API_URL=https://your-domain.com/api
   ```

2. Set `NODE_ENV=production` when running:
   ```bash
   NODE_ENV=production npm start
   ```

## 🔌 API Endpoints

### Get Configuration
```
GET /api/config
```
Returns current server configuration and environment settings.

### Get Portfolio Items
```
GET /api/portfolio
```
Returns array of portfolio items with images and PDF links.

### Submit Contact Form
```
POST /api/contact
Headers: Content-Type: application/json
Body: {
  "name": "Full Name",
  "email": "email@example.com",
  "subject": "Subject",
  "message": "Message content"
}
```

## 📁 Adding Your Content

### Images & PDFs Location
```
d:\wep\library\public\images\     ← Place your images here
d:\wep\library\public\pdfs\       ← Place your PDFs here
```

### Required Files
**Images:**
- `Jpg.jpg` - SPSS guide image
- `2.jpg` - RCBD model image
- `3.jpg` - Experimental design image
- `photo_2026-01-26_12-43-09.jpg` - Profile photo

**PDFs:**
- `ការណែនាំអំពីកម្មវិធី_SPSS.pdf` - SPSS guide
- `RCBD.pdf` - RCBD model guide
- `RCB.pdf` - Experimental design guide

### Quick Setup
1. Replace the `.txt` placeholder files with your actual images/PDFs
2. Use exact filenames as listed above
3. Restart the server: `python server.py`
4. Visit `http://localhost:3000` to see your content

See `CONTENT_GUIDE.md` for detailed instructions.

## 🎨 Customization

### URL Configuration
All URLs are dynamically generated based on environment:
- Development: `http://localhost:3000`
- Production: Uses `PROD_URL` from `.env`

### Image & PDF Paths
Images and PDFs use relative paths that work with the server:
- Images: `/images/filename.jpg`
- PDFs: `/pdfs/filename.pdf`

## 🚀 Deployment

### Vercel
```bash
vercel
```

### Heroku
```bash
git push heroku main
```

### Traditional VPS/Server
```bash
npm install
NODE_ENV=production PORT=80 npm start
```

## 📦 Dependencies

- **express**: Web framework
- **cors**: Cross-origin resource sharing
- **compression**: Response compression
- **helmet**: Security headers
- **dotenv**: Environment configuration

## 🔐 Security Features

- CORS protection
- Security headers (Helmet)
- Response compression
- Input validation
- Environment isolation

## 📱 Features

- ✅ Responsive design (mobile-first)
- ✅ Dynamic portfolio coverflow
- ✅ Contact form with backend processing
- ✅ Smooth scroll navigation
- ✅ Dark theme with accent colors
- ✅ Loading animations
- ✅ Mobile menu toggle
- ✅ Auto-playing carousel
- ✅ PDF download support

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Change PORT in .env or use different port
PORT=3001 npm start
```

### Images Not Loading
- Ensure images are in `public/images/`
- Check browser console for 404 errors
- Verify image file paths in HTML

### API Not Working
- Check if server is running
- Verify CORS is enabled
- Check browser developer console for errors

## 💡 Tips

- Use `npm run dev` with nodemon for auto-restart during development
- Compress images before uploading to reduce load times
- Test responsive design with browser DevTools
- Monitor console logs for server messages

## 📄 License

MIT License - © 2026 Pola Entertainment

## 👨‍💻 Author

Thorn Pola - thornpola6@gmail.com
