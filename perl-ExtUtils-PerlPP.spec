%include	/usr/lib/rpm/macros.perl
Summary:	ExtUtils-PerlPP perl module
Summary(pl):	Modu³ perla ExtUtils-PerlPP
Name:		perl-ExtUtils-PerlPP
Version:	0.03
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/ExtUtils/ExtUtils-PerlPP-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils-PerlPP - A Perl Preprocessor.

%description -l pl
ExtUtils-PerlPP - Preprocesor Perla.

%prep
%setup -q -n ExtUtils-PerlPP-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/ExtUtils/PerlPP
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/ExtUtils/PerlPP.pm
%{perl_sitearch}/auto/ExtUtils/PerlPP

%{_mandir}/man3/*
