# termpix

A terminal tool that displays pixelated ASCII art in your terminal, inspired by `ponysay` and `cowsay`.
Includes a tool for converting images to ASCII art, with basic image processing.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![AUR](https://img.shields.io/badge/AUR-pytermpix-blue.svg)

**AUR Package**: [pytermpix](https://aur.archlinux.org/packages/pytermpix)

## Installation

### From AUR 
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

### Using pip
```bash
git clone https://github.com/casperrr/termpix.git
cd termpix
pip install .
# or
pipx install .
```

## Features

- **Convert any image** to terminal ASCII art
- **Support for URLs** - directly load images from the web
- **Custom scaling** - resize output to fit your terminal
- **Background removal** - transparency threshold control
- **Random art** - includes 25+ pre-made pixel art files

***

### Dependencies
- Python 3.9+
- Pillow (PIL)
- requests
- validators

## Usage

### Basic Usage
```bash
# Display random pixel art
termpix

# Get help
termpix --help

# List available termpix file names
termpix -l

# List and display available termpix images
termpix -L

# Display a specific termpix image
termpix -s <termpix-file>

# Display a random termpix image from a custom tpix directory
termpix -d /path/to/custom/tpix/directory

# Display a specific termpix image using filename/path
termpix -f <termpix-file>
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

# Batch processing with saving
termpix tool -f input.jpg -o art.tpix --save-processed processed.png -r
```

## Command Line Options

### Main Commands
| Option | Description |
|--------|-------------|
| `tool` | Access the image conversion tool |
| `-m` | Debug mode |
| `-h, --help` | Show help message |
| `-l, --list` | List available termpix file names |
| `-L, --list-imgs` | List available termpix images |
| `-s, --select` | Select a specific termpix image | 
| `-d, --directory` | Display a random termpix image from a custom tpix directory |
| `-f, --file` | Select a specific termpix file path to display |

### Tool Options
| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--file` | `-f` | string | - | Local image file path |
| `--link` | `-l` | string | - | Image URL |
| `--output-location` | `-o` | string | `/usr/share/termpix/tpix` | Output .tpix file location |
| `--scale` | `-s` | int int | 70 100 | Width and height scaling |
| `--interpolation` | `-i` | flag | false | Enable smooth scaling |
| `--thresh` | `-t` | int | 128 | Background transparency (0-255) |
| `--quantization` | `-q` | int | 255 | Color quantization level (0-255) |
| `--hide-result` | `-r` | flag | false | Don't display output |
| `--save-processed` | - | string | - | Save processed image path |
| `--img-data` | - | flag | false | Show image metadata |

## 📁 File Formats

### Supported Input
- **Images**: JPEG, PNG
- **URLs**: Direct links to supported image formats

### Output Formats
- **Terminal**: Direct ASCII art display
- **.tpix**: Fancy name for a text file with ASCII art

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by `ponysay` and `cowsay`
- Built with Python and PIL/Pillow
- ASCII art conversion algorithms
- Community pixel art contributions

***

