Summary:	Changes the rpath or runpath in binaries
Name:		chrpath
Version:	0.13
Release:	13
License:	GPL
Group:		Applications/Editors
#Source0ActiveFtp
Source0:	http://ftp.tux.org/pub/X-Windows/ftp.hungry.com/chrpath/%{name}-%{version}.tar.gz
# Source0-md5:	b73072a8fbba277558c50364b65bb407
Patch0:		%{name}-keepgoing.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_chrpath	1

%description
chrpath changes, lists or removes the rpath or runpath setting in a
binary. The rpath, or runpath if it is present, is where the runtime
linker should look for the libraries needed for a program.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	CC=%{_target_cpu}-freddix-linux-gcc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	doc_DATA=""

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

