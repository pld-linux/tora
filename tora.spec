#
# Conditional build:
%bcond_with	oracle		# build with oracle support
Summary:	A graphical toolkit for database developers and administrators
Summary(pl):	Zestaf graficznych narzêdzi dla programistów i administratorów baz danych
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
BuildRequires:	docbook-xml >= 4.2
BuildRequires:	xsltproc
BuildRequires:	docbook-xsl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tora features a schema browser, SQL worksheet, PL/SQL editor
and debugger, storage manager, rollback segment monitor,
instance manager, and SQL output viewer.
Via qt3 it can access PostgreSQL and MySQL directly.
Any other database systems can be accessed via ODBC.                                               

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
