Name: mtxclient
Version: 0.7.0
Release: 1
Group:   System/Libraries
License: MIT
Summary: Client API library for Matrix, built on top of Boost.Asio
URL: https://github.com/Nheko-Reborn/mtxclient
Source0: https://github.com/Nheko-Reborn/mtxclient/archive/v%{version}/%{name}-%{version}.tar.gz
 
BuildRequires: cmake(mpark_variant)
BuildRequires: cmake(nlohmann_json)
BuildRequires: cmake(Olm)
BuildRequires: cmake(spdlog)
BuildRequires: pkgconfig(coeurl)
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(libevent)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(zlib)
BuildRequires: cmake
BuildRequires: ninja
 
%description
Client API library for the Matrix protocol, built on top of Boost.Asio.
 
%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
 
%description devel
%{summary}.
 
%prep
%autosetup -p1
 
%build
%cmake \
    -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DHUNTER_ENABLED:BOOL=OFF \
    -DUSE_BUNDLED_COEURL:BOOL=OFF \
    -DUSE_BUNDLED_GTEST:BOOL=OFF \
    -DUSE_BUNDLED_JSON:BOOL=OFF \
    -DUSE_BUNDLED_LIBCURL:BOOL=OFF \
    -DUSE_BUNDLED_LIBEVENT:BOOL=OFF \
    -DUSE_BUNDLED_OLM:BOOL=OFF \
    -DUSE_BUNDLED_OPENSSL:BOOL=OFF \
    -DUSE_BUNDLED_SPDLOG:BOOL=OFF \
    -DASAN:BOOL=OFF \
    -DCOVERAGE:BOOL=OFF \
    -DIWYU:BOOL=OFF \
    -DBUILD_LIB_TESTS:BOOL=OFF \
    -DBUILD_LIB_EXAMPLES:BOOL=OFF
%ninja_build

%install
%ninja_install -C build
ln -s libmatrix_client.so.%{version} %{buildroot}%{_libdir}/libmatrix_client.so.0
 
%files
%doc README.md
%license LICENSE
%{_libdir}/*.so.0*
 
%files devel
%{_includedir}/%{name}
%{_includedir}/mtx
%{_includedir}/mtx.hpp
%{_libdir}/cmake/MatrixClient
%{_libdir}/*.so
