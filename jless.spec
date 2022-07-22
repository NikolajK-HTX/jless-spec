Name:          jless
Version:       0.8.0
Release:       1%{?dist}
Summary:       jless is a command-line JSON viewer. 
License:       MIT
URL:           https://github.com/PaulJuliusMartinez/jless
Source0:       https://github.com/PaulJuliusMartinez/%{name}/releases/download/v%{version}/%{name}-v%{version}-x86_64-unknown-linux-gnu.zip

%description
jless is a command-line JSON viewer designed for reading, 
exploring, and searching through JSON data. 

%prep
%setup -qc

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Fri Jul 22 2022 - kagenogmig@gmail.com - 0.8.0-1
- Create SPEC
