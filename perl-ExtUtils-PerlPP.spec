%include	/usr/lib/rpm/macros.perl
%define	pdir	ExtUtils
%define	pnam	PerlPP
Summary:	ExtUtils::PerlPP perl module
Summary(pl):	Modu³ perla ExtUtils::PerlPP
Name:		perl-ExtUtils-PerlPP
Version:	0.03
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	374a4aea0e190061ff4e21b903752ee4
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils::PerlPP - A Perl Preprocessor.

%description -l pl
ExtUtils::PerlPP - Preprocesor Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/ExtUtils/PerlPP.pm
%{_mandir}/man3/*
