Name:		awesome-gnome
Version:	0.1
Release:	1%{?dist}
Summary:	Awesome in gnome-session

License:	Public Domain
URL:		https://github.com/zapster/awesome-gnome-rpm
Source0:	xsessions/awesome-gnome.desktop
Source1:	gnome-sessions/sessions/awesome.session
Source2:	applications/awesome.desktop

Requires:	awesome
Requires:	gnome-session
BuildRequires:	desktop-file-utils

%description
Awesome window manager in gnome-session


%build


%install
# copy
cp -p ${SOURCE0} %{buildroot}%{_datadir}/%{SOURCE0}
cp -p ${SOURCE1} %{buildroot}%{_datadir}/%{SOURCE1}
cp -p ${SOURCE2} %{buildroot}%{_datadir}/%{SOURCE2}
# verify desktop file
desktop-file-validate %{buildroot}%{_datadir}/%{SOURCE0}
desktop-file-validate %{buildroot}%{_datadir}/%{SOURCE0}
desktop-file-validate %{buildroot}%{_datadir}/%{SOURCE2}


%changelog

