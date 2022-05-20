#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cffsubr
Version  : 0.2.9.post1
Release  : 5
URL      : https://files.pythonhosted.org/packages/b6/a6/81c4ccd71c172a7f863c799433426332b01d3f4d302859313524ebf9230b/cffsubr-0.2.9.post1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b6/a6/81c4ccd71c172a7f863c799433426332b01d3f4d302859313524ebf9230b/cffsubr-0.2.9.post1.tar.gz
Summary  : Standalone CFF subroutinizer based on the AFDKO tx tool
Group    : Development/Tools
License  : Apache-2.0 OFL-1.0 OFL-1.1
Requires: pypi-cffsubr-bin = %{version}-%{release}
Requires: pypi-cffsubr-filemap = %{version}-%{release}
Requires: pypi-cffsubr-lib = %{version}-%{release}
Requires: pypi-cffsubr-license = %{version}-%{release}
Requires: pypi-cffsubr-python = %{version}-%{release}
Requires: pypi-cffsubr-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(booleanoperations)
BuildRequires : pypi(fonttools)
BuildRequires : pypi(lxml)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_git_ls_files)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
# cffsubr

%package bin
Summary: bin components for the pypi-cffsubr package.
Group: Binaries
Requires: pypi-cffsubr-license = %{version}-%{release}
Requires: pypi-cffsubr-filemap = %{version}-%{release}

%description bin
bin components for the pypi-cffsubr package.


%package filemap
Summary: filemap components for the pypi-cffsubr package.
Group: Default

%description filemap
filemap components for the pypi-cffsubr package.


%package lib
Summary: lib components for the pypi-cffsubr package.
Group: Libraries
Requires: pypi-cffsubr-license = %{version}-%{release}
Requires: pypi-cffsubr-filemap = %{version}-%{release}

%description lib
lib components for the pypi-cffsubr package.


%package license
Summary: license components for the pypi-cffsubr package.
Group: Default

%description license
license components for the pypi-cffsubr package.


%package python
Summary: python components for the pypi-cffsubr package.
Group: Default
Requires: pypi-cffsubr-python3 = %{version}-%{release}

%description python
python components for the pypi-cffsubr package.


%package python3
Summary: python3 components for the pypi-cffsubr package.
Group: Default
Requires: pypi-cffsubr-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(cffsubr)
Requires: pypi(fonttools)

%description python3
python3 components for the pypi-cffsubr package.


%prep
%setup -q -n cffsubr-0.2.9.post1
cd %{_builddir}/cffsubr-0.2.9.post1
pushd ..
cp -a cffsubr-0.2.9.post1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653008504
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cffsubr
cp %{_builddir}/cffsubr-0.2.9.post1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cffsubr/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/cffsubr-0.2.9.post1/NOTICE %{buildroot}/usr/share/package-licenses/pypi-cffsubr/db981c462edd1090a0cb2c51861f617502f61963
cp %{_builddir}/cffsubr-0.2.9.post1/external/afdko/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-cffsubr/26af2356af80e35e31c9974c24c603363135492f
cp %{_builddir}/cffsubr-0.2.9.post1/external/afdko/tests/buildmasterotfs_data/input/cff2_vf/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-cffsubr/05004ef61c196719f4fd1a1a582c8f6f4e88ddb1
cp %{_builddir}/cffsubr-0.2.9.post1/external/afdko/tests/comparefamily_data/input/source-code-pro/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-cffsubr/689c1517e0db480765a3c35f13a7d942779d7e5e
cp %{_builddir}/cffsubr-0.2.9.post1/tests/data/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-cffsubr/9fb363e27ccdb08776a6eb3b19965e56c173f4c2
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cffsubr

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-cffsubr

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cffsubr/05004ef61c196719f4fd1a1a582c8f6f4e88ddb1
/usr/share/package-licenses/pypi-cffsubr/26af2356af80e35e31c9974c24c603363135492f
/usr/share/package-licenses/pypi-cffsubr/689c1517e0db480765a3c35f13a7d942779d7e5e
/usr/share/package-licenses/pypi-cffsubr/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/pypi-cffsubr/9fb363e27ccdb08776a6eb3b19965e56c173f4c2
/usr/share/package-licenses/pypi-cffsubr/db981c462edd1090a0cb2c51861f617502f61963

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
