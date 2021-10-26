%define pname ed448goldilocks
%define commit 41f349ff802901dc8bd4db8324a462d371713f7f
%define shortcommit %(c=%{commit}; echo ${c:0:8})

%define sname decaf
%define	major 0
%define	libname %mklibname %{sname} %{major}
%define develname %mklibname %{sname} -d

Summary:	An implementation of elliptic curve cryptograph
Name:		lib%{sname}
#Version:	1.0.0
Version:	1.0.1~git20210602
Release:	1
License:	MIT
Group:		System/Libraries
URL:		https://ed448goldilocks.sourceforge.io/
#Source0:	https://downloads.sourceforge.net/ed448goldilocks/%{name}-%{version}.tgz
Source0:	%{pname}-code-%{commit}.zip

BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	python3

%description
The libdecaf library is for elliptic curve research and practical application.
It currently supports Ed448-Goldilocks and Curve25519.

The goals of this library are:
  - Implementing the X25519, X448 key exchange protocols (RFC 7748).
  - Implementing the Ed25519 and EdDSA-Ed448 signature schemes (RFC 8032).
  - Providing a platform for research and development of advanced cryptographic
    schemes using twisted Edwards curves.

This library is intended for developers who have experience with
cryptography. It doesn't (yet?) include documentation on how to use
digital signatures or key exchange securely. Consult your local
cryptographer for advice.

#-----------------------------------------------------------------------------

%package -n %{libname}
Summary:	An implementation of elliptic curve cryptography
Group:		System/Libraries

%description -n	%{libname}
The libdecaf library is for elliptic curve research and practical application.
It currently supports Ed448-Goldilocks and Curve25519.

The goals of this library are:
  - Implementing the X25519, X448 key exchange protocols (RFC 7748).
  - Implementing the Ed25519 and EdDSA-Ed448 signature schemes (RFC 8032).
  - Providing a platform for research and development of advanced cryptographic
    schemes using twisted Edwards curves.

This library is intended for developers who have experience with
cryptography. It doesn't (yet?) include documentation on how to use
digital signatures or key exchange securely. Consult your local
cryptographer for advice.

%files -n %{libname}
%{_libdir}/*.so.%{major}*

#-----------------------------------------------------------------------------

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This package contains development files for %{name}.

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/%{sname}
%{_datadir}/%{sname}/cmake

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{pname}-code-%{commit}
%cmake \
	-DENABLE_STATIC:BOOL=OFF \
	-DENABLE_TESTS:BOOL=ON \
        -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
