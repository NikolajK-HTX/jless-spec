# Generated by rust2rpm 21
%bcond_without check

%global crate jless

Name:           jless
Version:        0.8.0
Release:        1%{?dist}
Summary:        Command-line JSON viewer

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/jless
Source:         https://github.com/PaulJuliusMartinez/jless/archive/refs/tags/v0.8.0.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Command-line JSON viewer.}

%description %{_description}

Summary:        %{summary}

%files       -n %{crate}
%license LICENSE
%doc CHANGELOG.md README.md RELEASE_CHECKLIST.md SEARCH.md
%{_bindir}/jless

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
