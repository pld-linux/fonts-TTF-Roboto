Summary:	The Roboto family of fonts
Name:		fonts-TTF-Roboto
Version:	2.134
Release:	1
License:	Apache
Group:		Fonts
Source0:	https://github.com/google/roboto/releases/download/v2.134/roboto-unhinted.zip
# Source0-md5:	308966fb7e6d65254c52ff721c8e5c21
URL:		https://github.com/google/roboto/
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
Roboto: Google’s signature family of fonts, the default font on
Android and Chrome OS, and the recommended font for Google’s visual
language, Material Design.

%prep
%setup -q -n roboto-unhinted

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

cp -p *.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%{ttffontsdir}/Roboto*.ttf