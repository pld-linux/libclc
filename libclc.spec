# NOTE: for OpenCL libclc for llvm see llvm-libclc.spec; this library has nothing to do with OpenCL
Summary:	ISO C implementation of an ad-hoc extension library
Summary(pl.UTF-8):	Implementacja ISO C biblioteki rozszerzeń
Name:		libclc
Version:	0.1.5
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libclc/%{name}-%{version}.tar.gz
# Source0-md5:	7a79b796aaf968fc85bcf99a39766894
URL:		http://libclc.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libclc is a project undertaken by comp.lang.c regulars in order to
provide a portable API for most useful and common programming tasks.
It aims at providing services for the following tasks among others:
strings, file I/O, logging & error recovery, memory management, base
conversion, date & time, sorting & searching, hashing, lists, queues,
stacks, trees & other abstract data structures, random numbers,
crypto, database, graphs.

%description -l pl.UTF-8
libclc to projekt utrzymywany przez bywalców comp.lang.c w celu
dostarczenia przenośnego API do większości przydatnych i popularnych
zadań programistycznych. Celem jest zapewnienie obsługi następujących
elementów: łańcuchów znaków, we/wy na plikach, logowania i wznawianiu
po błędach, zarządzania pamięcią, zmiany podstawy obliczeń, daty i
czasu, sortowania i wyszukiwania, haszowania, list, kolejek, stosów,
drzew i innych abstrakcyjnych struktur danych, liczb losowych,
kryptografii, baz danych, grafów.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS
%{_libdir}/libclc.a
%{_libdir}/libclc_d.a
%{_includedir}/clc*.h
%{_mandir}/man3/clc*.3*
