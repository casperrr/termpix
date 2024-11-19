# Maintainer: casperrr
pkgname=termpix
pkgver=r23.67fca5e
pkgrel=1
pkgdesc="This is a test"
arch=('any')
url="http://github.com/casperrr/termpix"
licencse=('GNU')
depends=('python' 'python-pillow')
makedepends=('git' 'python-setuptools')
# source=("$pkgname-$pkgver.tar.gz::")
soruce=("$pkgname::git+https://github.com/casperrr/termpix.git#branch=package")
# md5sums=('SKIP')

pkgver() {
    cd "$srcdir"
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
    # cd "$srcdir/$pkgname"
    cd "$srcdir"
    python setup.py build
}

package() {
    # cd "$srcdir/$pkgname"
    cd "$srcdir"
    pip install --prefix=/usr --root "$pkgdir" .
    # python setup.py install
}
