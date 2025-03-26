# Modern QR Generator

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.7+-blue)](https://www.python.org/downloads/)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

**A sleek, modern QR code generator with a beautiful user interface and customization options.**

[Key Features](#key-features) • [Installation](#installation) • [Usage](#usage) • [Screenshots](#screenshots) • [Dependencies](#dependencies) • [License](#license)

</div>

## Key Features

✨ **Modern UI**: Clean, responsive interface with light and dark theme support  
🎨 **Customization**: Adjust size, error correction level, and choose from multiple colors  
💾 **Export Options**: Save your QR codes as PNG files  
🔄 **Real-time Preview**: See your QR code as you create it  
🌐 **Multi-platform**: Works on Windows, macOS, and Linux  
📱 **Responsive Layout**: Adapts to different window sizes

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/shendjs/ModernQRGenerator.git
cd ModernQRGenerator
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install qrcode[pil] pillow customtkinter
```

4. Run the application:
```bash
python qrgenerator.py
```

## Usage

1. **Enter Content**: Type or paste your text, URL, or data in the input field
2. **Customize**: 
   - Adjust the size using the slider
   - Select an error correction level (L, M, Q, H)
   - Choose a fill color for your QR code
3. **Generate**: Click the "Generate" button to create your QR code
4. **Save**: Use the "Save" button to export your QR code as a PNG file

### Error Correction Levels

- **L (Low)**: 7% of data can be restored if damaged
- **M (Medium)**: 15% of data can be restored if damaged
- **Q (Quartile)**: 25% of data can be restored if damaged
- **H (High)**: 30% of data can be restored if damaged

## Screenshots

<div align="center">
  <img src="https://raw.githubusercontent.com/user/repo/main/screenshots/light-theme.png" width="49%" alt="Light Theme">
  <img src="https://raw.githubusercontent.com/user/repo/main/screenshots/dark-theme.png" width="49%" alt="Dark Theme">
</div>

## Dependencies

- [qrcode](https://github.com/lincolnloop/python-qrcode): QR code generation
- [Pillow (PIL)](https://python-pillow.org/): Image processing
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter): Modern UI widgets

## Project Structure

```
modern-qr-generator/
├── qrgenerator.py      # Main application file
├── screenshots/         # App screenshots for documentation
├── LICENSE              # MIT License
└── README.md            # Project documentation
```

## Planned Features

- [ ] Add logo/image embedding in QR codes
- [ ] Additional export formats (SVG, PDF)
- [ ] Batch QR code generation
- [ ] Custom styling templates
- [ ] History of generated QR codes

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Icons and design inspiration from modern UI/UX trends
- Built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)

---

<div align="center">
  <sub>Created by Shend with ❤️</sub>
</div>
