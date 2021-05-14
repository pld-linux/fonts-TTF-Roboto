Summary:	The Roboto family of fonts
Summary(pl.UTF-8):	Rodzina fontów Roboto
Name:		fonts-TTF-Roboto
Version:	2.138
Release:	1
License:	Apache v2.0
Group:		Fonts
#Source0Download: https://github.com/google/roboto/releases
Source0:	https://github.com/google/roboto/releases/download/v%{version}/roboto-unhinted.zip?/roboto-unhinted-%{version}.zip
# Source0-md5:	5bf2e05feff2c242a1796557aaec9953
URL:		https://github.com/google/roboto/
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
Roboto: Google's signature family of fonts, the default font on
Android and Chrome OS, and the recommended font for Google's visual
language, Material Design.

%description -l pl.UTF-8
Roboto to rodzina fontów firmowana przez Google, domyślny font w
systemach Android i Chrome, zalecany font dla języka wizualnego
Google'a Material Design.

%prep
%setup -qc

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
