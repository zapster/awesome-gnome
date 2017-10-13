# INFO: Package contains data-only, no binaries, so no debuginfo is needed
%global debug_package %{nil}

Name:		awesome-gnome
Version:	0.1
Release:	1%{?dist}
Summary:	Awesome in gnome-session

License:	Public Domain
URL:		https://github.com/zapster/awesome-gnome-rpm
Source0:	awesome-gnome.desktop
Source1:	awesome.session
Source2:	awesome.desktop

BuildArch:  noarch

Requires:	awesome
Requires:	gnome-session
BuildRequires:	desktop-file-utils

%description
Awesome window manager in gnome-session


%build


%install
# copy
install -D -m 644 %{SOURCE0} %{buildroot}%{_datadir}/xsessions/awesome-gnome.desktop
install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/gnome-session/sessions/awesome.session
install -D -m 644 %{SOURCE2} %{buildroot}%{_datadir}/applications/awesome.desktop
# verify desktop file
#desktop-file-validate %{buildroot}%{_datadir}/xsessions/awesome-gnome.desktop
#desktop-file-validate %{buildroot}%{_datadir}/applications/awesome.desktop

%files
%{_datadir}/xsessions/awesome-gnome.desktop
%{_datadir}/gnome-session/sessions/awesome.session
%{_datadir}/applications/awesome.desktop

%changelog

