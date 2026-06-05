# set to nil when packaging a release,
# or the long commit tag for the specific git branch
%define commit_tag f5766cb53c244a808b7e512c7b83b3942fb67834

# when using a commit_tag (i.e. not nil) add a commit date
# decoration ~0.yyyyMMdd to Version number
%if "%{commit_tag}" != "%{nil}"
%define commit_date 20260301
%endif

%define libname %mklibname mtxclient
%define devname %mklibname mtxclient -d

Name: mtxclient
Version: 0.10.2%{?commit_date:~0.%{commit_date}}
Release: 1
Group:   System/Libraries
License: MIT
Summary: Client API library for Matrix, built on top of Boost.Asio
URL: https://github.com/Nheko-Reborn/mtxclient

# change the source URL depending on if the package is a release version or a git version
%if "%{commit_tag}" != "%{nil}"
Source0:       %url/archive/%{commit_tag}/%{name}-%{version}.tar.gz
%else
Source0:       %url/archive/%{version}/%{name}-%{version}.tar.gz
%endif

BuildSystem:   cmake
BuildOption:   -DCMAKE_BUILD_TYPE=Release
BuildOption:   -DHUNTER_ENABLED:BOOL=OFF
BuildOption:   -DUSE_BUNDLED_COEURL:BOOL=OFF
BuildOption:   -DUSE_BUNDLED_GTEST:BOOL=OFF
BuildOption:   -DUSE_BUNDLED_JSON:BOOL=OFF
BuildOption:   -DUSE_BUNDLED_LIBCURL:BOOL=OFF
BuildOption:   -DUSE_BUNDLED_LIBEVENT:BOOL=OFF
BuildOption:   -DUSE_BUNDLED_OLM:BOOL=OFF
BuildOption:   -DUSE_BUNDLED_OPENSSL:BOOL=OFF
BuildOption:   -DUSE_BUNDLED_SPDLOG:BOOL=OFF
BuildOption:   -DASAN:BOOL=OFF
BuildOption:   -DCOVERAGE:BOOL=OFF
BuildOption:   -DIWYU:BOOL=OFF
BuildOption:   -DBUILD_LIB_TESTS:BOOL=OFF
BuildOption:   -DBUILD_LIB_EXAMPLES:BOOL=OFF

BuildRequires: cmake(mpark_variant)
BuildRequires: cmake(nlohmann_json)
BuildRequires: cmake(Olm)
BuildRequires: cmake(spdlog)
BuildRequires: pkgconfig(coeurl) >= 0.3.0
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(libevent)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(re2)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(fmt)
 
%description
Client API library for the Matrix protocol, built on top of Boost.Asio.

%package -n %{libname}
Summary:	Library for MTXclient
Group:		System/Libraries
Provides: mtxclient

%description -n %{libname}
Client API library for the Matrix protocol, built on top of Boost.Asio.
 
%package -n %{devname}
Summary: Development files for %{name}
Requires:	%{libname} = %{version}-%{release}
Provides: mtxclient-devel
 
%description -n	%{devname}
%{summary}.
 
%files -n %{libname}
%doc README.md
%license LICENSE
%{_libdir}/*.so.0*
 
%files -n %{devname}
%{_includedir}/%{name}
%{_includedir}/mtx
%{_includedir}/mtx.hpp
%{_libdir}/cmake/MatrixClient
%{_libdir}/*.so
