# Bitwig Studio RPM

Since I need to use [yabridge](https://github.com/robbert-vdh/yabridge) for Windows-based VSTs like [Piapro Studio](https://piaprostudio.com/?lang=en), and yabridge is cumbersome to use with Bitwig's Flatpak, this SPEC config was born. It'll continue to be maintained until then.

Works with Fedora 36.

As of Bitwig 4.3, this package requires [aflyhorse/libjpeg](https://copr.fedorainfracloud.org/coprs/aflyhorse/libjpeg/) to provide `libjpeg.so.8`.

## Build instructions

- `sudo dnf copr enable aflyhorse/libjpeg`
- `sudo dnf in libjpeg8`
- `./build` OR `mock --sources . --spec bitwig-studio.spec` (preferred)
- If you used `mock`, package will be in `/var/lib/mock/fedora-$VERSION-$ARCH/result/bitwig-studio[...]`

## License

GPLv3