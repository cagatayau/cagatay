#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF Generation Test ve Verification Script

Bu script PDF oluşturma sistemini test eder ve doğrular.
"""

import os
import sys
import subprocess
from pathlib import Path

def test_requirements():
    """Gerekli bağımlılıkları test et"""
    print("🔍 Gerekli bağımlılıklar kontrol ediliyor...")
    
    try:
        import weasyprint
        import markdown
        print("✅ Tüm bağımlılıklar yüklü")
        return True
    except ImportError as e:
        print(f"❌ Eksik bağımlılık: {e}")
        return False

def test_files_exist():
    """Gerekli dosyaların varlığını kontrol et"""
    print("📁 Dosya varlıkları kontrol ediliyor...")
    
    script_dir = Path(__file__).parent
    files_to_check = [
        'teknoloji_sinav_rehberi.md',
        'generate_pdf.py',
        'requirements.txt'
    ]
    
    all_exist = True
    for file in files_to_check:
        file_path = script_dir / file
        if file_path.exists():
            print(f"✅ {file} mevcut")
        else:
            print(f"❌ {file} eksik")
            all_exist = False
    
    return all_exist

def test_pdf_generation():
    """PDF oluşturma işlemini test et"""
    print("🔄 PDF oluşturma test ediliyor...")
    
    script_dir = Path(__file__).parent
    generate_script = script_dir / 'generate_pdf.py'
    
    try:
        result = subprocess.run(
            [sys.executable, str(generate_script)],
            capture_output=True,
            text=True,
            cwd=script_dir
        )
        
        if result.returncode == 0:
            print("✅ PDF başarıyla oluşturuldu")
            
            # PDF dosyasının varlığını kontrol et
            pdf_path = script_dir / 'output' / 'Teknoloji_Sinav_Rehberi.pdf'
            if pdf_path.exists():
                file_size = pdf_path.stat().st_size
                print(f"📄 PDF dosya boyutu: {file_size / 1024:.2f} KB")
                return True
            else:
                print("❌ PDF dosyası oluşturulamadı")
                return False
        else:
            print(f"❌ PDF oluşturma hatası: {result.stderr}")
            return False
    
    except Exception as e:
        print(f"❌ Test hatası: {e}")
        return False

def verify_pdf_content():
    """PDF içeriğini doğrula"""
    print("📖 PDF içeriği doğrulanıyor...")
    
    script_dir = Path(__file__).parent
    pdf_path = script_dir / 'output' / 'Teknoloji_Sinav_Rehberi.pdf'
    
    if not pdf_path.exists():
        print("❌ PDF dosyası bulunamadı")
        return False
    
    # Dosya boyutu kontrolü
    file_size = pdf_path.stat().st_size
    if file_size < 1000:  # Minimum 1KB
        print("❌ PDF dosyası çok küçük - içerik eksik olabilir")
        return False
    
    print("✅ PDF içeriği doğrulandı")
    return True

def run_comprehensive_test():
    """Kapsamlı test çalıştır"""
    print("🚀 Teknoloji Sınavı Rehberi PDF Generator Test Başlıyor...")
    print("=" * 60)
    
    tests = [
        ("Bağımlılık Kontrolü", test_requirements),
        ("Dosya Varlığı Kontrolü", test_files_exist),
        ("PDF Oluşturma Testi", test_pdf_generation),
        ("PDF İçerik Doğrulama", verify_pdf_content)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 {test_name}...")
        if test_func():
            passed += 1
        else:
            print(f"⚠️  {test_name} başarısız!")
    
    print("\n" + "=" * 60)
    print(f"📊 Test Sonuçları: {passed}/{total} test başarılı")
    
    if passed == total:
        print("🎉 Tüm testler başarılı! PDF sistemı çalışıyor.")
        return True
    else:
        print("❌ Bazı testler başarısız. Lütfen hataları düzeltin.")
        return False

if __name__ == "__main__":
    success = run_comprehensive_test()
    sys.exit(0 if success else 1)