%define		_class		HTTP
%define		_subclass	Download
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.1.4
Release:	4
Summary:	Send HTTP Downloads
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTTP_Download/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Provides an easy interface to send hidden files or any arbitrary data to
the client over HTTP. It features HTTP Caching, Compression and Ranges
(partial downloads and resuming).

NOTE: Don't use with PHP's on-the-fly output compression, because files
may be sent coruppted.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.4-3mdv2012.0
+ Revision: 742008
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.4-2
+ Revision: 679359
- mass rebuild

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.4-1mdv2011.0
+ Revision: 587642
- update to new version 1.1.4

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.3-4mdv2010.1
+ Revision: 477894
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.1.3-3mdv2010.0
+ Revision: 441184
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-2mdv2009.1
+ Revision: 322126
- rebuild

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.3-1mdv2009.0
+ Revision: 278924
- update to new version 1.1.3

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-2mdv2009.0
+ Revision: 236885
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri May 04 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-1mdv2008.0
+ Revision: 22354
- 1.1.2


* Fri Mar 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-2mdv2007.1
+ Revision: 139476
- package HTTP/Download/Archive.php too

* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-1mdv2007.1
+ Revision: 81766
- Import php-pear-HTTP_Download

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-1mdk
- 1.1.1
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-1mdk
- initial Mandriva package (PLD import)

