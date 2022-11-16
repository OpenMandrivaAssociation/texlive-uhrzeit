Name:		texlive-uhrzeit
Version:	39570
Release:	1
Summary:	Time printing, in German
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uhrzeit
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uhrzeit.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uhrzeit.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The primary goal of this package is to facilitate formats and
ranges of times as formerly used in Germany. A variety of
printing formats are available.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/uhrzeit
%doc %{_texmfdistdir}/doc/latex/uhrzeit

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
