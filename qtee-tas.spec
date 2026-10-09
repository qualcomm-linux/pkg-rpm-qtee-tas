Name:           qtee-tas
Version:        0.1.0
Release:        1%{?dist}
Summary:        Qualcomm TEE Trusted Application binaries
License:        BSD-3-Clause AND LicenseRef-Qualcomm-No-Login-Binary-QTI
URL:            https://github.com/qualcomm/qtee-tas
Source0:        https://github.com/qualcomm/qtee-tas/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

ExclusiveArch:  aarch64

%global debug_package %{nil}
%global __os_install_post %{nil}

%description
qtee-tas hosts pre-built Qualcomm Trusted Execution Environment (TEE)
Trusted Application (TA) binaries. TAs are distributed as test-signed
.mbn files, organised per chipset target, and run inside Qualcomm's
secure world (QTEE). This package installs the TA binaries for all 
chipset targets provided by the upstream source.


%prep
%autosetup


%build


%install
for chipdir in ta/*/; do
    chip=$(basename "${chipdir}")
    install -d %{buildroot}%{_prefix}/lib/qtee-tas/${chip}
    install -m 644 "${chipdir}"*.mbn %{buildroot}%{_prefix}/lib/qtee-tas/${chip}/
done

%files
%license LICENSE.txt
%license NO.LOGIN.BINARY.LICENSE.QTI.pdf
%doc README.md
%{_prefix}/lib/qtee-tas/*


%changelog
* Tue Sep 22 2026 Abhinaba Rakshit <abhinaba.rakshit@oss.qualcomm.com> - 0.1.0-1
- Initial RPM package with upstream v0.1.0
