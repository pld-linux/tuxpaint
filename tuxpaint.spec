%define		stamps_ver	2003.12.23
Summary:	Tux Paint - A simple drawing program for children
Summary(pl):	Tux Paint - Prosty program do rysowania dla dzieci
Name:		tuxpaint
Version:	0.9.13
Release:	2
Epoch:		1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	580ed290af35c34a33f2206f7f36e489
Source1:	http://dl.sourceforge.net/%{name}/%{name}-stamps-%{stamps_ver}.tar.gz
# Source1-md5:	701fb126d9956ed113935bb0e1016a59
Source2:	%{name}.desktop
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-opt.patch
URL:		http://www.newbreedsoftware.com/tuxpaint/
BuildRequires:	SDL_image-devel >= 1.2.2
BuildRequires:	SDL_mixer-devel >= 1.2.4
BuildRequires:	SDL_ttf-devel >= 2.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11

%description
Tux Paint is a simple drawing program for young children (3-10 years
old). It is not meant as a general-purpose drawing tool. It is meant
to be fun and easy to use. Sound effects and a cartoon character help
let the user know what's going on, and keeps them entertained. There
are also extra-large cartoon-style mouse pointer shapes.

%description -l pl
Tux Paint jest prostym programem rysunkowym dla dzieci (3-10 lat). Nie
ma on byæ narzêdziem s³u¿±cym ogólnemu celowi nauki rysowania, lecz
programem ³atwym w u¿yciu, s³u¿±cym zabawie. Efekty d¼wiêkowe i
komiksowy charakter pomagaj± u¿ytkownikowi w ³atwym poruszaniu siê po
programie, czyni±c go rozrywkowym. W programie jest tak¿e du¿y
wska¼nik myszki oraz przyciski utrzymane w stylu komiksowym.

%package stamps
Summary:	Tux Paint - Collection of "rubber stamp" images
Summary(pl):	Tux Paint - Kolekcja obrazów z "gumowej piecz±tki"
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}

%description stamps
This is a collection of "rubber stamp" images for Tux Paint.

%description stamps -l pl
Jest to kolekcja obrazów dla Tux Painta zwana "gumowa piecz±tka".

%prep
%setup -q -a 1
%patch0 -p0
#%patch1 -p1

install %{SOURCE2} src

%build
%{__make} CC=%{__cc} \
	PREFIX=%{_prefix}/ \
	CONFDIR=%{_sysconfdir}/ \
	DATA_PREFIX=%{_datadir}/tuxpaint/ \
	DOC_PREFIX=%{_datadir}/doc/ \
	ICON_PREFIX=%{_pixmapsdir}/ \
	X11_ICON_PREFIX=%{_pixmapsdir}/ \
	LOCALE_PREFIX=%{_datadir}/locale \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/%{name},%{_pixmapsdir},%{_applnkdir}/Graphics,%{_datadir}/%{name}/stamps}

%{__make} install \
	_prefix=$RPM_BUILD_ROOT%{_prefix}/ \
	CONFDIR=$RPM_BUILD_ROOT%{_sysconfdir}/ \
	MAN_PREFIX=$RPM_BUILD_ROOT%{_mandir}/ \
	GNOME_PREFIX=$RPM_BUILD_ROOT%{_prefix}/ \
	KDE_PREFIX=$RPM_BUILD_ROOT%{_applnkdir}/ \
	X11_ICON_PREFIX=$RPM_BUILD_ROOT%{_pixmapsdir}/

install src/tuxpaint.conf $RPM_BUILD_ROOT%{_sysconfdir}
install data/images/icon48x48.png $RPM_BUILD_ROOT%{_pixmapsdir}/tuxpaint.png

%{__make} -C %{name}-stamps-%{stamps_ver} install \
	DATA_PREFIX=$RPM_BUILD_ROOT%{_datadir}/%{name}/

%find_lang %{name}

%clean
chmod -R a+rwX $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%lang(pl) %{_mandir}/pl/man?/*
%{_sysconfdir}/tuxpaint.conf
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/brushes
%{_datadir}/%{name}/fonts
%{_datadir}/%{name}/images
%{_datadir}/%{name}/sounds
%{_applnkdir}/Graphics/*
%{_pixmapsdir}/*

%files stamps
%defattr(644,root,root,755)
%{_datadir}/%{name}/stamps
