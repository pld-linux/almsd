Summary:	A.L.E.C lms daemon
Summary(pl):	A.L.E.C lms daemon
Name:		almsd
Version:	20040117
Release:	0.3
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://pbern.biz/almsd/snap/%{name}-%{version}.tar.bz2
# Source0-md5:	97132fc33580a4a6da61ece3dc2e8cf9
BuildRequires:	libgadu-devel
BuildRequires:	mysql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
none

%description -l pl
Program s³u¿y do tworzenia plikow konfiguracyjnych ró¿nych us³ug 
na podstawie bazy danych LMS`a oraz restartowania odpowiednich serwisow.

%package ethers
Summary:        A.L.E.C lms daemon module ethers
Summary(pl):    A.L.E.C lms daemon modu³ ethers
Group:          Networking/Utilities
Requires:	%{name} = %{version}
%description ethers
none
%description ethers -l pl
brak 

%package hostfile
Summary:        A.L.E.C lms daemon module hostfile
Summary(pl):    A.L.E.C lms daemon modu³ hostfile
Group:          Networking/Utilities
Requires:	%{name} = %{version}
%description hostfile 
none
%description hostfile -l pl
brak 

%package dhcp
Summary:        A.L.E.C lms daemon module dhcp
Summary(pl):    A.L.E.C lms daemon modu³ dhcp
Group:          Networking/Utilities
Requires:	%{name} = %{version}
%description dhcp
none
%description dhcp -l pl
brak 

%package oident
Summary:        A.L.E.C lms daemon module oident
Summary(pl):    A.L.E.C lms daemon modu³ oident
Group:          Networking/Utilities
Requires:	%{name} = %{version}
%description oident
none
%description oident -l pl
brak 

%package dns
Summary:        A.L.E.C lms daemon module dns
Summary(pl):    A.L.E.C lms daemon modu³ dns
Group:          Networking/Utilities
Requires:	%{name} = %{version}
%description dns
none
%description dns -l pl
brak 

%package cutoff
Summary:        A.L.E.C lms daemon module cutoff
Summary(pl):    A.L.E.C lms daemon modu³ cutoff
Group:          Networking/Utilities
Requires:	%{name} = %{version}
%description cutoff
none
%description cutoff -l pl
brak 

%package payments
Summary:        A.L.E.C lms daemon module payments
Summary(pl):    A.L.E.C lms daemon modu³ payments
Group:          Networking/Utilities
Requires:	%{name} = %{version}
%description payments
none
%description payments -l pl
brak 

%package traffic
Summary:        A.L.E.C lms daemon module traffic
Summary(pl):    A.L.E.C lms daemon modu³ traffic
Group:          Networking/Utilities
Requires:	%{name} = %{version}
%description traffic
none
%description traffic -l pl
brak 

%package notify
Summary:        A.L.E.C lms daemon module notify
Summary(pl):    A.L.E.C lms daemon modu³ notify
Group:          Networking/Utilities
Requires:	%{name} = %{version}
%description notify
none
%description notify -l pl
brak 

%package tc
Summary:        A.L.E.C lms daemon module tc
Summary(pl):    A.L.E.C lms daemon modu³ tc
Group:          Networking/Utilities
Requires:	%{name} = %{version}
%description tc
none
%description tc -l pl
brak 

%package ggnotify
Summary:        A.L.E.C lms daemon module ggnotify
Summary(pl):    A.L.E.C lms daemon modu³ ggnotify
Group:          Networking/Utilities
Requires:	%{name} = %{version}
%description ggnotify
none
%description ggnotify -l pl
brak 

%prep
%setup -q

%build
./configure \
    --prefix=%{_bindir}  \
    --libdir=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
       INSTALLDIR=$RPM_BUILD_ROOT%{_bindir} 

install -d  $RPM_BUILD_ROOT%{_libdir}

for i in ethers hostfile dhcp oident dns cutoff payments traffic notify tc ggnotify; do
    install modules/$i/*.so $RPM_BUILD_ROOT%{_libdir}
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO lms.ini.sample
%attr(755,root,root) %{_bindir}/*

%files ethers
%attr(755,root,root) %{_libdir}/ethers.so

%files hostfile
%attr(755,root,root) %{_libdir}/hostfile.so

%files dhcp
%attr(755,root,root) %{_libdir}/dhcp.so

%files oident
%attr(755,root,root) %{_libdir}/oident.so

%files dns
%attr(755,root,root) %{_libdir}/dns.so

%files cutoff
%attr(755,root,root) %{_libdir}/cutoff.so

%files payments
%attr(755,root,root) %{_libdir}/payments.so

%files traffic
%attr(755,root,root) %{_libdir}/traffic.so

%files notify
%attr(755,root,root) %{_libdir}/notify.so

%files tc
%attr(755,root,root) %{_libdir}/tc.so

%files ggnotify
%attr(755,root,root) %{_libdir}/ggnotify.so
