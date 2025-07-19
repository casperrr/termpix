# 🎨 termpix

A powerful terminal tool that displays pixelated ASCII art in your terminal, inspired by `ponysay` and `cowsay`. Convert any image into beautiful terminal art with customizable scaling, colors, and effects!

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![AUR](https://img.shields.io/badge/AUR-pytermpix-blue.svg)

## ✨ Features

- 🖼️ **Convert any image** to terminal ASCII art
- 🌐 **Support for URLs** - directly load images from the web
- 🎨 **Color quantization** - adjust color depth (0-255)
- 📏 **Custom scaling** - resize output to fit your terminal
- 🔍 **Interpolation** - smooth scaling for better quality
- 🎭 **Background removal** - transparency threshold control
- 💾 **Save outputs** - export processed images and .tpix files
- 📊 **Image analysis** - view detailed image metadata
- 🎲 **Random art** - includes 25+ pre-made pixel art files

## 🚀 Installation

### From AUR (Arch Linux)
```bash
# Using yay
yay -S pytermpix

# Using paru
paru -S pytermpix

# Manual installation
git clone https://aur.archlinux.org/pytermpix.git
cd pytermpix
makepkg -si
```

### From Source
```bash
git clone https://github.com/casperrr/termpix.git
cd termpix
pip install -e .
```

### Dependencies
- Python 3.9+
- Pillow (PIL)
- requests
- validators

## 📖 Usage

### Basic Usage
```bash
# Display random pixel art
termpix

# Get help
termpix --help
```

### Image Conversion Tool
```bash
# Convert local image
termpix tool -f /path/to/image.jpg

# Convert from URL
termpix tool -l https://example.com/image.png

# Custom scaling (width x height)
termpix tool -f image.jpg -s 80 40

# Enable interpolation for smoother scaling
termpix tool -f image.jpg -i

# Adjust background transparency threshold (0-255)
termpix tool -f image.jpg -t 100

# Color quantization (reduce colors)
termpix tool -f image.jpg -q 16

# Save processed image
termpix tool -f image.jpg --save-processed output.png

# Save as .tpix file
termpix tool -f image.jpg -o myart.tpix

# Hide output (useful when just saving)
termpix tool -f image.jpg -r -o myart.tpix

# Show image metadata
termpix tool -f image.jpg --img-data
```

### Advanced Examples
```bash
# Perfect for terminal: scaled, quantized, with interpolation
termpix tool -f photo.jpg -s 60 30 -q 32 -i -t 50

# Create low-fi pixel art
termpix tool -l "https://picsum.photos/200" -s 40 20 -q 8

# Batch processing with saving
termpix tool -f input.jpg -o art.tpix --save-processed processed.png -r
```

## 🎨 Pre-included Art

termpix comes with 25+ pixel art files including:
- **Characters**: Adventure Time, Bender, GLaDOS, Yoda, Guy Fawkes
- **Gaming**: TF2 characters (Medic, Pyro, Sniper, Spy), Big Daddy, Vault Boy
- **Memes**: Tux penguin, Blob fish, Reddit logo, Pooh bear
- **And many more!**

Run `termpix` without arguments to see a random piece!

## 🔧 Command Line Options

### Main Commands
| Option | Description |
|--------|-------------|
| `tool` | Access the image conversion tool |
| `-m` | Debug mode |
| `-h, --help` | Show help message |

### Tool Options
| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--file` | `-f` | string | - | Local image file path |
| `--link` | `-l` | string | - | Image URL |
| `--output-location` | `-o` | string | - | Output .tpix file location |
| `--scale` | `-s` | int int | 70 100 | Width and height scaling |
| `--interpolation` | `-i` | flag | false | Enable smooth scaling |
| `--thresh` | `-t` | int | 128 | Background transparency (0-255) |
| `--quantization` | `-q` | int | 255 | Color quantization level (0-255) |
| `--hide-result` | `-r` | flag | false | Don't display output |
| `--save-processed` | - | string | - | Save processed image path |
| `--img-data` | - | flag | false | Show image metadata |

## 📁 File Formats

### Supported Input
- **Images**: JPEG, PNG, GIF, BMP, TIFF, WebP
- **URLs**: Direct links to supported image formats

### Output Formats
- **Terminal**: Direct ASCII art display
- **.tpix**: Custom termpix format for storing terminal art
- **Processed images**: Save modified images in original formats

## 🔧 Development

### Project Structure
```
termpix/
├── src/termpix/          # Main package
│   ├── __init__.py       # Package exports
│   ├── __main__.py       # CLI entry point
│   ├── termpix.py        # Core display logic
│   └── termpixtool/      # Image processing tools
├── tpix/                 # Pre-made pixel art
├── PKGBUILD             # Arch Linux package
└── pyproject.toml       # Python package config
```

### Contributing
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make changes and test
4. Commit: `git commit -m "feat: add new feature"`
5. Push: `git push origin feature-name`
6. Open a Pull Request

### Building
```bash
python -m build
pip install dist/*.whl
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by `ponysay` and `cowsay`
- Built with Python and PIL/Pillow
- ASCII art conversion algorithms
- Community pixel art contributions

## 🐛 Issues & Support

- **Bug Reports**: [GitHub Issues](https://github.com/casperrr/termpix/issues)
- **Feature Requests**: [GitHub Discussions](https://github.com/casperrr/termpix/discussions)
- **AUR Package**: [pytermpix](https://aur.archlinux.org/packages/pytermpix)

---

Made with ❤️ by [casperrr](https://github.com/casperrr)
