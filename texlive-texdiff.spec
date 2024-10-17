Name:		texlive-texdiff
Version:	29752
Release:	2
Summary:	Compare documents and produce tagged merge
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/texdiff
License:	ARTISTIC
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdiff.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdiff.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-texdiff.bin = %{EVRD}

%description
Two files are compared and a new TeX file is output. When the
output file is processed with (La)TeX it marks new changes with
blue and old text with red with a strike-through line.
Furthermore, passages with changes are marked at the margin
with grey bars by the LaTeX changebar package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/texdiff
%{_texmfdistdir}/scripts/texdiff/texdiff
%doc %{_mandir}/man1/texdiff.1*
%doc %{_texmfdistdir}/doc/man/man1/texdiff.man1.pdf
%doc %{_texmfdistdir}/doc/support/texdiff/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/texdiff/texdiff texdiff
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
