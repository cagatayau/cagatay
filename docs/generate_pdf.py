#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teknoloji Sınavı Rehberi PDF Oluşturucu

Bu script, Markdown formatındaki teknoloji sınavı rehberini
professional PDF formatına dönüştürür.

Özellikler:
- Türkçe karakter desteği
- Professional layout
- İçindekiler tablosu
- Sayfa numaraları
- Başlık hiyerarşisi
- A4 format optimizasyonu
"""

import os
import sys
import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import logging
from datetime import datetime

# Logging ayarları
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TechnoloyExamGuidePDFGenerator:
    """Teknoloji Sınavı Rehberi PDF üretici sınıfı"""
    
    def __init__(self, markdown_file, output_file):
        """
        PDF generator başlatıcı
        
        Args:
            markdown_file (str): Markdown dosya yolu
            output_file (str): Çıktı PDF dosya yolu
        """
        self.markdown_file = markdown_file
        self.output_file = output_file
        self.font_config = FontConfiguration()
        
    def read_markdown(self):
        """Markdown dosyasını oku"""
        try:
            with open(self.markdown_file, 'r', encoding='utf-8') as f:
                content = f.read()
            logger.info(f"Markdown dosyası başarıyla okundu: {self.markdown_file}")
            return content
        except FileNotFoundError:
            logger.error(f"Markdown dosyası bulunamadı: {self.markdown_file}")
            raise
        except Exception as e:
            logger.error(f"Markdown dosyası okunurken hata: {e}")
            raise
    
    def markdown_to_html(self, markdown_content):
        """Markdown'ı HTML'e dönüştür"""
        try:
            # Markdown extensions for better formatting
            md = markdown.Markdown(
                extensions=[
                    'markdown.extensions.toc',      # Table of contents
                    'markdown.extensions.tables',   # Tables support
                    'markdown.extensions.codehilite', # Code highlighting
                    'markdown.extensions.fenced_code', # Fenced code blocks
                    'markdown.extensions.attr_list',   # Attribute lists
                    'pymdownx.superfences',         # Advanced code blocks
                    'pymdownx.tabbed',              # Tabbed content
                    'pymdownx.details',             # Details/summary
                ],
                extension_configs={
                    'markdown.extensions.toc': {
                        'permalink': False,
                        'baselevel': 1,
                        'title': 'İçindekiler',
                        'anchorlink': False  # Disable anchor links to avoid warnings
                    },
                    'markdown.extensions.codehilite': {
                        'css_class': 'highlight',
                        'use_pygments': True
                    }
                }
            )
            
            html_content = md.convert(markdown_content)
            toc = md.toc
            
            logger.info("Markdown başarıyla HTML'e dönüştürüldü")
            return html_content, toc
            
        except Exception as e:
            logger.error(f"Markdown HTML dönüştürme hatası: {e}")
            raise
    
    def create_complete_html(self, html_content, toc):
        """Tam HTML doküman oluştur"""
        
        # Türkçe karakter desteği için meta tags
        html_template = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teknoloji Sınavı Rehberi</title>
    <style>
        {css_styles}
    </style>
</head>
<body>
    <div class="cover-page">
        <h1 class="main-title">TEKNOLOJİ SINAVI REHBERİ</h1>
        <div class="subtitle">Detaylı Sınav Hazırlık Kılavuzu</div>
        <div class="date">Hazırlanma Tarihi: {date}</div>
        <div class="institution">Teknoloji ve İnovasyon Programı</div>
    </div>
    
    <div class="page-break"></div>
    
    <div class="toc-page">
        <h2 class="toc-title">İÇİNDEKİLER</h2>
        {toc}
    </div>
    
    <div class="page-break"></div>
    
    <div class="content">
        {content}
    </div>
</body>
</html>
        """.format(
            css_styles=self.get_css_styles(),
            date=datetime.now().strftime("%d.%m.%Y"),
            toc=toc,
            content=html_content
        )
        
        return html_template
    
    def get_css_styles(self):
        """CSS stillerini döndür"""
        css = """
        /* Temel sayfa ayarları */
        @page {
            size: A4;
            margin: 2.5cm 2cm 2.5cm 2cm;
            @bottom-center {
                content: counter(page);
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                font-size: 10pt;
                color: #666;
            }
        }
        
        @page :first {
            @bottom-center {
                content: "";
            }
        }
        
        /* Font ayarları - Türkçe karakter desteği */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 11pt;
            line-height: 1.6;
            color: #333;
            text-align: justify;
            hyphens: auto;
        }
        
        /* Kapak sayfası */
        .cover-page {
            text-align: center;
            padding-top: 5cm;
            page-break-after: always;
        }
        
        .main-title {
            font-size: 28pt;
            font-weight: bold;
            color: #1f4e79;
            margin-bottom: 1cm;
            letter-spacing: 2px;
        }
        
        .subtitle {
            font-size: 16pt;
            color: #4472c4;
            margin-bottom: 2cm;
        }
        
        .date {
            font-size: 12pt;
            margin-bottom: 0.5cm;
            color: #666;
        }
        
        .institution {
            font-size: 14pt;
            font-weight: bold;
            color: #1f4e79;
        }
        
        /* Sayfa sonu */
        .page-break {
            page-break-after: always;
        }
        
        /* İçindekiler */
        .toc-page {
            page-break-after: always;
        }
        
        .toc-title {
            font-size: 20pt;
            font-weight: bold;
            color: #1f4e79;
            text-align: center;
            margin-bottom: 1cm;
            border-bottom: 2px solid #4472c4;
            padding-bottom: 0.5cm;
        }
        
        .toc ul {
            list-style-type: none;
            padding-left: 0;
        }
        
        .toc li {
            margin-bottom: 0.3cm;
            padding-left: 1cm;
            text-indent: -1cm;
        }
        
        .toc a {
            text-decoration: none;
            color: #333;
            border-bottom: 1px dotted #999;
        }
        
        .toc a:hover {
            color: #4472c4;
        }
        
        /* Başlıklar */
        h1 {
            font-size: 20pt;
            font-weight: bold;
            color: #1f4e79;
            margin-top: 1cm;
            margin-bottom: 0.8cm;
            page-break-before: auto;
            page-break-after: avoid;
            border-bottom: 2px solid #4472c4;
            padding-bottom: 0.3cm;
        }
        
        h2 {
            font-size: 16pt;
            font-weight: bold;
            color: #4472c4;
            margin-top: 0.8cm;
            margin-bottom: 0.6cm;
            page-break-after: avoid;
        }
        
        h3 {
            font-size: 14pt;
            font-weight: bold;
            color: #5b9bd5;
            margin-top: 0.6cm;
            margin-bottom: 0.4cm;
            page-break-after: avoid;
        }
        
        h4 {
            font-size: 12pt;
            font-weight: bold;
            color: #70ad47;
            margin-top: 0.5cm;
            margin-bottom: 0.3cm;
            page-break-after: avoid;
        }
        
        /* Paragraflar */
        p {
            margin-bottom: 0.4cm;
            text-align: justify;
        }
        
        /* Listeler */
        ul, ol {
            margin-bottom: 0.4cm;
            padding-left: 1.2cm;
        }
        
        li {
            margin-bottom: 0.2cm;
        }
        
        /* Vurgulu metinler */
        strong, b {
            font-weight: bold;
            color: #1f4e79;
        }
        
        em, i {
            font-style: italic;
            color: #4472c4;
        }
        
        /* Kod blokları */
        code {
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
            background-color: #f8f9fa;
            padding: 0.1cm 0.2cm;
            border-radius: 3px;
            font-size: 10pt;
        }
        
        pre {
            background-color: #f8f9fa;
            padding: 0.5cm;
            border-radius: 5px;
            border-left: 4px solid #4472c4;
            overflow-x: auto;
            margin-bottom: 0.6cm;
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
            font-size: 9pt;
            line-height: 1.4;
        }
        
        /* Tablolar */
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 0.6cm;
            font-size: 10pt;
        }
        
        th {
            background-color: #4472c4;
            color: white;
            padding: 0.3cm;
            border: 1px solid #ddd;
            font-weight: bold;
            text-align: left;
        }
        
        td {
            padding: 0.3cm;
            border: 1px solid #ddd;
        }
        
        tr:nth-child(even) {
            background-color: #f8f9fa;
        }
        
        /* Sınav soruları bölümü */
        .exam-section {
            background-color: #fff2cc;
            padding: 0.5cm;
            border-left: 5px solid #ffc000;
            margin-bottom: 0.6cm;
            page-break-inside: avoid;
        }
        
        .question-number {
            font-weight: bold;
            color: #d35400;
            font-size: 12pt;
        }
        
        .question-points {
            float: right;
            background-color: #e74c3c;
            color: white;
            padding: 0.1cm 0.3cm;
            border-radius: 3px;
            font-size: 9pt;
            font-weight: bold;
        }
        
        /* Cevap anahtarları */
        .answer-key {
            background-color: #e8f5e8;
            padding: 0.5cm;
            border-left: 5px solid #27ae60;
            margin-bottom: 0.6cm;
            page-break-inside: avoid;
        }
        
        /* Uyarı kutuları */
        .warning {
            background-color: #fff3cd;
            border-left: 5px solid #ffc107;
            padding: 0.5cm;
            margin-bottom: 0.6cm;
        }
        
        .info {
            background-color: #d1ecf1;
            border-left: 5px solid #17a2b8;
            padding: 0.5cm;
            margin-bottom: 0.6cm;
        }
        
        /* Sayfa kenarboşlukları ve widows/orphans kontrolü */
        .content {
            widows: 3;
            orphans: 3;
        }
        
        /* Print optimizasyonları */
        @media print {
            body {
                font-size: 10pt;
            }
            
            h1 {
                font-size: 18pt;
            }
            
            h2 {
                font-size: 14pt;
            }
            
            h3 {
                font-size: 12pt;
            }
            
            .page-break {
                page-break-after: always;
            }
        }
        """
        
        return css
    
    def generate_pdf(self):
        """PDF dosyasını oluştur"""
        try:
            # Markdown içeriğini oku
            markdown_content = self.read_markdown()
            
            # HTML'e dönüştür
            html_content, toc = self.markdown_to_html(markdown_content)
            
            # Tam HTML doküman oluştur
            complete_html = self.create_complete_html(html_content, toc)
            
            # Output dizinini oluştur
            output_dir = os.path.dirname(self.output_file)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
                logger.info(f"Output dizini oluşturuldu: {output_dir}")
            
            # PDF oluştur
            logger.info("PDF oluşturma işlemi başlatılıyor...")
            
            html_doc = HTML(string=complete_html, encoding='utf-8')
            
            # PDF üret
            html_doc.write_pdf(
                self.output_file,
                font_config=self.font_config,
                optimize_size=('fonts', 'images')
            )
            
            logger.info(f"PDF başarıyla oluşturuldu: {self.output_file}")
            
            # Dosya boyutu bilgisi
            file_size = os.path.getsize(self.output_file)
            file_size_mb = file_size / (1024 * 1024)
            logger.info(f"PDF dosya boyutu: {file_size_mb:.2f} MB")
            
            return True
            
        except Exception as e:
            logger.error(f"PDF oluşturma hatası: {e}")
            raise

def main():
    """Ana fonksiyon"""
    try:
        # Dosya yolları
        script_dir = os.path.dirname(os.path.abspath(__file__))
        markdown_file = os.path.join(script_dir, 'teknoloji_sinav_rehberi.md')
        output_file = os.path.join(script_dir, 'output', 'Teknoloji_Sinav_Rehberi.pdf')
        
        # Markdown dosyasının varlığını kontrol et
        if not os.path.exists(markdown_file):
            logger.error(f"Markdown dosyası bulunamadı: {markdown_file}")
            return False
        
        # PDF generator oluştur
        generator = TechnoloyExamGuidePDFGenerator(markdown_file, output_file)
        
        # PDF üret
        success = generator.generate_pdf()
        
        if success:
            print(f"\n✅ PDF başarıyla oluşturuldu!")
            print(f"📁 Dosya konumu: {output_file}")
            print(f"📄 Dosya boyutu: {os.path.getsize(output_file) / (1024*1024):.2f} MB")
            return True
        else:
            print("\n❌ PDF oluşturma işlemi başarısız!")
            return False
            
    except Exception as e:
        logger.error(f"Ana fonksiyon hatası: {e}")
        print(f"\n❌ Hata: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)