Summary:	GUI for managing SQL databases
Summary(pl):	GUI do zarz±dzania SQLowymi bazami danych
Name:		tora
Version:	1.3.8
Release:	1
License:	GPL
Group:		Utilities
Source0:	http://prdownloads.sourceforge.net/tora/tora-alpha-1.3.8.tar.gz
Source1:	%{name}.desktop
URL:		http://www.globecom.se/tora/
BuildRequires:	qt-devel
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
	--with-kde-include=/usr/X11R6/include \
	--with-kde-libs=/usr/X11R6/lib \
	--with-qt-include=/usr/X11R6/include/qt \
	--with-qt-libs=/usr/X11R6/lib \
	--with-qt-moc=/usr/X11R6/bin/moc \
	--with-qt-uic=/usr/X11R6/bin/uic \
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
