Summary:	Python toolkit for building compound Tkinter widgets.
Summary(pl.UTF-8):	Zestaw narzędzi dla Pythona do budowania komponentów Tkinter
Name:		Pmw
Version:	1.2
Release:	2
License:	MIT
Group:		Development/Languages/Python
Source0:	http://download.sourceforge.net/pmw/%{name}.%{version}.tar.gz
# Source0-md5:	75c49c30595217c8d9376c36aa5426aa
Patch0:		%{name}-env-location.patch
URL:		http://pmw.sourceforge.net/
Requires:	python-tkinter
Requires:	python
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pmw is a toolkit for building high-level compound widgets in Python
using the Tkinter module. It consists of a set of base classes and a
library of flexible and extensible megawidgets built on this
foundation. These megawidgets include notebooks, comboboxes, selection
widgets, paned widgets, scrolled widgets and dialog windows.

%description -l pl.UTF-8
Pmw jest zestawem narzędzi do budowania komponentów wysokiego poziomu
dla Pythona korzystając z modułu Tkinter. Zawiera zestaw podstawowych
klas i bibliotek przenośnych i rozszerzalnych mega-komponentów.
Zawiera notesy, comboboksy, komponenty wybierania, panele, przesuwane
i okna dialogowe.

%prep
%setup -q -n %{name}
%patch0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}
cp -r . $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}/%{name}*/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}*/doc/*
%{py_sitescriptdir}/%{name}
