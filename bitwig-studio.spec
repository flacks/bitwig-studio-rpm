Name:		bitwig-studio
Version:	5.1
Release:	1%{?dist}
Summary:	DAW & music production software
License:	Proprietary
URL:		https://bitwig.com
Source0:	https://downloads.bitwig.com/stable/%{version}/%{name}-%{version}.deb

%description
Bitwig Studio is a digital audio workstation (DAW) and music production software.

%prep
ar p %{_topdir}/SOURCES/%{name}-%{version}.deb data.tar.xz | tar -xJf -

%install
cp -a opt usr %{buildroot}
export QA_RPATHS=$(( 0x0020|0x0002 ))

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
/usr/share/icons/hicolor/scalable/mimetypes/com.bitwig.BitwigStudio.application-bitwig-impulse.svg
/usr/share/icons/hicolor/scalable/mimetypes/com.bitwig.BitwigStudio.application-bitwig-modulator.svg
/usr/share/icons/hicolor/scalable/mimetypes/com.bitwig.BitwigStudio.application-bitwig-module.svg
/usr/share/icons/hicolor/scalable/mimetypes/com.bitwig.BitwigStudio.application-bitwig-package.svg
/usr/share/icons/hicolor/scalable/mimetypes/com.bitwig.BitwigStudio.application-bitwig-preset.svg
/usr/share/icons/hicolor/scalable/mimetypes/com.bitwig.BitwigStudio.application-bitwig-project-folder.svg
/usr/share/icons/hicolor/scalable/mimetypes/com.bitwig.BitwigStudio.application-bitwig-project.svg
/usr/share/icons/hicolor/scalable/mimetypes/com.bitwig.BitwigStudio.application-bitwig-remote-controls.svg
/usr/share/icons/hicolor/scalable/mimetypes/com.bitwig.BitwigStudio.audio-x.dawproject.svg
/usr/share/metainfo/com.bitwig.BitwigStudio.appdata.xml
/usr/share/mime/packages/com.bitwig.BitwigStudio.xml

%changelog
* Mon Jan 8 2024 Jean Lucas <jean@4ray.co> - 5.1
- 5.1

* Wed May 10 2023 Jean Lucas <jean@4ray.co> - 4.4.10
- 4.4.10

* Fri Jan 27 2023 Jean Lucas <jean@4ray.co> - 4.4.6
- 4.4.6

* Mon Dec 12 2022 Jean Lucas <jean@4ray.co> - 4.4.5
- 4.4.5

* Sun Oct 9 2022 Jean Lucas <jean@4ray.co> - 4.3.10-1
- 4.3.10

* Fri Sep 23 2022 Jean Lucas <jean@4ray.co> - 4.3.8-1
- 4.3.8

* Mon Aug 22 2022 Jean Lucas <jean@4ray.co> - 4.3.4-1
- 4.3.4

* Sat Jul 2 2022 Jean Lucas <jean@4ray.co> - 4.3-1
- Version bump to 4.3, add README

* Tue Apr 19 2022 Jean Lucas <jean@4ray.co> - 4.2.3-1
- Version bump to 4.2.3, add build script

* Sat Mar 12 2022 Jean Lucas <jean@4ray.co> - 4.2-1
- Version bump to 4.2

* Sun Dec 26 2021 Jean Lucas <jean@4ray.co> - 4.1.2-1
- Initial commit
