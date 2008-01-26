#
# TODO
# - check locale names (I think there is some wrong)
%define		stamps_ver	2007.11.21
Summary:	Tux Paint - A simple drawing program for children
Summary(pl.UTF-8):	Tux Paint - Prosty program do rysowania dla dzieci
Name:		tuxpaint
Version:	0.9.18
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/tuxpaint/%{name}-%{version}.tar.gz
# Source0-md5:	5d1ee8aabfef787702f8ddef257fc1a7
Source1:	http://dl.sourceforge.net/tuxpaint/%{name}-stamps-%{stamps_ver}.tar.gz
# Source1-md5:	1a4e032ff67920248931247787f331a1
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-vfolders.patch
Patch2:		%{name}-locale_names.patch
URL:		http://www.tuxpaint.org/
BuildRequires:	SDL_Pango-devel
BuildRequires:	SDL_image-devel >= 1.2.2
BuildRequires:	SDL_mixer-devel >= 1.2.4
BuildRequires:	SDL_ttf-devel >= 2.0.5
BuildRequires:	gettext-devel
BuildRequires:	libpaper-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11

%description
Tux Paint is a simple drawing program for young children (3-10 years
old). It is not meant as a general-purpose drawing tool. It is meant
to be fun and easy to use. Sound effects and a cartoon character help
let the user know what's going on, and keeps them entertained. There
are also extra-large cartoon-style mouse pointer shapes.

%description -l pl.UTF-8
Tux Paint jest prostym programem do rysowania dla dzieci (3-10 lat).
Nie jest on narzędziem służącym do nauki rysowania, lecz programem
łatwym w użyciu, służącym zabawie. Efekty dźwiękowe i komiksowy
charakter pomagają użytkownikowi w łatwym poruszaniu się po
programie, czyniąc go rozrywkowym. W programie jest także duży
wskaźnik myszki oraz przyciski utrzymane w stylu komiksowym.

%package stamps
Summary:	Tux Paint - Collection of "rubber stamp" images
Summary(pl.UTF-8):	Tux Paint - Kolekcja obrazów z "gumowej pieczątki"
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description stamps
This is a collection of "rubber stamp" images for Tux Paint.

%description stamps -l pl.UTF-8
Jest to kolekcja obrazów dla Tux Painta o nazwie "gumowa pieczątka".

%prep
%setup -q -a 1
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	CC="%{__cc}" \
	PREFIX="%{_prefix}" \
	CONFDIR="%{_sysconfdir}" \
	DATA_PREFIX="%{_datadir}/tuxpaint" \
	DOC_PREFIX="%{_datadir}/doc" \
	ICON_PREFIX="%{_pixmapsdir}" \
	X11_ICON_PREFIX="%{_pixmapsdir}" \
	LOCALE_PREFIX="%{_datadir}/locale" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/%{name},%{_pixmapsdir},%{_desktopdir},%{_datadir}/%{name}/stamps}

%{__make} install \
	_prefix=$RPM_BUILD_ROOT%{_prefix}/ \
	CONFDIR=$RPM_BUILD_ROOT%{_sysconfdir}/ \
	MAN_PREFIX=$RPM_BUILD_ROOT%{_mandir}/ \
	GNOME_PREFIX=$RPM_BUILD_ROOT%{_prefix}/ \
	KDE_PREFIX=$RPM_BUILD_ROOT%{_desktopdir}/ \
	X11_ICON_PREFIX=$RPM_BUILD_ROOT%{_pixmapsdir}/

install src/tuxpaint.conf $RPM_BUILD_ROOT%{_sysconfdir}
install data/images/icon48x48.png $RPM_BUILD_ROOT%{_pixmapsdir}/tuxpaint.png

%{__make} -C %{name}-stamps-%{stamps_ver} install \
	DATA_PREFIX=$RPM_BUILD_ROOT%{_datadir}/%{name}/

chmod -R a+rwx $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_datadir}/{doc/tuxpaint,gnome/apps,tuxpaint/CVS}

#rm a lot of unwanted files and directories:
find docs/ -type d|grep CVS|xargs rm -rf
find docs/ -name "[KC]OP*" -exec rm -f "{}" ";"
find docs/ -name "INS*" -exec rm -f "{}" ";"
find docs/ -name "AUT*" -exec rm -f "{}" ";"
find docs/ -size -50c -type f -exec rm -f "{}" ";"
find docs/ -empty |xargs rm -rf

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%lang(pl) %{_mandir}/pl/man?/*
%{_sysconfdir}/tuxpaint.conf
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/plugins/
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/brushes
%{_datadir}/%{name}/fonts
%{_datadir}/%{name}/images
%{_datadir}/%{name}/sounds
%{_datadir}/%{name}/starters
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*

%files stamps
%defattr(644,root,root,755)
%{_datadir}/%{name}/stamps
