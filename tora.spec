#
# Conditional build:
%bcond_with	oracle		# build with oracle support
#
Summary:	A graphical toolkit for database developers and administrators
Summary(pl.UTF-8):	Zestaw graficznych narzędzi dla programistów i administratorów baz danych
Name:		tora
Version:	2.1.1
Release:	0.1
License:	GPL v2
Group:		Applications/Databases/Interfaces
Source0:	http://dl.sourceforge.net/tora/%{name}-%{version}.tar.gz
# Source0-md5:	6a25c8f62a70f368f16126103d54be7d
Source1:	%{name}.desktop
Patch0:		%{name}-postgresql.patch
URL:		http://tora.sourceforge.net/
BuildRequires:	pcre-devel
BuildRequires:	postgresql-devel
BuildRequires:	qscintilla2-devel
BuildRequires:	qt-devel >= 4.3.0
BuildRequires:	qt-linguist
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{with oracle}
# ORACLE_HOME is required for oracle
%define _preserve_env %_preserve_env_base ORACLE_HOME
%endif

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

rm -f src/moc_*

%build
%{__libtoolize}
%{__aclocal} -I config/m4
%{__autoconf}
%{__automake}
%configure \
	--libdir=%{_datadir}/%{name} \
	%{!?with_oracle:--without-oracle}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install src/icons/tora.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
cp -a src/templates $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/help
%{_datadir}/%{name}/templates
%{_datadir}/%{name}/*.qm
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_infodir}/tora*
