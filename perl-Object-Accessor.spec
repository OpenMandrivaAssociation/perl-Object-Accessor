%define upstream_name	 Object-Accessor
%define upstream_version 0.48

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.48
Release:	2
Summary:	Add a Makefile target to determine test coverage using Devel::Cover
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Object/Object-Accessor-0.48.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Params::Check)
BuildArch:	noarch

%description
Object::Accessor provides an interface to create per object accessors (as
opposed to per Class accessors, as, for example, Class::Accessor provides).

You can choose to either subclass this module, and thus using its accessors on
your own module, or to store an Object::Accessor object inside your own object,
and access the accessors from there. See the SYNOPSIS for examples.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Object
%{_mandir}/*/*


%changelog
* Sat May 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.420.0-1mdv2011.0
+ Revision: 674667
- update to new version 0.42

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 0.380.0-4
+ Revision: 640773
- rebuild to obsolete old packages

* Wed Jan 26 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.380.0-3
+ Revision: 633008
- don't rename the man page, the conflict has been fixed

* Mon Jan 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.380.0-2
+ Revision: 631316
- fix man page conflict with perl package

* Sat Jan 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.380.0-1mdv2011.0
+ Revision: 630633
- update to new version 0.38

* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.360.0-1mdv2011.0
+ Revision: 461336
- update to 0.36

* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.340.0-1mdv2010.0
+ Revision: 402000
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.34-2mdv2009.0
+ Revision: 268644
- rebuild early 2009.0 package (before pixel changes)

* Tue May 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.34-1mdv2009.0
+ Revision: 209330
- update to new version 0.34

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 0.32-1mdv2008.0
+ Revision: 22626
- 0.32


* Tue Aug 29 2006 guillomovitch
+ 2006-08-29 10:39:53 (58595)
- new version

* Thu Aug 03 2006 Nicolas Lécureuil <neoclust@mandriva.org>
+ 2006-08-03 15:02:54 (43227)
- import perl-Object-Accessor-0.20-1mdv2007.0

* Fri Jun 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-1mdv2007.0
- New version 0.20

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.12-2mdk
- Buildrequires fix

* Wed Sep 21 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdk
- New release 0.12

* Mon Apr 25 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdk 
- first mandrivalinux release


