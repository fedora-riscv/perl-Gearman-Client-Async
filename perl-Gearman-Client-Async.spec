Name:           perl-Gearman-Client-Async
Version:        0.94
Release:        7%{?dist}
Summary:        Asynchronous Client for the Gearman distributed job system
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Gearman-Client-Async/
Source0:        http://www.cpan.org/authors/id/B/BR/BRADFITZ/Gearman-Client-Async-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Gearman::Server)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Asynchronous Client for the Gearman distributed job system

%prep
%setup -q -n Gearman-Client-Async-%{version}

# Filter double Requires:
cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
  sed -e '/^perl(Danga::Socket)$/d'
EOF

%define __perl_requires %{_builddir}/Gearman-Client-Async-%{version}/%{name}-req
chmod +x %{__perl_requires}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

mv README.txt README

%check
# this test fails to run on x86_64 (#246356)
rm t/err8.t
make test

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGES README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.94-7
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 07 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.94-4
- rebuild for new perl

* Mon Jun 09 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.94-3
- Disable test which fails on x86_64 (#246356)
* Mon Jun 02 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.94-2
- Enabled tests
- Added necessary BuilRequires for F-8
* Sun May 20 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.94-1
- Specfile autogenerated by cpanspec 1.69.1.
