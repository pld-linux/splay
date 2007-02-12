Summary:	MPEG-1,2 Audio layer 1,2,3 file player
Summary(pl.UTF-8):   Odtwarzacz plików dźwiękowych MPEG-1,2 warstw 1,2,3
Name:		splay
Version:	0.9.5.2
Release:	1
License:	LGPL (library), GPL (application)
Group:		Applications/Sound
Source0:	http://splay.sourceforge.net/tgz/%{name}-%{version}.tar.gz
# Source0-md5:	91cf15bdf0d0c4eb94306c3a8d8b94cc
Patch0:		%{name}-fix.patch
Patch1:		%{name}-qt3.patch
Patch2:		%{name}-id3lib.patch
URL:		http://splay.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	id3lib-devel >= 3.8.2-2
BuildRequires:	libstdc++-devel
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MPEG-1,2 Audio layer 1,2,3 file player.

%description -l pl.UTF-8
Odtwarzacz plików dźwiękowych MPEG-1,2 warstw 1,2,3.

%package xsplay
Summary:	Qt-based X interface for splay
Summary(pl.UTF-8):   Oparty o Qt interfejs pod X do programu splay
Group:		X11/Applications/Sound
# only because xsplay(1) manual is just reference to splay(1)
Requires:	%{name} = %{version}-%{release}

%description xsplay
Qt-based X interface for splay.

%description xsplay -l pl.UTF-8
Oparty o Qt interfejs pod X do programu splay.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

# MOC files for old qt - need regeneration
rm -f apps/moc_*.cc

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README README.LIB
%attr(755,root,root) %{_bindir}/splay
%{_mandir}/man1/splay.1*

%files xsplay
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xsplay
%{_mandir}/man1/xsplay.1*
