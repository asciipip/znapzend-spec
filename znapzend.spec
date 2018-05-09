Name: znapzend
Version: 0.18.0
Release: 1%{?dist}
Summary: zfs backup with remote capabilities and mbuffer integration
License: GPLv3+
URL: http://www.znapzend.org
Source: https://github.com/oetiker/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

%description
ZnapZend is a ZFS centric backup tool. It relies on snapshot, send and
receive to do its work. It has the built-in ability to manage both local
snapshots as well as remote copies by thinning them out as time
progresses.

%prep
%setup

%build
./configure --prefix=/opt/znapzend
make

%install
make DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir} install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
for prog in $(ls $RPM_BUILD_ROOT/opt/znapzend/bin); do
    ln -s /opt/znapzend/bin/$prog $RPM_BUILD_ROOT/%{_bindir}/$prog
done
mkdir -p $RPM_BUILD_ROOT/%{_unitdir}
<init/znapzend.service perl -pe 's{NONE/bin}{%{_bindir}}' >$RPM_BUILD_ROOT/%{_unitdir}/znapzend.service

%files
/opt/znapzend
%doc README.md LICENSE COPYRIGHT CHANGES
%{_bindir}/*
%{_unitdir}/*
%{_mandir}/*/*
