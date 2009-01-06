%define name python-smbpasswd
%define ver 1.0.1
%define rel %mkrel 6

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
Prefix: 	%{_prefix}
Url: 		http://barryp.org/software/%{name}/
BuildRequires:	libxine-devel python-devel

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

