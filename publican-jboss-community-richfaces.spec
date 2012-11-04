Summary:	Publican documentation template files for RichFaces community documents
Summary(pl.UTF-8):	Pliki szablonów dokumentacji Publicana dla dokumentów społeczności RichFaces
Name:		publican-jboss-community-richfaces
Version:	1.0
Release:	1
License:	CC-BY-SA
Group:		Development/Tools
Source0:	https://fedorahosted.org/releases/p/u/publican/%{name}-%{version}.tgz
# Source0-md5:	656a22bd5434a8b1c87c6ca6c4e891e1
URL:		https://publican.fedorahosted.org/
BuildRequires:	publican >= 1.0
Requires:	publican >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides common files and templates needed to build
RichFaces community documents with Publican.

%description -l pl.UTF-8
Ten pakiet udostępnia wspólne pliki oraz szablony wymagane do
budowania dokumentów społeczności RichFaces przy użyciu
Publicana.

%prep
%setup -q

%build
publican build --formats=xml --langs=all --publish

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/publican/Common_Content

publican install_brand --path=$RPM_BUILD_ROOT%{_datadir}/publican/Common_Content

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README
%{_datadir}/publican/Common_Content/jboss-community-richfaces
