require('dotenv').config();
const express = require('express');
const cors = require('cors');
const compression = require('compression');
const helmet = require('helmet');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3000;
const HOST = process.env.HOST || 'localhost';
const NODE_ENV = process.env.NODE_ENV || 'development';

// Security & Performance Middleware
app.use(helmet());
app.use(compression());
app.use(cors());

// Body parsing
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static files from public directory
app.use(express.static(path.join(__dirname, 'public')));

// API Route: Get configuration for frontend
app.get('/api/config', (req, res) => {
  const protocol = NODE_ENV === 'production' ? 'https' : 'http';
  const baseUrl = NODE_ENV === 'production' 
    ? process.env.PROD_URL 
    : `${protocol}://${HOST}:${PORT}`;
  
  res.json({
    environment: NODE_ENV,
    baseUrl,
    apiUrl: `${baseUrl}/api`,
    contactEmail: process.env.CONTACT_EMAIL,
    phone: process.env.PHONE
  });
});

// API Route: Handle contact form submissions
app.post('/api/contact', (req, res) => {
  const { name, email, message, subject } = req.body;
  
  // Validation
  if (!name || !email || !message) {
    return res.status(400).json({
      success: false,
      message: 'Missing required fields: name, email, message'
    });
  }
  
  // Log the message (in production, send email)
  console.log('📧 New contact message:', {
    name,
    email,
    subject: subject || 'No subject',
    message,
    timestamp: new Date().toISOString()
  });
  
  // In production, integrate with email service (SendGrid, Nodemailer, etc.)
  if (NODE_ENV === 'production') {
    // TODO: Send email using email service
    console.log('Email would be sent in production');
  }
  
  res.json({
    success: true,
    message: 'Message received! We will get back to you soon.'
  });
});

// API Route: Get portfolio items
app.get('/api/portfolio', (req, res) => {
  const portfolio = [
    {
      id: 0,
      title: 'ការណែនាំអំពីកម្មវិធី SPSS',
      description: 'SPSS គឺជាសំណុំ ប្រើដើម្បីវិភាគទិន្នន័យប្រកបដោយប្រសិទ្ធភាព និងគ្រប់គ្រងទិន្នន័យជាប្រព័ន្ធ។',
      image: '/images/Jpg.jpg',
      pdf: '/pdfs/ការណែនាំអំពីកម្មវិធី_SPSS.pdf'
    },
    {
      id: 1,
      title: 'គំរូប្លង់ RCBD',
      description: 'ការវិភាគទិន្នន័យតាមកម្មវិធីSPSSគំរូប្លង់ RCBD',
      image: '/images/2.jpg',
      pdf: '/pdfs/RCBD.pdf'
    },
    {
      id: 2,
      title: 'ការរៀបចំផែនការពិសោធន៍',
      description: 'ការរៀបចំផែការសាកល្បងដោយចៃដន្យនៅក្នុងប្លុងពេញលេញ',
      image: '/images/3.jpg',
      pdf: '/pdfs/RCB.pdf'
    }
  ];
  
  res.json({ success: true, data: portfolio });
});

// Serve index.html for all other routes (SPA support)
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Error:', err);
  res.status(500).json({
    success: false,
    message: 'Internal Server Error',
    error: NODE_ENV === 'development' ? err.message : undefined
  });
});

// Start server
app.listen(PORT, HOST, () => {
  const url = `http://${HOST}:${PORT}`;
  console.log(`
╔══════════════════════════════════════════════════════════╗
║         🎬 Pola Entertainment Server Started             ║
╠══════════════════════════════════════════════════════════╣
║ Server URL:  ${url}
║ Environment: ${NODE_ENV}
║ Port:        ${PORT}
║ Host:        ${HOST}
╚══════════════════════════════════════════════════════════╝
  `);
});

// Graceful shutdown
process.on('SIGTERM', () => {
  console.log('SIGTERM received, shutting down gracefully');
  process.exit(0);
});
