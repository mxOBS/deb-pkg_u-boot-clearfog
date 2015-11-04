#
# spec file for package u-boot-mx6cubox-imarvell-clearfog
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2010 Texas Instruments Inc by Nishanth Menon
# Copyright (c) 2007-2010 by Silvan Calarco <silvan.calarco@mambasoft.it>
# Copyright (c) 2015 Josua Mayer
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           u-boot-marvell-clearfog
Version:        2013.01
Release:        1
Summary:        The u-boot firmware by Marvell for the Clearfog board
License:        GPL-2.0
Group:          System/Boot
Url:            https://github.com/MarvellEmbeddedProcessors/u-boot-armada38x/tree/u-boot-2013.01-15t1-clearfog
Source:         u-boot-marvell-clearfog_2013.01pkg1.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       u-boot-loader
Conflicts:      otherproviders(u-boot-loader)
ExclusiveArch:  armv7l armv7hl

# sources are incompatible with gcc v5.x
%if 0%{?suse_version} > 1320
BuildRequires: gcc48
%endif

%description
Das U-Boot (or just "U-Boot" for short) is Open Source Firmware for Embedded PowerPC, ARM, MIPS and x86 processors.
This package contains the firmware for the clearfog arm platform.

%package doc
Summary:        Documentation for the u-boot Firmware
Group:          Documentation/Other

%description doc
Das U-Boot (or just "U-Boot" for short) is Open Source Firmware for Embedded PowerPC, ARM, MIPS and x86 processors.
This package contains documentation for u-boot firmware

%prep
%setup -q -n u-boot-marvell-clearfog-2013.01pkg1
cd u-boot
patch -p1 < ../raw-initrd.patch
patch -p1 < ../armhf.patch
patch -p1 < ../enable-stage-boot.patch
cd ..

%build
cd u-boot
%if 0%{?suse_version} > 1320
export CC=gcc-4.8 CXX=g++-4.8
%endif
make %{?jobs:-j %jobs} CFLAGS="$RPM_OPT_FLAGS" armada_38x_clearfog_config
make %{?jobs:-j %jobs} u-boot.mmc

%install
cd u-boot
install -D -m 0644 u-boot.mmc %{buildroot}/boot/u-boot-clearfog.mmc

%files
%defattr(-,root,root)
/boot/*
%doc u-boot/COPYING u-boot/CREDITS u-boot/README

%files doc
%defattr(-,root,root)
# Generic documents
%doc u-boot/doc/README.JFFS2 u-boot/doc/README.JFFS2_NAND u-boot/doc/README.commands
%doc u-boot/doc/README.autoboot u-boot/doc/README.commands u-boot/doc/README.console u-boot/doc/README.dns
%doc u-boot/doc/README.hwconfig u-boot/doc/README.nand u-boot/doc/README.NetConsole u-boot/doc/README.serial_multi
%doc u-boot/doc/README.SNTP u-boot/doc/README.standalone u-boot/doc/README.update u-boot/doc/README.usb
%doc u-boot/doc/README.video u-boot/doc/README.VLAN u-boot/doc/README.silent u-boot/doc/README.POST u-boot/doc/README.Modem
# Now any h/w dependent Documentation
%doc u-boot/doc/README.ARM-SoC u-boot/doc/README.ARM-memory-map 

%changelog
