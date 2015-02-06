%define	name	cxref
%define	version	1.6c
%define release	2

Summary:	C program cross-referencing & documentation tool
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/C
Source0:	http://www.gedanken.demon.co.uk/download-cxref/%name-%version.tgz
URL:		http://www.gedanken.demon.co.uk/cxref/
Buildrequires:	flex bison
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A program that takes as input a series of C source files
and produces a LaTeX or HTML document containing a cross
reference of the files/functions/variables in the program,
including documentation taken from suitably formatted
source code comments.
The documentation is stored in the C source file in
specially formatted comments, making it simple to maintain.
The cross referencing includes lists of functions called,
callers of each function, usage of global variables, header
file inclusion, macro definitions and type definitions.
Works for ANSI C, including many gcc extensions.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

rm -rf $RPM_BUILD_ROOT%_datadir/cxref-cpp.defines

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*



%changelog
* Tue Mar 15 2011 Stéphane Téletchéa <steletch@mandriva.org> 1.6c-1mdv2011.0
+ Revision: 645101
- update to new version 1.6c

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6b-4mdv2011.0
+ Revision: 617490
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.6b-3mdv2010.0
+ Revision: 426271
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.6b-2mdv2009.0
+ Revision: 266550
- rebuild early 2009.0 package (before pixel changes)

* Fri May 02 2008 Funda Wang <fwang@mandriva.org> 1.6b-1mdv2009.0
+ Revision: 200032
- New version 1.6b

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.6a-2mdv2008.1
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import cxref


* Thu Aug 03 2006 Lenny Cartier <lenny@mandriva.com> 1.6a-2mdv2007.0
- rebuild

* Tue Jul 05 2005 Lenny Cartier <lenny@mandriva.com> 1.6a-1mdk
- 1.6a

* Mon Jun 14 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.5g-1mdk
- 1.5g

* Wed Jan 14 2004 Franck Villaume <fvill@freesurf.fr> 1.5e-2mdk
- BuildRequires : bison

* Sun Dec 14 2003 Per �yvind Karlsen <peroyvind@linux-mandrake.com> 1.5e-1mdk
- 1.5e
- rm -rf $RPM_BUILD_ROOT at the beginning of %%install
- spec cosmetics

* Sun May 11 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.5d-1mdk
- 1.5d

* Mon Apr 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.5c-4mdk
- adjust buildrequires

* Wed Jan 22 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.5c-3mdk
- rebuild

* Tue Oct 09 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.5c-2mdk
- fixes by Anton Graham <darkimage@programmer.net> :
	- Add patch from source URL to make useable with gcc-{2.96,3.x}

* Mon Jul 02 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.5c-1mdk
- updated to 1.5c

* Mon Jan 08 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.5b-2mdk
- rebuild
- add url

* Wed Sep 27 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.5b-1mdk
- stop providing the docs

* Tue Oct 19 1999 Lenny Cartier <lenny@mandrakesoft.com>
- Specfile adaptation for Mandrake

* Mon Oct 18 1999 Richard Jackson <richardj@1gig.net>
- initial RPM build



