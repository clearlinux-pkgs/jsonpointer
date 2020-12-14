#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jsonpointer
Version  : 2.0
Release  : 43
URL      : https://files.pythonhosted.org/packages/52/e7/246d9ef2366d430f0ce7bdc494ea2df8b49d7a2a41ba51f5655f68cfe85f/jsonpointer-2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/52/e7/246d9ef2366d430f0ce7bdc494ea2df8b49d7a2a41ba51f5655f68cfe85f/jsonpointer-2.0.tar.gz
Summary  : Identify specific nodes in a JSON document (RFC 6901)
Group    : Development/Tools
License  : BSD-3-Clause
Requires: jsonpointer-bin = %{version}-%{release}
Requires: jsonpointer-license = %{version}-%{release}
Requires: jsonpointer-python = %{version}-%{release}
Requires: jsonpointer-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
===================
        
        |PyPI version| |Supported Python versions| |Build Status| |Coverage
        Status|
        
        Resolve JSON Pointers in Python
        -------------------------------
        
        Library to resolve JSON Pointers according to `RFC

%package bin
Summary: bin components for the jsonpointer package.
Group: Binaries
Requires: jsonpointer-license = %{version}-%{release}

%description bin
bin components for the jsonpointer package.


%package license
Summary: license components for the jsonpointer package.
Group: Default

%description license
license components for the jsonpointer package.


%package python
Summary: python components for the jsonpointer package.
Group: Default
Requires: jsonpointer-python3 = %{version}-%{release}

%description python
python components for the jsonpointer package.


%package python3
Summary: python3 components for the jsonpointer package.
Group: Default
Requires: python3-core
Provides: pypi(jsonpointer)

%description python3
python3 components for the jsonpointer package.


%prep
%setup -q -n jsonpointer-2.0
cd %{_builddir}/jsonpointer-2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603394351
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python tests.py
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jsonpointer
cp %{_builddir}/jsonpointer-2.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/jsonpointer/0305317c0f694ba11e8f059938fd0c880356e7bc
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jsonpointer

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jsonpointer/0305317c0f694ba11e8f059938fd0c880356e7bc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
