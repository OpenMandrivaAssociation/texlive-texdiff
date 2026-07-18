%global tl_name texdiff
%global tl_revision 79618
%global tl_bin_links texdiff:%{_texmfdistdir}/scripts/texdiff/texdiff

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4
Release:	%{tl_revision}.1
Summary:	Compare documents and produce tagged merge
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/texdiff
License:	artistic
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texdiff.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texdiff.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(texdiff.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
Two files are compared and a new TeX file is output. When the output
file is processed with (La)TeX it marks new changes with blue and old
text with red with a strike-through line. Furthermore, passages with
changes are marked at the margin with grey bars by the LaTeX changebar
package.

