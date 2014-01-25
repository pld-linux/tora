#
# Conditional build:
%bcond_with	oracle		# build with oracle support
%bcond_with	instantclient	# build oracle support with oracle-instantclient
#
Summary:	A graphical toolkit for database developers and administrators
Summary(pl.UTF-8):	Zestaw graficznych narzędzi dla programistów i administratorów baz danych
Name:		tora
Version:	2.1.3
Release:	5
License:	GPL v2
Group:		Applications/Databases/Interfaces
Source0:	http://downloads.sourceforge.net/tora/%{name}-%{version}.tar.gz
# Source0-md5:	ea4a75a9daeaf58492413e3f7fe40293
Source1:	%{name}.desktop
Patch0:		%{name}-postgresql.patch
Patch1:		%{name}-gcc.patch
Patch2:		%{name}-build.patch
Patch3:		gethostname.patch
URL:		http://tora.sourceforge.net/
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtSql-devel
BuildRequires:	QtXml-devel
BuildRequires:	cppunit-devel
%{?with_instantclient:BuildRequires:	oracle-instantclient-devel}
BuildRequires:	pcre-devel
BuildRequires:	postgresql-devel
BuildRequires:	qscintilla2-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-linguist
BuildRequires:	xorg-lib-libICE-devel
Suggests:	QtSql-pgsql
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
%patch1 -p1
%patch2 -p1
%patch3 -p1

rm -f src/moc_*

%build
%{__libtoolize}
%{__aclocal} -I config/m4
%{__autoconf}
%{__automake}
%configure \
	--libdir=%{_datadir}/%{name} \
	--with-qt-libraries=%{_libdir} \
%if %{with oracle}
    %if %{with instantclient}
	--with-instant-client \
	--with-oracle-includes=%{_includedir}/oracle/client \
	--with-oracle-libraries=%{_libdir} \
    %endif
	--with-oracle
%else
	--without-oracle
%endif

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
