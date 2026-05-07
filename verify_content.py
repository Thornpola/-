#!/usr/bin/env python3
"""
Content Verification Script
Run: python verify_content.py
"""

import os
import sys

def check_files():
    """Check if required content files exist"""
    base_path = os.path.join(os.path.dirname(__file__), 'public')

    # Required images
    required_images = [
        'Jpg.jpg',
        '2.jpg',
        '3.jpg',
        'photo_2026-01-26_12-43-09.jpg'
    ]

    # Required PDFs
    required_pdfs = [
        'ការណែនាំអំពីកម្មវិធី_SPSS.pdf',
        'RCBD.pdf',
        'RCB.pdf'
    ]

    print("🔍 Checking Content Files...\n")

    # Check images
    print("📸 IMAGES:")
    images_path = os.path.join(base_path, 'images')
    for img in required_images:
        img_path = os.path.join(images_path, img)
        if os.path.exists(img_path):
            print(f"  ✅ {img}")
        else:
            print(f"  ❌ {img} - MISSING")

    print("\n📄 PDFs:")
    pdfs_path = os.path.join(base_path, 'pdfs')
    for pdf in required_pdfs:
        pdf_path = os.path.join(pdfs_path, pdf)
        if os.path.exists(pdf_path):
            print(f"  ✅ {pdf}")
        else:
            print(f"  ❌ {pdf} - MISSING")

    print("\n" + "="*50)
    print("💡 To add missing files:")
    print("   Images → public/images/")
    print("   PDFs   → public/pdfs/")
    print("   Use exact filenames as shown above")
    print("="*50)

if __name__ == "__main__":
    check_files()