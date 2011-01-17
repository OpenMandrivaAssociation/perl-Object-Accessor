%define upstream_name	 Object-Accessor
%define upstream_version 0.38

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2
Summary:	Add a Makefile target to determine test coverage using Devel::Cover
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Object/%{upstream_name}-%{upstream_version}.tar.gz
Buildrequires:  perl(Params::Check)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Object::Accessor provides an interface to create per object accessors (as
opposed to per Class accessors, as, for example, Class::Accessor provides).

You can choose to either subclass this module, and thus using its accessors on
your own module, or to store an Object::Accessor object inside your own object,
and access the accessors from there. See the SYNOPSIS for examples.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

# fix conflict with  perl package
mv %{buildroot}%{_mandir}/man3/Object::Accessor.3pm \
    %{buildroot}%{_mandir}/man3/Object::Accessor.standalone.3pm

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Object
%{_mandir}/*/*
