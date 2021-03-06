Summary:	Intelligent schema migrations for Django apps
Name:		python-django-south
Version:	0.7.6
Release:	2
License:	ASL 2.0
Group:		Development/Languages
URL:		http://south.aeracode.org
Source0:	http://www.aeracode.org/releases/south/south-%{version}.tar.gz
# Source0-md5:	6089871449006d45d06c409b42d8bd44
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-django
Obsoletes:	Django-south
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
South brings migrations to Django applications. Its main objectives
are to provide a simple, stable and database-independent migration
layer to prevent all the hassle schema changes over time bring to your
Django applications.

%prep
%setup -q -n South-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/south/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/south
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/South-*.egg-info
%endif
