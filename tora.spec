Summary:	GUI for managing SQL databases
Summary(pl):	GUI do zarz±dzania SQLowymi bazami danych
Name:		tora
Version:	1.3.14
Release:	1
License:	GPL
Group:		Utilities
Source0:	http://dl.sourceforge.net/tora/tora-alpha-%{version}.tar.gz	
# Source0-md5:	0e7ed1ca994a7e61a7b7962138eaeb55
Source1:	%{name}.desktop
URL:		http://www.globecom.se/tora/
BuildRequires:	kdelibs-devel
BuildRequires:	qt-devel
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
	--with-kde-include=/usr/include \
	--with-kde-libs=/usr/lib \
	--with-qt-include=/usr/include/qt \
	--with-qt-libs=/usr/lib \
	--with-qt-moc=/usr/bin/moc \
	--with-qt-uic=/usr/bin/uic \
	--without-oracle
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities

%{__make} install ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README BUGS NEWS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_applnkdir}/Utilities/*
