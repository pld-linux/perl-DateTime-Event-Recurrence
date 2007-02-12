#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DateTime
%define	pnam	Event-Recurrence
Summary:	DateTime::Event::Recurrence - DateTime::Set extension for create basic recurrence sets
Summary(pl.UTF-8):	DateTime::Event::Recurrence - rozszerzenie DateTime::Set o tworzenie prostych zbiorów rekurencyjnych
Name:		perl-DateTime-Event-Recurrence
Version:	0.16
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/F/FG/FGLOCK/DateTime-Event-Recurrence-%{version}.tar.gz
# Source0-md5:	9a08830b081a93619f4a8564063e3bf0
URL:		http://search.cpan.org/dist/DateTime-Event-Recurrence/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DateTime >= 1:0.27
BuildRequires:	perl-DateTime-Set >= 0.17
%endif
Requires:	perl-DateTime >= 1:0.34-1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides convenience methods that let you easily create
DateTime::Set objects for various recurrences, such as "once a month"
or "every day". You can also create more complicated recurrences, such
as "every Monday, Wednesday and Thursday at 10:00 AM and 2:00 PM".

%description -l pl.UTF-8
Ten moduł dostarcza wygodne metody pozwalające łatwo tworzyć obiekty
DateTime::Set dla różnych rekurencji, takich jak "raz w miesiącu" czy
"codziennie". Można także tworzyć bardziej złożone rekurencje, takie
jak "każdy poniedziałek, środa i czwartek od 10:00 do 14:00".

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
%doc Changes CREDITS README TODO
%{perl_vendorlib}/DateTime/Event/*.pm
%{_mandir}/man3/*
