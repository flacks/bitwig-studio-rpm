Name:           bitwig-studio
Version:        4.1.2
Release:        1%{?dist}
Summary:        DAW & music production software

License:        Proprietary
URL:            https://bitwig.com
Source0:        https://downloads-na.bitwig.com/stable/%{version}/%{name}-%{version}.deb

%description
Bitwig Studio is a digital audio workstation (DAW) and music production software.

%prep
ar p %{_topdir}/SOURCES/%{name}-%{version}.deb data.tar.xz | tar -xJf -

%install
cp -a opt usr %{buildroot}
export QA_RPATHS=$[ 0x0020|0x0002 ]

%files
/opt/bitwig-studio
/usr/bin/bitwig-studio
/usr/share/applications/com.bitwig.BitwigStudio.desktop
/usr/share/icons/hicolor/128x128/apps/com.bitwig.BitwigStudio.png
/usr/share/icons/hicolor/48x48/apps/com.bitwig.BitwigStudio.png
/usr/share/icons/hicolor/scalable/apps/com.bitwig.BitwigStudio.svg
/usr/share/icons/hicolor/scalable/mimetypes/com.bitwig.BitwigStudio.application-bitwig-clip.svg
/usr/share/icons/hicolor/scalable/mimetypes/com.bitwig.BitwigStudio.application-bitwig-device.svg
/usr/share/icons/hicolor/scalable/mimetypes/com.bitwig.BitwigStudio.application-bitwig-extension.svg
/usr/share/icons/hicolor/scalable/mimetypes/com.bitwig.BitwigStudio.application-bitwig-modulator.svg
/usr/share/icons/hicolor/scalable/mimetypes/com.bitwig.BitwigStudio.application-bitwig-module.svg
/usr/share/icons/hicolor/scalable/mimetypes/com.bitwig.BitwigStudio.application-bitwig-package.svg
/usr/share/icons/hicolor/scalable/mimetypes/com.bitwig.BitwigStudio.application-bitwig-preset.svg
/usr/share/icons/hicolor/scalable/mimetypes/com.bitwig.BitwigStudio.application-bitwig-project-folder.svg
/usr/share/icons/hicolor/scalable/mimetypes/com.bitwig.BitwigStudio.application-bitwig-project.svg
/usr/share/icons/hicolor/scalable/mimetypes/com.bitwig.BitwigStudio.application-bitwig-remote-controls.svg
/usr/share/metainfo/com.bitwig.BitwigStudio.appdata.xml
/usr/share/mime/packages/com.bitwig.BitwigStudio.xml

%changelog
* Sun Dec 26 2021 Jean Lucas <jean@4ray.co> - 4.1.2-1
- Initial commit
