Summary:	A.L.E.C lms daemon
Summary(pl.UTF-8):   Demon A.L.E.C lms
Name:		almsd
Version:	20040309
Release:	2
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://pbern.biz/almsd/snap/%{name}-%{version}.tar.bz2
# Source0-md5:	fdb66515e67ca258dba002ea0fb960b8
BuildRequires:	libgadu-devel
BuildRequires:	mysql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility for creating of several services configuration files basing on
LMS database and restarting appropriate services.

%description -l pl.UTF-8
Program służy do tworzenia plików konfiguracyjnych różnych usług na
podstawie bazy danych LMS-a oraz restartowania odpowiednich usług.

%package ethers
Summary:	A.L.E.C lms daemon - ethers module
Summary(pl.UTF-8):   Demon A.L.E.C lms daemon - moduł ethers
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}

%description ethers
ethers module for A.L.E.C lms daemon.

%description ethers -l pl.UTF-8
Moduł ethers dla demona A.L.E.C lms.

%package hostfile
Summary:	A.L.E.C lms daemon - hostfile module
Summary(pl.UTF-8):   Demon A.L.E.C lms - moduł hostfile
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}

%description hostfile 
hostfile module for A.L.E.C lms daemon.

%description hostfile -l pl.UTF-8
Moduł hostfile dla demona A.L.E.C lms.

%package dhcp
Summary:	A.L.E.C lms daemon - dhcp module
Summary(pl.UTF-8):   Demon A.L.E.C lms - moduł dhcp
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}

%description dhcp
dhcp module for A.L.E.C lms daemon.

%description dhcp -l pl.UTF-8
Moduł dhcp dla demona A.L.E.C lms.

%package oident
Summary:	A.L.E.C lms daemon - oident module
Summary(pl.UTF-8):   Demon A.L.E.C lms - moduł oident
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}

%description oident
oident module for A.L.E.C lms daemon.

%description oident -l pl.UTF-8
Moduł oident dla demona A.L.E.C lms.

%package dns
Summary:	A.L.E.C lms daemon - dns module
Summary(pl.UTF-8):   Demon A.L.E.C lms - moduł dns
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}

%description dns
dns module for A.L.E.C lms daemon.

%description dns -l pl.UTF-8
Moduł dns dla demona A.L.E.C lms.

%package cutoff
Summary:	A.L.E.C lms daemon - cutoff module
Summary(pl.UTF-8):   Demon A.L.E.C lms - moduł cutoff
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}

%description cutoff
cutoff module for A.L.E.C lms daemon.

%description cutoff -l pl.UTF-8
Moduł cutoff dla demona A.L.E.C lms.

%package payments
Summary:	A.L.E.C lms daemon - payments module
Summary(pl.UTF-8):   Demon A.L.E.C lms - moduł payments
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}

%description payments
payments module for A.L.E.C lms daemon.

%description payments -l pl.UTF-8
Moduł płatności (payments) dla demona A.L.E.C lms.

%package traffic
Summary:	A.L.E.C lms daemon - traffic module
Summary(pl.UTF-8):   Demon A.L.E.C lms - moduł traffic
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}

%description traffic
traffic module for A.L.E.C lms daemon.

%description traffic -l pl.UTF-8
Moduł traffic dla demona A.L.E.C lms.

%package notify
Summary:	A.L.E.C lms daemon - notify module
Summary(pl.UTF-8):   Demon A.L.E.C lms - moduł notify
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}

%description notify
notify module for A.L.E.C lms daemon.

%description notify -l pl.UTF-8
Moduł powiadamiania (notify) dla demona A.L.E.C lms.

%package tc
Summary:	A.L.E.C lms daemon - tc module
Summary(pl.UTF-8):   Demon A.L.E.C lms - moduł tc
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}

%description tc
tc module for A.L.E.C lms daemon.

%description tc -l pl.UTF-8
Moduł tc dla demona A.L.E.C lms.

%package ggnotify
Summary:	A.L.E.C lms daemon - ggnotify module
Summary(pl.UTF-8):   Demon A.L.E.C lms - moduł ggnotify
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}

%description ggnotify
ggnotify module for A.L.E.C lms daemon.

%description ggnotify -l pl.UTF-8
Moduł ggnotify dla demona A.L.E.C lms.

%prep
%setup -q

%build
./configure \
	--prefix=%{_bindir} \
	--libdir=%{_libdir}

%{__make} \
	CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

%{__make} install \
	INSTALLDIR=$RPM_BUILD_ROOT%{_bindir} 

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
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ethers.so

%files hostfile
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/hostfile.so

%files dhcp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/dhcp.so

%files oident
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/oident.so

%files dns
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/dns.so

%files cutoff
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cutoff.so

%files payments
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/payments.so

%files traffic
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/traffic.so

%files notify
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/notify.so

%files tc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/tc.so

%files ggnotify
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ggnotify.so
