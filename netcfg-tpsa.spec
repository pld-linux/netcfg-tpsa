Summary:	TPSA connections configurator
Summary(pl):	Konfigurator po³±czeñ TPSA
Name:		netcfg-tpsa
Version:	1.0
Release:	0.1
License:	GPL
Group:		-
Source0:	http://ep09.pld-linux.org/~havner/livecd-%{version}.tar.bz2
# Source0-md5:	f0bc5023d278c3c39dcdbca9e9539c78
Requires:	perl-Paw
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TPSA connections configurator.

%description -l pl
Konfigurator po³±czeñ TPSA

%prep
%setup -q -n livecd

%build

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT%{_sbindir}
install tpsa/netcfg-tpsa.pl $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
