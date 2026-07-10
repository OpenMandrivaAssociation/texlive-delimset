%global tl_name delimset
%global tl_revision 78523

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.3.1
Release:	%{tl_revision}.1
Summary:	Typeset and declare sets of delimiters with convenient size control
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/delimset
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/delimset.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/delimset.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/delimset.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
delimset is a LaTeX2e package to typeset and declare sets of delimiters
in math mode whose size can be adjusted conveniently.

