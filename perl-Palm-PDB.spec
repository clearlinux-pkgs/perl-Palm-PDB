#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Palm-PDB
Version  : 1.400
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/C/CJ/CJM/Palm-PDB-1.400.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CJ/CJM/Palm-PDB-1.400.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libpalm-pdb-perl/libpalm-pdb-perl_1.400-1.debian.tar.xz
Summary  : 'Parse Palm database files'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Palm-PDB-license
Requires: perl-Palm-PDB-man

%description
Palm-PDB version 1.400, released March 7, 2015
This distribution contains Palm::PDB and Palm::Raw, a pair of Perl 5
modules for reading, manipulating, and writing the .pdb and .prc
database files used by PalmOS devices such as the PalmPilot and its
successors.

%package license
Summary: license components for the perl-Palm-PDB package.
Group: Default

%description license
license components for the perl-Palm-PDB package.


%package man
Summary: man components for the perl-Palm-PDB package.
Group: Default

%description man
man components for the perl-Palm-PDB package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n Palm-PDB-1.400
mkdir -p %{_topdir}/BUILD/Palm-PDB-1.400/deblicense/
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
mkdir -p %{buildroot}/usr/share/doc/perl-Palm-PDB
cp LICENSE %{buildroot}/usr/share/doc/perl-Palm-PDB/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Palm/PDB.pm
/usr/lib/perl5/site_perl/5.26.1/Palm/Raw.pm

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-Palm-PDB/LICENSE

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Palm::PDB.3
/usr/share/man/man3/Palm::Raw.3
