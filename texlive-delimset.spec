Name:		texlive-delimset
Version:	71829
Release:	1
Summary:	Typeset and declare sets of delimiters with convenient size control
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/delimset
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/delimset.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/delimset.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/delimset.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
delimset is a LaTeX2e package to typeset and declare sets of
delimiters in math mode whose size can be adjusted
conveniently.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/delimset
%{_texmfdistdir}/tex/latex/delimset
%doc %{_texmfdistdir}/doc/latex/delimset

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
