#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	ExtUtils
%define		pnam	PerlPP
Summary:	ExtUtils::PerlPP - a Perl preprocessor
Summary(pl.UTF-8):   ExtUtils::PerlPP - preprocesor Perla
Name:		perl-ExtUtils-PerlPP
Version:	0.03
Release:	8
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	374a4aea0e190061ff4e21b903752ee4
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils::PerlPP module contains a Perl preprocessor.

%description -l pl.UTF-8
Moduł ExtUtils::PerlPP zawiera preprocesor Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/ExtUtils/PerlPP.pm
%{_mandir}/man3/*
