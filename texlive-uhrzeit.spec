%global tl_name uhrzeit
%global tl_revision 79121

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2c
Release:	%{tl_revision}.1
Summary:	Time printing, in German
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uhrzeit
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uhrzeit.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uhrzeit.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The primary goal of this package is to facilitate formats and ranges of
times as formerly used in Germany. A variety of printing formats are
available.

