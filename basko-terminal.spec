%define _unpackaged_files_terminate_build 1

Name: basko-terminal
Version: 0.9.0
Release: alt1

Summary: Modified terminal emulator application for Xfce
Summary(ru_RU.UTF-8): Модифицированный эмулятор терминала для Xfce
License: GPLv2+
Group: Terminals
Url: https://github.com/r4nc-375/basko-terminal
Vcs: https://github.com/r4nc-375/basko-terminal

Source: %name-%version.tar

Requires: xfce4-common
Requires: libvte3

BuildRequires(pre): rpm-macros-xfce4
BuildRequires: xfce4-dev-tools
BuildRequires: pkgconfig(libxfconf-0)
Buildrequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(vte-2.91)
BuildRequires: pkgconfig(libxfce4ui-2)
BuildRequires: docbook-dtds
BuildRequires: docbook-style-xsl
BuildRequires: intltool
BuildRequires: time
BuildRequires: xorg-cf-files
BuildRequires: gtk-doc

%description
basko-terminal is a lightweight and easy to use terminal emulator for X
windowing system with Quick commands tabs system

%description -l ru_RU.UTF-8
basko-terminal - легкий и удобный эмулятор терминала для Xfce с системой
быстрых команд.

%prep
%setup

%build
%xfce4reconf
%configure \
	--enable-maintainer-mode \
	--enable-gen-doc \
	--enable-debug=minimum \
	LDFLAGS="%{optflags} -lxfce4util"
%make_build

%install
%make_install
%find_lang %name

%files -f %name.lang
%doc README.md NEWS THANKS
%_bindir/*
%_man1dir/*
%_datadir/basko-terminal
%_datadir/gnome-control-center/default-apps/%name-default-apps.xml
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*

%changelog
* Tue Jul 28 2026 Vsevolod Myalitsin <r4nc@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus.
