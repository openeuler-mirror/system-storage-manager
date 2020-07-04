%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/system-storage-manager-%{version}}

Name:           system-storage-manager
Version:        1.3
Release:        2
Summary:        A single tool to manage your storage
License:        GPLv2+
URL:            https://system-storage-manager.github.io/
Source0:        https://github.com/system-storage-manager/ssm/archive/system-storage-manager-%{version}.tar.gz
Patch0000:      python3-sphinx.patch
BuildArch:      noarch
Requires:       util-linux which xfsprogs e2fsprogs python3-pwquality
BuildRequires:  python3-devel python3-sphinx python3-pwquality

%description
system Storage Manager has developed a convenient command-line interface.

In more complex enterprise storage environment, using the device mapper (dm), 
the logical volume manager (LVM) or multiple devices (md) it would be difficult to manage, 
because of the addition of the file system, the tools needed to configure and manage storage
quantity has become more, so that the user is difficult to grasp, and system administrators
to consider too many options, so have a greater chance for mistakes and problems.

System Storage Manager can manage Storage using LVM, BTRFS, encrypted volumes, 
and many other technologies. BTRFS management tools can simplify Storage management, 
and we are working to bring this ease of use to Linux file systems.

%prep
%autosetup -n ssm-system-storage-manager-%{version} -p1

%build
make docs

%install
%{__python3} setup.py install --root=${RPM_BUILD_ROOT}
if [ "%{_pkgdocdir}" != "%{_docdir}/system-storage-manager-%{version}" ]; then
    mv ${RPM_BUILD_ROOT}/{%{_docdir}/system-storage-manager-%{version},%{_pkgdocdir}}
fi

%check
%{__python3} test.py || :

%files
%{_bindir}/*
%{_pkgdocdir}/
%{_mandir}/man8/*
%{python3_sitelib}/*

%changelog
* Fri Jul 03 2020  yaokai <yaokai13@huawei.com> - 1.3-2
- Package init
