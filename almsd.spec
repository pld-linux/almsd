Summary:	A.L.E.C lms daemon
Summary(pl):	A.L.E.C lms daemon
Name:		almsd
Version:	20040117
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://pbern.biz/almsd/%{name}-%{version}.tar.bz2
# Source0-md5:	97132fc33580a4a6da61ece3dc2e8cf9
BuildRequires:	mysql-devel
Requires:	lms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
brak

%description -l pl
Program sluzy do tworzenia plikow konfiguracyjnych roznych uslug 
na podstawie bazy danych LMS`a oraz restartowania odpowiednich serwisow.

%prep
%setup -q

%build
./configure \
    --prefix=%{_bindir} \
    --libdir=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so
