Summary:	TPSA connections configurator
Summary(pl):	Konfigurator po��cze� TPSA
Name:		netcfg-tpsa
Version:	0.99
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://ep09.pld-linux.org/~havner/tpsa-%{version}.tar.bz2
# Source0-md5:	37ef5e8d37371e82a82629da4958a31d
Requires:	perl-Paw
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TPSA connections configurator.

%description -l pl
Konfigurator po��cze� TPSA.

%prep
%setup -q -n tpsa

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_desktopdir}}

install netcfg-tpsa.pl $RPM_BUILD_ROOT%{_sbindir}
install netcfg-tpsa.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_desktopdir}/*
