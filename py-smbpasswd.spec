%define name py-smbpasswd
%define ver 1.0.1
%define rel %mkrel 7

%define have_pre %(echo %ver|awk '{p=0} /[a-z,A-Z][a-z,A-Z]/ {p=1} {print p}')
%if %have_pre
%define version %(perl -e '$name="%ver"; print ($name =~ /(.*?)[a-z]/);')
%define release 0.%(echo %ver|sed -e 's/%version//g').%rel
%else
%define version %ver
%define release %rel
%endif

Summary: 	NT/LM hash generation module for Python
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://barryp.org/software/%{name}/files/py-smbpasswd-%{ver}.tar.gz
License:	GPL
Group: 		Development/Python
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Url: 		https://barryp.org/software/%{name}/
BuildRequires:	libxine-devel python-devel
Provides:	python-smbpasswd = %version-%release

%description
This module can generate both LANMAN and NT password hashes, suitable for use
with Samba.

Sample usage
    import smbpasswd
    pwd = 'mypassword'
    print 'LANMAN hash is', smbpasswd.lmhash(pwd)
    print 'NT hash is', smbpasswd.nthash(pwd)
    print 'both hashes at once = %s:%s (lm:nt)' % smbpasswd.hash(pwd)

%prep
%setup -q -n py-smbpasswd-%ver

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README.txt



%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.0.1-7mdv2010.0
+ Revision: 442007
- rebuild

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 1.0.1-6mdv2009.1
+ Revision: 325817
- fix spec
- rebuild

  + Jérôme Soyer <saispo@mandriva.org>
    - Rename

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-4mdv2009.0
+ Revision: 259472
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-3mdv2009.0
+ Revision: 247326
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0.1-1mdv2008.1
+ Revision: 136447
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 06 2007 Buchan Milne <bgmilne@mandriva.org> 1.0.1-1mdv2008.0
+ Revision: 80514
- New verison 1.0.1

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2008.0
+ Revision: 69409
- use %%mkrel


* Sun Apr 03 2005 Michael Scherer <misc@mandrake.org> 1.0-2mdk
- Rebuild for new python

* Tue Jul 20 2004 Buchan Milne <bgmilne@linux-mandrake.com> 1.0-1mdk
- First Mandrake package

