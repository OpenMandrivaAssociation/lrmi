%define major 0
%define libname %mklibname %name %major

Summary:	Library for calling real mode BIOS routines under Linux
Name:		lrmi
Version:	0.10
Release:	%mkrel 14
License:	MIT
Group:		System/Libraries
URL:		http://sourceforge.net/projects/lrmi/
Source0:	http://prdownloads.sourceforge.net/lrmi/%{name}-%{version}.tar.bz2
Patch0:		lrmi-0.10-makefile.patch
Patch1:		lrmi-no_strip.diff
Patch2:		lrmi-build_fix.diff
Patch3:		lrmi-shared_vbetest_fix.diff
ExclusiveArch:	%ix86
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
LRMI is a library for calling real mode BIOS routines under Linux.

%package -n	%{libname}
Summary:	Library for calling real mode BIOS routines under Linux
Group:		System/Libraries

%description -n	%{libname}
LRMI is a library for calling real mode BIOS routines under Linux.

%package -n	%{libname}-devel
Summary:	Library for calling real mode BIOS routines under Linux
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	liblrmi-devel = %{version}-%{release}

%description -n	%{libname}-devel
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
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_libdir} %{buildroot}%{_includedir}

%makeinstall LIBDIR=%{buildroot}%{_libdir} INCDIR=%{buildroot}%{_includedir}
install -D vbetest %{buildroot}%{_bindir}/vbetest

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files tools
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


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10-13mdv2011.0
+ Revision: 666096
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.10-12mdv2011.0
+ Revision: 606420
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.10-11mdv2010.1
+ Revision: 521148
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.10-10mdv2010.0
+ Revision: 426005
- rebuild

* Tue Apr 07 2009 Funda Wang <fwang@mandriva.org> 0.10-9mdv2009.1
+ Revision: 364628
- rebuild

* Sun Sep 14 2008 Oden Eriksson <oeriksson@mandriva.com> 0.10-9mdv2009.0
+ Revision: 284725
- rebuild
- fix build

  + Pascal Terjan <pterjan@mandriva.org>
    - Move the tool to the -tool subpackage which was empty

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.10-6mdv2008.1
+ Revision: 170968
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.10-5mdv2008.1
+ Revision: 152869
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sun Mar 18 2007 Oden Eriksson <oeriksson@mandriva.com> 0.10-3mdv2007.1
+ Revision: 146121
- added P1 to prevent borky strip in the install
- bunzip patches

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - Import lrmi

* Wed Apr 05 2006 Götz Waschk <waschk@mandriva.org> 0.10-2mdk
- this is for x86 only

* Tue Apr 04 2006 Götz Waschk <waschk@mandriva.org> 0.10-1mdk
- initial package

