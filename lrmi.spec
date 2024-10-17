%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Library for calling real mode BIOS routines under Linux
Name:		lrmi
Version:	0.10
Release:	26
License:	MIT
Group:		System/Libraries
Url:		https://sourceforge.net/projects/lrmi/
Source0:	http://prdownloads.sourceforge.net/lrmi/%{name}-%{version}.tar.bz2
Patch0:		lrmi-0.10-makefile.patch
Patch1:		lrmi-no_strip.diff
Patch2:		lrmi-build_fix.diff
Patch3:		lrmi-shared_vbetest_fix.diff
ExclusiveArch:	%ix86

%description
LRMI is a library for calling real mode BIOS routines under Linux.

%package -n	%{libname}
Summary:	Library for calling real mode BIOS routines under Linux
Group:		System/Libraries

%description -n	%{libname}
LRMI is a library for calling real mode BIOS routines under Linux.

%package -n	%{devname}
Summary:	Library for calling real mode BIOS routines under Linux
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	liblrmi-devel = %{version}-%{release}

%description -n	%{devname}
LRMI is a library for calling real mode BIOS routines under Linux.

%package	tools
Summary:	Library for calling real mode BIOS routines under Linux
Group:		System/Configuration/Hardware

%description	tools
LRMI is a library for calling real mode BIOS routines under Linux.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p0
%patch3 -p0

%build
make CFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}%{_libdir} %{buildroot}%{_includedir}

%makeinstall LIBDIR=%{buildroot}%{_libdir} INCDIR=%{buildroot}%{_includedir}
install -D vbetest %{buildroot}%{_bindir}/vbetest

%files tools
%doc README
%{_bindir}/*

%files -n %{libname}
%{_libdir}/liblrmi.so.%{major}*

%files -n %{devname}
%{_libdir}/liblrmi.so
%{_includedir}/lrmi.h

