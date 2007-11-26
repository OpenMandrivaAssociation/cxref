%define	name	cxref
%define	version	1.6a
%define	release	%mkrel 2

Summary:	C program cross-referencing & documentation tool
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/C
Source0:	%{name}-%{version}.tar.bz2
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
%configure
%make
#make docs

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

