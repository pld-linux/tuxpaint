Summary:	Tux Paint
Summary(pl):	Tux Paint
Name:		tuxpaint
Version:	2002.09.29
Release:	0.1
Copyright:	GPL
Group:		Graphics
Source0:	ftp://ftp.sonic.net/pub/users/nbs/unix/x/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	SDL_image-devel >= 1.2.2
BuildRequires:	SDL_ttf-devel >= 2.0.5
BuildRequires:	SDL_mixer-devel >= 1.2.4
#Requires:	
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description

%description -l pl

%prep
%setup -q

#%patch

%build
#./configure --prefix=%{_prefix}
#export CC PREFIX CONFDIE DTA_PREFIX DOC_PREFIX MAN_PREFIX ICON_PREFIX \
#X11_ICON_PREFIX GNOME_PREFIX KDE_PREFIX LOCALE_PREFIX
%{__make} CC=gcc \
PREFIX=/usr/X11R6/ \
CONFDIR=/etc/tuxpaint/ \
DATA_PREFIX=/usr/share/tuxpaint/ \
DOC_PREFIX=/usr/share/doc/ \
MAN_PREFIX=/usr/share/man/ \
ICON_PREFIX=/usr/share/pixmaps/ \
X11_ICON_PREFIX=/usr/X11R6/include/X11/pixmaps/ \
GNOME_PREFIX=/usr/X11R6/share/gnome/apps/Graphisc/ \
KDE_PREFIX=/usr/X11R6/share/applnk/Graphics/ \
LOCALE_PREFIX=/usr/share/locale/ \
RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(,,)
