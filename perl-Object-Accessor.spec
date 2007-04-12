%define module	Object-Accessor
%define name	perl-%{module}
%define version 0.21
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Add a Makefile target to determine test coverage using Devel::Cover
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:		http://www.cpan.org/modules/by-module/Object/%{module}-%{version}.tar.bz2
BuildArch:	noarch
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires:  perl(Params::Check)
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Object::Accessor provides an interface to create per object accessors (as
opposed to per Class accessors, as, for example, Class::Accessor provides).

You can choose to either subclass this module, and thus using its accessors on
your own module, or to store an Object::Accessor object inside your own object,
and access the accessors from there. See the SYNOPSIS for examples.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Object
%{_mandir}/*/*


