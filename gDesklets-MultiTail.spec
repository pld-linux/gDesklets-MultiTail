%define	pname	MultiTail
%define	fname	multitail
Summary:	MultiTail displays multiple log files in one gDesklets display
Summary(pl):	MultiTail wy�wietla zawarto�� wielu plik�w na jednym wy�wietlaczu
Name:		gDesklets-%{pname}
Version:	0.2.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://gdesklets.gnomedesktop.org/files/%{fname}-%{version}.tar.bz2
# Source0-md5:	936d09b9a2247f3ff0adc6f7e3d6f5d8
URL:		http://gdesklets.gnomedesktop.org/categories.php?func=gd_show_app&gd_app_id=52
BuildRequires:	python >= 2.3
BuildRequires:	python-pygtk >= 1.99.18
Requires:	gDesklets
Provides:	gDesklets-display
Provides:	gDesklets-sensor
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_sensorsdir	%{_datadir}/gdesklets/Sensors
%define	_displaysdir	%{_datadir}/gdesklets/Displays

%description
MultiTail displays multiple log files in one gDesklets display.

%description -l pl
MultiTail wy�wietla zawarto�� wielu plik�w na jednym wy�wietlaczu.

%prep
%setup -q -n %{pname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sensorsdir},%{_displaysdir}/%{pname}}

./Install_%{pname}_Sensor.bin --nomsg \
	$RPM_BUILD_ROOT%{_sensorsdir}

cp -R %{pname}/{dark,light,trans}-theme $RPM_BUILD_ROOT%{_displaysdir}/%{pname}

%py_comp $RPM_BUILD_ROOT%{_sensorsdir}
%py_ocomp $RPM_BUILD_ROOT%{_sensorsdir}

rm -f $RPM_BUILD_ROOT%{_sensorsdir}/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{pname}/README
%{_sensorsdir}/*
%{_displaysdir}/*
