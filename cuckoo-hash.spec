%define fullname %{name}-0.0-0.0-3_g31e5106_dirty

Name:           cuckoo-hash
Version:        0.0
Release:        0.0-3_g31e5106_dirty%{?dist}
Summary:        Cuckoo hashing C library
Group:          System Environment/Libraries
License:        LGPLv3+
Source:         %{fullname}.tar.bz2

%description
C library implementing cuckoo hashing algorithm.


%prep
%setup -q -n %{fullname}


%build
%configure
make %{?_smp_mflags}


%check
make check


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_libdir}/*


%package devel
Summary:        Cuckoo hashing C library headers
Requires:       %{name} == %{version}

%description devel
C library implementing cuckoo hashing algorithm.

This package contains development files.


%files devel
%defattr(-,root,root,-)
%{_includedir}/*


%changelog
