%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%{!?python_version: %define python_version %(%{__python} -c "import sys ; print sys.version[:3]")}

%define srcname lxml

Name:           python-%{srcname}
Version:        1.0.3
Release:        2%{?dist}
Summary:        ElementTree-like Python bindings for libxml2 and libxslt

Group:          Development/Libraries
License:        BSD
URL:            http://codespeak.net/lxml/
Source0:        http://codespeak.net/lxml/%{srcname}-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-devel libxslt-devel python-setuptools
# Upstream now includes the generated .c file and the Pyrex shipped
# with FC (0.9.3.1) is broken for gcc >= 4.0
#BuildRequires: Pyrex >= 0.9.4
Requires:   python-abi = %{python_version}

%description
lxml provides a Python binding to the libxslt and libxml2 libraries.  It
follows the ElementTree API as much as possible in order to provide a more
Pythonic interface to libxml2 and libxslt than the default bindings.  In
particular, lxml deals with Python Unicode strings rather than encoded UTF-8
and handles memory management automatically, unlike the default bindings.


%prep
%setup -q -n %{srcname}-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --single-version-externally-managed


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.txt LICENSES.txt PKG-INFO CREDITS.txt CHANGES.txt doc/
%{python_sitearch}/lxml-%{version}-py%{python_version}.egg-info/
%dir %{python_sitearch}/lxml
%{python_sitearch}/lxml/*.so
%{python_sitearch}/lxml/*.py
%{python_sitearch}/lxml/*.pyc
%{python_sitearch}/lxml/*.pyo

%changelog
* Sat Sep 16 2006 Shahms E. King <shahms@shahms.com> 1.0.3-2
- Rebuild for FC6

* Thu Aug 17 2006 Shahms E. King <shahms@shahms.com> 1.0.3-1
- Update to new upstream version

* Fri Aug 11 2006 Shahms E. King <shahms@shahms.com> 1.0.2-2
- Include, don't ghost .pyo files per new guidelines

* Fri Jul 07 2006 Shahms E. King <shahms@shahms.com> 1.0.2-1
- Update to new upstream release

* Mon Jun 26 2006 Shahms E. King <shahms@shahms.com> 1.0.1-1
- Update to new upstream release

* Fri Jun 02 2006 Shahms E. King <shahms@shahms.com> 1.0-1
- Update to new upstream 1.0 release

* Wed Apr 26 2006 Shahms E. King <shahms@shahms.com> 0.9.1-3
- Add python-setuptools to BuildRequires
- Use dist tag

* Wed Apr 26 2006 Shahms E. King <shahms@shahms.com> 0.9.1-2
- Fix summary and description

* Tue Apr 18 2006 Shahms E. King <shahms@shahms.com> 0.9.1-1
- update the new upstream version
- remove Pyrex build req

* Tue Dec 13 2005 Shahms E. King <shahms@shahms.com> 0.8-1
- Initial package
