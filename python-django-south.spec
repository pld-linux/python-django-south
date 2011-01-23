Summary:	Intelligent schema migrations for Django apps
Name:		python-django-south
Version:	0.7.2
Release:	1
License:	ASL 2.0
Group:		Development/Languages
URL:		http://south.aeracode.org
Source0:	http://www.aeracode.org/releases/south/south-%{version}.tar.gz
# Source0-md5:	4c6b60b38a9464509f2671ae540e1446
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
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
%setup -q -n south

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/south/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%{py_sitescriptdir}/south
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/South-*.egg-info
%endif
