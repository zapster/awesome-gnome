Name:		awesome-gnome
Version:	0.1
Release:	1%{?dist}
Summary:	Awesome in gnome-session

License:	Public Domain
URL:		https://github.com/zapster/awesome-gnome-rpm
Source0:	

Requires:	awesome

%description
Awesome window manager in gnome-session


%build


%install
# verify desktop file
# desktop-file-validate %{buildroot}%{_datadir}/xsessions/%{name}.desktop


%changelog

