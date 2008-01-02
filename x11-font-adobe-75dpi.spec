Name: x11-font-adobe-75dpi
Version: 1.0.0
Release: %mkrel 5
Summary: Xorg X11 font adobe-75dpi
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/font-adobe-75dpi-%{version}.tar.bz2
License: CHECK
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch
BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-75dpi-fonts <= 6.9.0
Requires(post): mkfontdir
Requires(postun): mkfontdir
Requires(post): mkfontscale
Requires(postun): mkfontscale

%description
Xorg X11 font adobe-75dpi

%prep
%setup -q -n font-adobe-75dpi-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir} --with-fontdir=%_datadir/fonts/75dpi

%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%_datadir/fonts/75dpi/fonts.dir
rm -f %{buildroot}%_datadir/fonts/75dpi/fonts.scale

%post
mkfontscale %_datadir/fonts/75dpi
mkfontdir %_datadir/fonts/75dpi

%postun
mkfontscale %_datadir/fonts/75dpi
mkfontdir %_datadir/fonts/75dpi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%_datadir/fonts/75dpi/cour*
%_datadir/fonts/75dpi/helv*
%_datadir/fonts/75dpi/ncen*
%_datadir/fonts/75dpi/symb*
%_datadir/fonts/75dpi/tim*