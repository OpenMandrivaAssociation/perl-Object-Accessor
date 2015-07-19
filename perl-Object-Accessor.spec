%define upstream_name	 Object-Accessor
%define upstream_version 0.48

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.48
Release:	6
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
