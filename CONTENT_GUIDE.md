# 📁 Content Setup Guide

## 🎯 Adding Your Images & PDFs

### Step 1: Place Your Files

**Images go here:**
```
d:\wep\library\public\images\
```

**PDFs go here:**
```
d:\wep\library\public\pdfs\
```

### Step 2: Replace Placeholder Files

Delete the `.txt` files and replace them with your actual files:

#### Required Images:
- `Jpg.jpg` - SPSS guide image
- `2.jpg` - RCBD model image  
- `3.jpg` - Experimental design image
- `photo_2026-01-26_12-43-09.jpg` - Profile photo

#### Required PDFs:
- `ការណែនាំអំពីកម្មវិធី_SPSS.pdf` - SPSS guide PDF
- `RCBD.pdf` - RCBD model PDF
- `RCB.pdf` - Experimental design PDF

### Step 3: File Naming

**IMPORTANT:** Use exact filenames as shown above. The website expects these specific names.

---

## 🔧 Updating Portfolio Content

### Option 1: Edit Server Directly

Open `server.py` and modify the `PORTFOLIO_DATA` list:

```python
PORTFOLIO_DATA = [
    {
        "id": 0,
        "title": "Your Title",
        "description": "Your description",
        "image": "/images/your-image.jpg",
        "pdf": "/pdfs/your-file.pdf"
    },
    # Add more items...
]
```

### Option 2: Use API

The portfolio loads from `/api/portfolio`. You can modify the data there.

---

## 📸 Image Requirements

- **Format:** JPG, PNG, GIF, WebP
- **Size:** Recommended 500x600px or larger
- **Quality:** High resolution for best display
- **Naming:** Use descriptive names

---

## 📄 PDF Requirements

- **Format:** PDF only
- **Size:** Keep under 10MB per file
- **Content:** Educational materials, guides, etc.
- **Naming:** Use descriptive Khmer/English names

---

## 🚀 Testing Your Content

1. **Restart Server:**
   ```bash
   cd d:\wep\library
   python server.py
   ```

2. **Check URLs:**
   - Images: `http://localhost:3000/images/your-image.jpg`
   - PDFs: `http://localhost:3000/pdfs/your-file.pdf`

3. **Test Download:** Click "ទាញយក" buttons on portfolio items

---

## 📋 Current Portfolio Items

| ID | Title | Image | PDF |
|----|-------|-------|-----|
| 0 | SPSS Guide | `/images/Jpg.jpg` | `/pdfs/ការណែនាំអំពីកម្មវិធី_SPSS.pdf` |
| 1 | RCBD Model | `/images/2.jpg` | `/pdfs/RCBD.pdf` |
| 2 | Experimental Design | `/images/3.jpg` | `/pdfs/RCB.pdf` |
| 3-8 | Sample Items | Picsum photos | No PDFs |

---

## 🔄 Updating the Website

After adding files:
1. Refresh your browser
2. Check browser console for errors
3. Test all download links
4. Verify images load properly

---

## 🆘 Troubleshooting

### Images Not Loading
- Check file exists in `public/images/`
- Verify filename matches exactly
- Check browser developer tools (F12) for 404 errors

### PDFs Not Downloading
- Check file exists in `public/pdfs/`
- Verify filename matches exactly
- Check file isn't corrupted

### Server Errors
- Restart the server: `python server.py`
- Check terminal for error messages
- Verify Flask is installed: `pip list | findstr Flask`

---

## 📞 Need Help?

If you need assistance:
1. Check the terminal output for error messages
2. Verify all files are in the correct folders
3. Ensure filenames match exactly (case-sensitive)
4. Test URLs directly in browser

---

**✅ Ready to add your content!**
Place your files in the folders above and restart the server.