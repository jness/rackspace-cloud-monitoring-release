
Name:           rackspace-cloud-monitoring-release 
Version:        1.0
Release:        2%{?dist}

Summary:        Rackspace Cloud Monitoring repository configuration

Group:          System Environment/Base 
License:        Rackspace Cloud Monitoring End User Agreement 
URL:            http://cloudmonitoring.rackspace.com

Source0:        RACKSPACE-CLOUD-MONITORING-GPG-KEY.linux
Source1:	RACKSPACE-CLOUD-MONITORING-GPG-KEY.el5
Source2:	RACKSPACE-CLOUD-MONITORING-GPG-KEY.centos5

Source3:        rackspace-cloud-monitoring.repo.el5	
Source4:        rackspace-cloud-monitoring.repo.el6	
Source5:        rackspace-cloud-monitoring.repo.centos5	
Source6:        rackspace-cloud-monitoring.repo.centos6	
Source7:        rackspace-cloud-monitoring.repo.fedora16
Source8:        rackspace-cloud-monitoring.repo.fedora17

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Provides:       rackspace-cloud-monitoring

%description
This package contains the Rackspace Cloud Monitoring repository
GPG key as well as configuration for yum.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .

%build


%install
rm -rf $RPM_BUILD_ROOT

# MaaS uses multiple keys to sign their packages....
# http://www.rackspace.com/knowledge_center/article/install-the-cloud-monitoring-agent#RedHat
#
%if 0%{?el5}
if [ %{?dist} == .centos5 ] # hacky...
then
install -Dpm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RACKSPACE-CLOUD-MONITORING-GPG-KEY
else
install -Dpm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RACKSPACE-CLOUD-MONITORING-GPG-KEY
fi
%else
install -Dpm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RACKSPACE-CLOUD-MONITORING-GPG-KEY
%endif

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%if 0%{?el5}
if [ %{?dist} == .centos5 ] # hacky...
then
install -pm 644 %{SOURCE5} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/rackspace-cloud-monitoring.repo
else
install -pm 644 %{SOURCE3} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/rackspace-cloud-monitoring.repo
fi
%endif

%if 0%{?el6}
%if 0%{?centos} == 6
install -pm 644 %{SOURCE6} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/rackspace-cloud-monitoring.repo
%else
install -pm 644 %{SOURCE4} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/rackspace-cloud-monitoring.repo
%endif
%endif

%if 0%{?fedora} == 16
install -pm 644 %{SOURCE7} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/rackspace-cloud-monitoring.repo
%endif

%if 0%{?fedora} == 17
install -pm 644 %{SOURCE8} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/rackspace-cloud-monitoring.repo
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*


%changelog
* Thu Apr 04 2013 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.0-2
- MaaS uses multiple signing keys...

* Tue Apr 02 2013 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.0-1
- New package for Rackspace Monitoring Release
