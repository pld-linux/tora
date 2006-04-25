#
# Conditional build:
%bcond_with	oracle		# build with oracle support
Summary:	A graphical toolkit for database developers and administrators
Summary(pl):	Zestaf graficznych narzêdzi dla programistów i administratorów baz danych
Name:		tora
Version:	1.3.21
Release:	0.2
License:	GPL v2
Group:		Applications/Databases/Interfaces
Source0:	http://dl.sourceforge.net/tora/%{name}-%{version}.tar.gz
# Source0-md5:	10e3c9944ffaca50de046e2c3e02eee4
Source1:	%{name}.desktop
URL:		http://tora.sourceforge.net/
BuildRequires:	kdelibs-devel
BuildRequires:	qt-devel
BuildRequires:	qt-linguist
BuildRequires:	qscintilla-devel
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TOra features a schema browser, SQL worksheet, PL/SQL editor
and debugger, storage manager, rollback segment monitor,
instance manager, and SQL output viewer.
Via qt3 it can access PostgreSQL and MySQL directly.
Any other database systems can be accessed via ODBC.                                               

%prep
%setup -q

%build
%configure \
	--libdir=%{_libdir}/%{name} \
	--enable-plugin \
	%{?with_oracle:--with-oracle}%{?without_oracle:--without-oracle}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/help/{images,api}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install icons/tora.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

install help/*.html $RPM_BUILD_ROOT%{_libdir}/%{name}/help/
install help/images/*.png $RPM_BUILD_ROOT%{_libdir}/%{name}/help/images/
install help/api/*.html $RPM_BUILD_ROOT%{_libdir}/%{name}/help/api/

install *.qm $RPM_BUILD_ROOT%{_libdir}/%{name}/
install templates/*.tpl $RPM_BUILD_ROOT%{_libdir}/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/lib*.so
%{_libdir}/%{name}/lib*.la
# Needed?
%{_libdir}/%{name}/lib*.a
%{_libdir}/%{name}/help
%{_libdir}/%{name}/*.tpl
%{_libdir}/%{name}/*.qm
%{_desktopdir}/*
%{_pixmapsdir}/*
