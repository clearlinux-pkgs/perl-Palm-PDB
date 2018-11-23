#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Palm-PDB
Version  : 1.400
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/C/CJ/CJM/Palm-PDB-1.400.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CJ/CJM/Palm-PDB-1.400.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libpalm-pdb-perl/libpalm-pdb-perl_1.400-1.debian.tar.xz
Summary  : 'Parse Palm database files'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Palm-PDB-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Palm-PDB version 1.400, released March 7, 2015
This distribution contains Palm::PDB and Palm::Raw, a pair of Perl 5
modules for reading, manipulating, and writing the .pdb and .prc
database files used by PalmOS devices such as the PalmPilot and its
successors.

%package dev
Summary: dev components for the perl-Palm-PDB package.
Group: Development
Provides: perl-Palm-PDB-devel = %{version}-%{release}

%description dev
dev components for the perl-Palm-PDB package.


%package license
Summary: license components for the perl-Palm-PDB package.
Group: Default

%description license
license components for the perl-Palm-PDB package.


%prep
%setup -q -n Palm-PDB-1.400
cd ..
%setup -q -T -D -n Palm-PDB-1.400 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Palm-PDB-1.400/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Palm-PDB
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Palm-PDB/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/Palm/PDB.pm
/usr/lib/perl5/vendor_perl/5.28.0/Palm/Raw.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Palm::PDB.3
/usr/share/man/man3/Palm::Raw.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Palm-PDB/LICENSE
