Summary:	Tux Paint - A simple drawing program for children
Summary(pl):	Tux Paint - Prosty program do rysowania dla dzieci
Name:		tuxpaint
Version:	2002.09.29
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.sonic.net/pub/users/nbs/unix/x/%{version}/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.sonic.net/pub/users/nbs/unix/x/%{name}/stamps/%{name}-stamps-%{version}.tar.gz
Source2:	tuxpaint.desktop
Patch0:		%{name}-Makefile.patch
URL:		http://www.newbreedsoftware.com/tuxpaint/
BuildRequires:	SDL_image-devel >= 1.2.2
BuildRequires:	SDL_mixer-devel >= 1.2.4
BuildRequires:	SDL_ttf-devel >= 2.0.5
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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
Requires:	%{name} = %{version}

%description stamps
This is a collection of "rubber stamp" images for Tux Paint.

%description stamps -l pl
Jest to kolekcja obrazów dla Tux Painta zwana "gumowa piecz±tka".

%prep
%setup -q
%patch0 -p0

%build
%{__make} CC=%{__cc} \
	PREFIX=%{_prefix}/ \
	CONFDIR=%{_sysconfdir}/tuxpaint/ \
	DATA_PREFIX=%{_datadir}/tuxpaint/ \
	DOC_PREFIX=%{_datadir}/doc/ \
	MAN_PREFIX=%{_mandir}/ \
	ICON_PREFIX=%{_datadir}/pixmaps/ \
	X11_ICON_PREFIX=%{_datadir}/pixmaps/ \
	GNOME_PREFIX=%{_applnkdir}/Graphics/ \
	KDE_PREFIX=%{_applnkdir}/Graphics/ \
	LOCALE_PREFIX=%{_datadir}/locale/ \
	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/%{name},%{_pixmapsdir},%{_applnkdir}/Graphics,%{_datadir}/%{name}/stamps}

%{__make} _prefix=$RPM_BUILD_ROOT%{_prefix} install

install src/tuxpaint.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install data/images/icon32x32.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps/tuxpaint.xpm
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Graphics

tar zxf %{SOURCE1}
cd %{name}-stamps-%{version}
cd stamps
cp -rf cartoon $RPM_BUILD_ROOT%{_datadir}/%{name}/stamps/
cp -rf misc $RPM_BUILD_ROOT%{_datadir}/%{name}/stamps/
cp -rf photo $RPM_BUILD_ROOT%{_datadir}/%{name}/stamps/

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc docs
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/%{name}
%{_applnkdir}/*
%{_pixmapsdir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/brushes
%{_datadir}/%{name}/fonts
%{_datadir}/%{name}/images
%{_datadir}/%{name}/sounds

%files stamps
%defattr(644,root,root,755)
%{_datadir}/%{name}/stamps
