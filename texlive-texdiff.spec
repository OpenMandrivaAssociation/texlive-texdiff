# revision 26313
# category Package
# catalog-ctan /support/texdiff
# catalog-date 2009-11-10 00:58:07 +0100
# catalog-license artistic
# catalog-version 0.4
Name:		texlive-texdiff
Version:	0.4
Release:	3
Summary:	Compare documents and produce tagged merge
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/texdiff
License:	ARTISTIC
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdiff.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdiff.doc.tar.xz
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
%doc %{_texmfdistdir}/doc/support/texdiff/README
%doc %{_mandir}/man1/texdiff.1*
%doc %{_texmfdir}/doc/man/man1/texdiff.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/texdiff/texdiff texdiff
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
