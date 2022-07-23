%global debug_package %{nil}
%global _unitdir %{_prefix}/lib/systemd/system

Name:    jless
Version: 0.8.0
Release: 1%{?dist}
Summary: A JSON command-line viewer

License: MIT
URL:     https://github.com/PaulJuliusMartinez/jless
Source0: %{url}/archive/v%{version}.tar.gz

%description
jless is a command-line JSON viewer designed for reading, 
exploring, and searching through JSON data. 

%prep
%autosetup

%build
# use latest stable rust version from rustup
curl -Lfo rustup https://sh.rustup.rs
chmod +x rustup
./rustup -y
source ~/.cargo/env

cargo build --release

strip target/release/%{name}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_bindir}
install -m 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/jless

%changelog
* Sat Jul 23 2022 jehaj - 0.8.0-1
- Initial release
