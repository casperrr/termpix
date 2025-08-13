# Maintainer: casperrr
pkgname=pytermpix
pkgver=1.1.0
pkgrel=1
pkgdesc="Convert and display images as pixel art in an ANSI terminal"
arch=('any')
url="https://github.com/casperrr/termpix"
license=('MIT')
depends=('python' 'python-pillow' 'python-requests' 'python-validators')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-hatchling')
source=("$pkgname-$pkgver.tar.gz::https://github.com/casperrr/termpix/archive/v$pkgver.tar.gz")
sha256sums=('8530f72197b7ced0d01fedd5b7b10a595b420a75a45ad87d5c72f17f26aa1d2a')

build() {
    cd "termpix-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "termpix-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
}
