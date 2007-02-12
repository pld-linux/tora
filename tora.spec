#
# Conditional build:
%bcond_with	oracle		# build with oracle support
#
Summary:	A graphical toolkit for database developers and administrators
Summary(pl.UTF-8):   Zestaw graficznych narzędzi dla programistów i administratorów baz danych
Name:		tora
Version:	1.3.21
Release:	0.4
License:	GPL v2
Group:		Applications/Databases/Interfaces
Source0:	http://dl.sourceforge.net/tora/%{name}-%{version}.tar.gz
# Source0-md5:	10e3c9944ffaca50de046e2c3e02eee4
Source1:	%{name}.desktop
Patch0:		%{name}-no-maximize.patch
Patch1:		%{name}-cpp.patch
URL:		http://tora.sourceforge.net/
BuildRequires:	kdelibs-devel
BuildRequires:	pcre-devel
BuildRequires:	qscintilla-devel
BuildRequires:	qt-devel
BuildRequires:	qt-linguist
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TOra features a schema browser, SQL worksheet, PL/SQL editor and
debugger, storage manager, rollback segment monitor, instance manager,
and SQL output viewer. Via qt3 it can access PostgreSQL and MySQL
directly. Any other database systems can be accessed via ODBC.

%description -l pl.UTF-8
TOra zawiera przeglądarkę schematów, arkusz roboczy SQL, edytor i
debugger PL/SQL, zarządcę danych, monitor segmentów wycofań, zarządcę
instancji i przeglądarkę wyjścia SQL. Poprzez qt3 może współpracować
bezpośrednio z bazami PostgreSQL i MySQL. Inne systemy baz danych mogą
być obsługiwane poprzez ODBC.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--libdir=%{_libdir}/%{name} \
	--enable-plugin \
	%{?with_oracle:--with-oracle}%{!?with_oracle:--without-oracle}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install icons/tora.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

cp -a help $RPM_BUILD_ROOT%{_libdir}/%{name}
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/help/images/{.xvpics,.cvsignore}

install *.qm $RPM_BUILD_ROOT%{_libdir}/%{name}
install templates/*.tpl $RPM_BUILD_ROOT%{_libdir}/%{name}

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
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
