Summary:	GUI for managing SQL databases
Summary(pl):	GUI do zarz±dzania SQLowymi bazami danych
Name:		tora
Version:	1.3.14.1
Release:	0.3
License:	GPL v2
Group:		Applications/Databases/Interfaces
Source0:	http://dl.sourceforge.net/tora/%{name}-alpha-%{version}.tar.gz	
# Source0-md5:	5560b5104438e1b71bd89386d0fcdc00
Source1:	%{name}.desktop
URL:		http://www.globecom.se/tora/
BuildRequires:	kdelibs-devel
BuildRequires:	qt-devel
BuildRequires:	qt-linguist
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GUI for managing SQL databases.

%description -l pl
GUI do zarz±dzania SQLowymi bazami danych.

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix} \
	--prefix-lib=%{_datadir} \
	--with-kde-include=%{_includedir} \
	--with-kde-libs=%{_libdir} \
	--with-qt-include=%{_includedir}/qt \
	--with-qt-libs=%{_libdir} \
	--with-qt-moc=%{_bindir}/moc \
	--with-qt-uic=%{_bindir}/uic \
	--without-oracle \
	--with-gcc="%{__cc}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	ROOT=$RPM_BUILD_ROOT
	
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install icons/tora.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
