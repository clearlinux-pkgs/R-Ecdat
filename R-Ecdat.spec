#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Ecdat
Version  : 0.3.1
Release  : 19
URL      : https://cran.r-project.org/src/contrib/Ecdat_0.3-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Ecdat_0.3-1.tar.gz
Summary  : Data Sets for Econometrics
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : R-Ecfun
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n Ecdat

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552903845

%install
export SOURCE_DATE_EPOCH=1552903845
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Ecdat
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Ecdat
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Ecdat
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  Ecdat || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Ecdat/DESCRIPTION
/usr/lib64/R/library/Ecdat/INDEX
/usr/lib64/R/library/Ecdat/Meta/Rd.rds
/usr/lib64/R/library/Ecdat/Meta/data.rds
/usr/lib64/R/library/Ecdat/Meta/features.rds
/usr/lib64/R/library/Ecdat/Meta/hsearch.rds
/usr/lib64/R/library/Ecdat/Meta/links.rds
/usr/lib64/R/library/Ecdat/Meta/nsInfo.rds
/usr/lib64/R/library/Ecdat/Meta/package.rds
/usr/lib64/R/library/Ecdat/NAMESPACE
/usr/lib64/R/library/Ecdat/data/Rdata.rdb
/usr/lib64/R/library/Ecdat/data/Rdata.rds
/usr/lib64/R/library/Ecdat/data/Rdata.rdx
/usr/lib64/R/library/Ecdat/data/datalist
/usr/lib64/R/library/Ecdat/demoFiles/2_data.xls
/usr/lib64/R/library/Ecdat/demoFiles/5_data.xls
/usr/lib64/R/library/Ecdat/demoFiles/NIPA6.16A20090820.csv
/usr/lib64/R/library/Ecdat/demoFiles/NIPA6.16B20080817.csv
/usr/lib64/R/library/Ecdat/demoFiles/NIPA6.16C20080817.csv
/usr/lib64/R/library/Ecdat/demoFiles/NIPA6.16D20130130.csv
/usr/lib64/R/library/Ecdat/help/AnIndex
/usr/lib64/R/library/Ecdat/help/Ecdat.rdb
/usr/lib64/R/library/Ecdat/help/Ecdat.rdx
/usr/lib64/R/library/Ecdat/help/aliases.rds
/usr/lib64/R/library/Ecdat/help/paths.rds
/usr/lib64/R/library/Ecdat/html/00Index.html
/usr/lib64/R/library/Ecdat/html/R.css
/usr/lib64/R/library/Ecdat/scripts/F1.PikettySaez.R
