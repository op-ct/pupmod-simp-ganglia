Summary: Ganglia Puppet Module
Name: pupmod-ganglia
Version: 4.1.0
Release: 6
License: Apache License, Version 2.0
Group: Applications/System
Source: %{name}-%{version}-%{release}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: pupmod-apache >= 2.0.0-0
Requires: pupmod-common >= 4.2.0-0
Requires: pupmod-concat >= 2.1.0-1
Requires: pupmod-iptables >= 2.0.0-0
Requires: puppet >= 3.3.0
Requires: puppetlabs-stdlib >= 4.1.0-0.SIMP
Buildarch: noarch
Requires: simp-bootstrap >= 4.2.0
Obsoletes: pupmod-ganglia-test

Prefix:"/etc/puppet/environments/simp/modules"

%description
This Puppet module provides the capability to configure Ganglia.

%prep
%setup -q

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/ganglia

dirs='files lib manifests templates'
for dir in $dirs; do
  test -d $dir && cp -r $dir %{buildroot}/%{prefix}/ganglia
done

mkdir -p %{buildroot}/usr/share/simp/tests/modules/ganglia

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/ganglia

%files
%defattr(0640,root,puppet,0750)
/etc/puppet/environments/simp/modules/ganglia

%post
#!/bin/sh

if [ -d /etc/puppet/environments/simp/modules/ganglia/plugins ]; then
  /bin/mv /etc/puppet/environments/simp/modules/ganglia/plugins /etc/puppet/environments/simp/modules/ganglia/plugins.bak
fi

%postun
# Post uninstall stuff

%changelog
* Fri Jan 16 2015 Trevor Vaughan <tvaughan@onyxpoint.com> - 4.1.0-6
- Changed puppet-server requirement to puppet

* Thu Dec 04 2014 Trevor Vaughan <tvaughan@onyxpoint.com> - 4.1.0-5
- Updated to properly handle the SSL protocols in Apache. We now add a
  + if one is warranted and just keep the entry if it starts with a +
  a minus or is 'all'.

* Fri Oct 17 2014 Trevor Vaughan <tvaughan@onyxpoint.com> - 4.1.0-4
- CVE-2014-3566: Updated protocols to mitigate POODLE.

* Sun Jun 22 2014 Kendall Moore <kmoore@keywcorp.com> - 4.1.0-3
- Removed MD5 file checksums for FIPS compliance.

* Fri May 16 2014 Kendall Moore <kmoore@keywcorp.com> - 4.1.0-2
- Updated web/conf.pp to convert cipher suite to an array and updated the apache template.
- Removed all stock classes and related spec tests so they can be ported to the simp module.

* Mon Apr 21 2014 Trevor Vaughan <tvaughan@onyxpoint.com> - 4.1.0-1
- Updated all references to global variables to point to hiera.

* Thu Feb 13 2014 Kendall Moore <kmoore@keywcorp.com> - 4.1.0-0
- Updated to pass all lint tests.
- Added spec tests.
- Updated code documentation.
- Updated templates to use native booleans instead of strings.

* Thu Oct 03 2013 Kendall Moore <kmoore@keywcorp.com> - 2.1.0-1
- Updated all erb templates to properly scope variables.

* Tue Sep 24 2013 Trevor Vaughan <tvaughan@onyxpoint.com> - 2.1.0-0
- Update the gweb LDAP variables to handle ldaps connections.

* Fri Nov 09 2012 Trevor Vaughan <tvaughan@onyxpoint.com> - 2.0.1-7
- Allow the use of no authentication to get to the web interface as an option.
- Provide the ability to have Ganglia bind to the usual 443 interface instead
  of using it's own declaration for Apache.
- Fix a bug where 0.0.0.0/0 would be passed directly to apache instead of
  translated to 'all'.

* Mon Sep 10 2012 Maintenance - 2.0.1-6
- Updated to allow IGMP when using gmetad since Ganglia appears to need it now.

* Thu Jun 07 2012 Maintenance - 2.0.1-5
- Ensure that Arrays in templates are flattened.
- Call facts as instance variables.
- Moved mit-tests to /usr/share/simp...
- Updated pp files to better meet Puppet's recommended style guide.

* Fri Mar 02 2012 Maintenance - 2.0.1-4
- Improved test stubs.

* Fri Feb 20 2012 Morgan Haskel <morgan.haskel@onyxpoint.com> - 2.0.1-3
- Ganglia can now authenticate via LDAP.
- Ganglia ACLs have been implemented.
- Updated the Ganglia module to work properly with gweb.

* Mon Jan 16 2012 Maintenance - 2.0.1-2
- Refactored the module tests.

* Mon Dec 26 2011 Trevor Vaughan <tvaughan@onyxpoint.com> - 2.0-3
- Updated the spec file to not require a separate file list.

* Mon Oct 10 2011 Trevor Vaughan <tvaughan@onyxpoint.com> - 2.0-2
- Updated to put quotes around everything that need it in a comparison
  statement so that puppet > 2.5 doesn't explode with an undef error.
- Fixed a dependency issue that prevented Ganglia from installing properly with
  one run.

* Sat Mar 19 2011 Morgan Haskel <morgan.haskel@onyxpoint.com> - 2.0.0-1
- Updated documentation to note that users are responsible for restarting
  Apache if they use alternate certificates.
- Added Apache related materials.
- Changed all instances of defined(Class['foo']) to defined('foo') per the
  directions from the Puppet mailing list.
- Updated to use concat_build and concat_fragment types.

* Tue Jan 11 2011 Morgan Haskel <morgan.haskel@onyxpoint.com> - 2.0.0-0
- Refactored for SIMP-2.0.0-alpha release

* Tue Dec 7 2010 Morgan Haskel <morgan.haskel@onyxpoint.com> - 1.0-0
- Initial creation of Ganglia puppet module
