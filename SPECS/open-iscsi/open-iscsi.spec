Summary:        iSCSI tools for Linux
Name:           open-iscsi
Version:        2.1.3
Release:        1%{?dist}
License:        GPLv2
URL:            https://github.com/open-iscsi/open-iscsi
Group:          Applications/System
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        %{name}-%{version}.tar.gz
%define sha1    open=19aa834f5a6033fd0e53d4e32a8f28c4a3d5ec58

BuildRequires:  open-isns-devel
BuildRequires:  openssl-devel
BuildRequires:  kmod-devel
BuildRequires:  systemd-devel
BuildRequires:  util-linux-devel

Requires:       openssl
Requires:       kmod
Requires:       systemd
Requires:       util-linux

%description
iSCSI tools for Linux

%package devel
Summary: Development Libraries for open-iscsi
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
%description devel
Header files for doing development with open-iscsi.

%prep
%setup -q

%build
sed -i 's/lib64/lib/g' libopeniscsiusr/Makefile
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
install -d %{buildroot}%{_unitdir}
install -pm 644 etc/systemd/iscsi.service %{buildroot}%{_unitdir}
install -pm 644 etc/systemd/iscsid.service %{buildroot}%{_unitdir}
install -pm 644 etc/systemd/iscsid.socket %{buildroot}%{_unitdir}
install -pm 644 etc/systemd/iscsiuio.service %{buildroot}%{_unitdir}
install -pm 644 etc/systemd/iscsiuio.socket %{buildroot}%{_unitdir}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_sysconfdir}/iscsi/ifaces/iface.example
%config(noreplace) %{_sysconfdir}/iscsi/initiatorname.iscsi
%config(noreplace) %{_sysconfdir}/iscsi/iscsid.conf
/sbin/iscsi-gen-initiatorname
/sbin/iscsi-iname
/sbin/iscsi_discovery
/sbin/iscsi_fw_login
/sbin/iscsi_offload
/sbin/iscsiadm
/sbin/iscsid
/sbin/iscsistart
/sbin/iscsiuio
%{_unitdir}/iscsi.service
%{_unitdir}/iscsid.service
%{_unitdir}/iscsid.socket
%{_unitdir}/iscsiuio.service
%{_unitdir}/iscsiuio.socket
%{_libdir}/libopeniscsiusr.so.*
%{_mandir}/man8/iscsi-iname.8.gz
%{_mandir}/man8/iscsi_discovery.8.gz
%{_mandir}/man8/iscsi_fw_login.8.gz
%{_mandir}/man8/iscsiadm.8.gz
%{_mandir}/man8/iscsid.8.gz
%{_mandir}/man8/iscsistart.8.gz
%{_mandir}/man8/iscsiuio.8.gz

%files devel
%defattr(-,root,root)
%{_includedir}/libopeniscsiusr.h
%{_includedir}/libopeniscsiusr_common.h
%{_includedir}/libopeniscsiusr_iface.h
%{_includedir}/libopeniscsiusr_session.h
%{_includedir}/libopeniscsiusr_node.h
%{_libdir}/libopeniscsiusr.so
%{_libdir}/pkgconfig/libopeniscsiusr.pc

%changelog
* Tue Feb 16 2021 Susant Sahani <ssahani@vmware.com> 2.1.3-1
- Initial version.
