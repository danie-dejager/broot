%define name broot
%define version 1.45.1
%define release 1%{?dist}

Summary:  Fast cd command that learns your habits
Name:     %{name}
Version:  %{version}
Release:  %{release}
License:  MIT
URL:      https://github.com/Canop/broot
Source0:  https://github.com/Canop/broot/archive/refs/tags/v%{version}.tar.gz

%define debug_package %{nil}

BuildRequires: rust
BuildRequires: cargo
BuildRequires: gcc
BuildRequires: make
BuildRequires: gzip
BuildRequires: upx

%description
broot is a blazing fast alternative to cd, inspired by z and z.lua. It keeps
track of the directories you use most frequently, and uses a ranking algorithm
to navigate to the best match.

%prep
%setup -q

%build
cargo build --release
strip --strip-all target/release/%{name}
upx target/release/%{name}

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 target/release/%{name} %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}

%changelog
* Sun Apr 6 2025 - Danie de Jager - 1.45.1-1
- Switched to using system Rust toolchain
* Thu Feb 13 2025 - Danie de Jager - 1.44.7-1
* Thu Feb 6 2025 - Danie de Jager - 1.44.6-2
- Rebuilt with rustc 1.84.1
* Sun Jan 12 2025 - Danie de Jager - 1.44.6-1
* Fri Jan 3 2025 - Danie de Jager - 1.44.5-1
* Sat Dec 28 2024 - Danie de Jager - 1.44.3-1
* Fri Dec 20 2024 - Danie de Jager - 1.44.2-2
* Thu Oct 22 2024 - Danie de Jager - 1.44.2-1
* Thu Oct 17 2024 - Danie de Jager - 1.44.1-1
* Thu Sep 12 2024 - Danie de Jager - 1.44.0-1
* Sun Aug 25 2024 - Danie de Jager - 1.43.0-1
* Sun Aug 25 2024 - Danie de Jager - 1.42.0-1
* Mon Aug 5 2024 Danie de Jager - 1.41.1-1 
* Wed Jul 17 2024 Danie de Jager - 1.40.0-1 
* Mon Jul 8 2024 Danie de Jager - 1.39.2-1 
* Sun Jul 7 2024 Danie de Jager - 1.39.1-1 
* Sat Jun 1 2024 Danie de Jager - 1.39.0-1 
* Mon May 6 2024 Danie de Jager - 1.38.0-1 
* Mon Apr 29 2024 Danie de Jager - 1.37.0-1 
* Fri Apr 26 2024 Danie de Jager - 1.36.1-2
- Built with rustc 1.77.2
* Mon Mar 11 2024 Danie de Jager - 1.36.1-1
* Wed Mar 8 2024 Danie de Jager - 1.35.0-1
* Wed Feb 21 2024 Danie de Jager - 1.34.0-1
- Initial RPM build
