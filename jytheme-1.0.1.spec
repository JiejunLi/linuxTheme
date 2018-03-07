Name:           jytheme
Version:       	1.0
Release:        1%{?dist}
Summary:        jieyun Tech

License:        GPL
URL:            www.jieyung.com
Source0:        %{name}-%{version}.tar.gz

#BuildRequires:  
#Requires:       

#buildroot:	/tmp/

%description 
HCI startup darwin

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
rm -rf .git
mkdir -p %{buildroot}/usr/share/plymouth/themes/darwin/
ls
cp *.png %{buildroot}/usr/share/plymouth/themes/darwin/
cp *.plymouth %{buildroot}/usr/share/plymouth/themes/darwin/
cp *.script %{buildroot}/usr/share/plymouth/themes/darwin/

%files
%defattr(-,root,root,-) 
%attr(0755,root,root)/usr/share/plymouth/themes/darwin/*.png
%attr(0755,root,root)/usr/share/plymouth/themes/darwin/*.plymouth
%attr(0755,root,root)/usr/share/plymouth/themes/darwin/*.script

%post
plymouth-set-default-theme -R darwin 

%clean
rm -rf %{buildroot}

%changelog
* Thu Sep 14 2017 lijiejun <lijiejun@jieyung.com> 0.1-1
- Initial it.
