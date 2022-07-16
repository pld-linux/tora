#
# Conditional build:
%bcond_with	oracle		# build with oracle support
%bcond_with	instantclient	# build oracle support with oracle-instantclient

Summary:	A graphical toolkit for database developers and administrators
Summary(pl.UTF-8):	Zestaw graficznych narzędzi dla programistów i administratorów baz danych
Name:		tora
Version:	3.2
Release:	1
License:	GPL v2
Group:		Applications/Databases/Interfaces
Source0:	https://github.com/tora-tool/tora/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9a08df5eb9ca8a8c26d05540fc57d103
Patch0:		qscintilla.patch
Patch1:		qt-5.11.0.patch
Patch2:		missing-header.patch
Patch3:		i18n.patch
URL:		https://github.com/tora-tool/tora
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	cppunit-devel
BuildRequires:	loki-devel
%{?with_instantclient:BuildRequires:	oracle-instantclient-devel}
BuildRequires:	pcre-devel
BuildRequires:	postgresql-devel
BuildRequires:	qscintilla2-qt5-devel
BuildRequires:	qt5-build
BuildRequires:	qt5-linguist
BuildRequires:	texinfo
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

%build
mkdir -p build
cd build
%cmake ../ \
%if %{with oracle}
	-DENABLE_ORACLE=ON \
%if %{with instantclient}
	-DORACLE_PATH_INCLUDES=%{_includedir}/oracle/client \
	-DORACLE_PATH_LIB=%{_libdir} \
%endif
%else
	-DENABLE_ORACLE=OFF \
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p src/icons/tora.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
cp -a src/templates $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.xpm
