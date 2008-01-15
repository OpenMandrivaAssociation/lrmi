%define major 0
%define libname %mklibname %name %major

Summary:	LRMI is a library for calling real mode BIOS routines under Linux
Name:		lrmi
Version:	0.10
Release:	%mkrel 4
License:	MIT
Group:		System/Libraries
URL:		http://sourceforge.net/projects/lrmi/
Source0:	http://prdownloads.sourceforge.net/lrmi/%{name}-%{version}.tar.bz2
Patch0:		lrmi-0.10-makefile.patch
Patch1:		lrmi-no_strip.diff
ExclusiveArch:	%ix86
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
LRMI is a library for calling real mode BIOS routines under Linux.

%package -n	%{libname}
Summary:	LRMI is a library for calling real mode BIOS routines under Linux
Group:		System/Libraries

%description -n	%{libname}
LRMI is a library for calling real mode BIOS routines under Linux.

%package -n	%{libname}-devel
Summary:	LRMI is a library for calling real mode BIOS routines under Linux
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	liblrmi-devel = %{version}-%{release}

%description -n	%{libname}-devel
LRMI is a library for calling real mode BIOS routines under Linux.

%package	tools
Summary:	LRMI is a library for calling real mode BIOS routines under Linux
Group:		System/Configuration/Hardware

%description	tools
LRMI is a library for calling real mode BIOS routines under Linux.

%prep

%setup -q
%patch0 -p1
%patch1 -p0

%build
%make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_libdir} %{buildroot}%{_includedir}

%makeinstall LIBDIR=%{buildroot}%{_libdir} INCDIR=%{buildroot}%{_includedir}
install -D vbetest %{buildroot}%{_bindir}/vbetest

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/liblrmi.so.%{major}*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/liblrmi.so
%{_includedir}/lrmi.h


