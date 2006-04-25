# Conditional build:
%bcond_with	oracle		# build with oracle support
Summary:	GUI for managing SQL databases
Summary(pl):	GUI do zarz±dzania SQLowymi bazami danych
Name:		tora
Version:	1.3.21
Release:	0.1
License:	GPL v2
Group:		Applications/Databases/Interfaces
Source0:	http://dl.sourceforge.net/tora/%{name}-%{version}.tar.gz
# Source0-md5:	10e3c9944ffaca50de046e2c3e02eee4
Source1:	%{name}.desktop
Patch0:		%{name}-LDFLAGS.patch
URL:		http://www.globecom.se/tora/
BuildRequires:	kdelibs-devel
BuildRequires:	qt-devel
BuildRequires:	qt-linguist
BuildRequires:	mono-devel
BuildRequires:	qscintilla-devel
BuildRequires:	pcre-devel
BuildRequires:	cppunit-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GUI for managing SQL databases.

%description -l pl
GUI do zarz±dzania SQLowymi bazami danych.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cp -f /usr/share/automake/config.sub .
%configure \
	%{?with_oracle:--with-oracle}%{?without_oracle:--without-oracle}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install icons/tora.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_libdir}/lib*.so.*.*.*
%{_desktopdir}/*
%{_pixmapsdir}/*
