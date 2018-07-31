Name: mtx
Version: 1.3.12
Release: 14%{?dist}
Summary: SCSI media changer control program
License: GPLv2
Group: Applications/System
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# http://mtx.opensource-sw.net/bugs/view.php?id=9
Patch0: %{name}-1.3.12-destdir.patch
# http://mtx.opensource-sw.net/bugs/view.php?id=13
# https://bugzilla.redhat.com/show_bug.cgi?id=538403
Patch1: %{name}-1.3.12-argc.patch
Patch2: emc-fix-fail-with-too-high-slot-count_cleanupver.patch
Patch3: mtx-1.3.12-fix-resource-leak.patch
Patch4: mtx-1.3.12-scsitape-usage--add-erase.patch
Patch5: mtx-1.3.12-man-Document-mtx-eject-and-previous-operations.patch
URL: http://mtx.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
The MTX program controls the robotic mechanism in autoloaders and tape
libraries such as the HP SureStore DAT 40x6, Exabyte EZ-17, and
Exabyte 220. This program is also reported to work with a variety of
other tape libraries and autochangers from ADIC, Tandberg/Overland,
Breece Hill, HP, and Seagate.

If you have a backup tape device capable of handling more than one
tape at a time, you should install MTX.


%prep
%setup -q

%patch0 -p2 -b .destdir
%patch1 -p2 -b .argc
%patch2 -p1 -b .emc_slot_count
%patch3 -p1 -b .fixresourceleak
%patch4 -p1 -b .scsitape_adderase
%patch5 -p1 -b .mtxman1upd

# remove exec permission
chmod a-x contrib/config_sgen_solaris.sh contrib/mtx-changer


%build
export CFLAGS="$RPM_OPT_FLAGS"
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CHANGES COMPATABILITY contrib FAQ LICENSE
%doc mtx.doc mtxl.README.html README TODO
%{_mandir}/man1/*
%{_sbindir}/*


%changelog
* Wed Mar 16 2016 David Sommerseth <davids@redhat.com> - 1.3.12-14
- Update scsitape --help screen to show the erase command and improved mtx.1 man page (#948459)

* Wed Mar 16 2016 David Sommerseth <davids@redhat.com> - 1.3.12-13
- Fix resource leak during processing of import/export information

* Fri Mar 11 2016 David Sommerseth <davids@redhat.com> - 1.3.12-12
- Fix fail with too high slot count (#1298647)

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.3.12-11
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.3.12-10
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 19 2009 Dan Horák <dan[at]danny.cz> 1.3.12-5
- dropped debug output when tools are called with wrong number of arguments (#538403)
- added patch to support DESTDIR for installing

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 21 2008 Dan Horák <dan[at]danny.cz> 1.3.12-2
- spec file cleanup for better compliance with the guidelines

* Mon Aug 25 2008 Dan Horák <dan[at]danny.cz> 1.3.12-1
- update to mtx-1.3.12

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3.11-3
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Jindrich Novy <jnovy@redhat.com> 1.3.11-2
- update License
- rebuild for BuildID

* Wed Mar 28 2007 Jindrich Novy <jnovy@redhat.com> 1.3.11-1
- update to 1.3.11 (adds new scsieject utility, bugfixes)
- sync nostrip patch

* Tue Feb 06 2007 Jindrich Novy <jnovy@redhat.com> 1.3.10-1
- update to mtx-1.3.10
- update URL, Source0
- don't strip debuginfo

* Tue Dec 12 2006 Jindrich Novy <jnovy@redhat.com> 1.2.18-9
- spec cleanup

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.2.18-8.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.2.18-8.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.2.18-8.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Mar  7 2005 Jindrich Novy <jnovy@redhat.com> 1.2.18-8
- fix type confusion in SCSI_writet(), SCSI_readt(), slow_memcopy()
  and slow_bzero()
- rebuilt with gcc4

* Thu Feb 10 2005 Jindrich Novy <jnovy@redhat.com> 1.2.18-7
- remove -D_FORTIFY_SOURCE=2 from CFLAGS, present in RPM_OPT_FLAGS

* Wed Feb  9 2005 Jindrich Novy <jnovy@redhat.com> 1.2.18-6
- rebuilt with -D_FORTIFY_SOURCE=2

* Wed Aug 11 2004 Jindrich Novy <jnovy@redhat.com> 1.2.18-5
- dead code elimination
- updated spec link to recent source
- removed spec link to obsolete URL
- rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jan 13 2004 Than Ngo <than@redhat.com> 1.2.18-2
- rebuild

* Fri Sep 26 2003 Harald Hoyer <harald@redhat.de> 1.2.18-1
- 1.2.18

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 1.2.16-6
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun 19 2002 Than Ngo <than@redhat.com> 1.2.16-4
- don't forcibly strip binaries

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Feb 26 2002 Than Ngo <than@redhat.com> 1.2.16-2
- rebuild

* Tue Feb 19 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.16-1
- 1.2.16

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Dec 14 2001 Than Ngo <than@redhat.com> 1.2.15-1
- update to 1.2.15

* Mon Aug 13 2001 Preston Brown <pbrown@redhat.com> 1.2.13-1
- 1.2.13 fixes "+ Too many Data Transfer Elements Reported" problem (#49258)

* Mon Jun 25 2001 Preston Brown <pbrown@redhat.com>
- 1.2.12
- moved binaries to /usr/sbin from /sbin

* Wed Feb 14 2001 Michael Stefaniuc <mstefani@redhat.com>
- 1.2.10
- updated %%doc

* Mon Dec 11 2000 Preston Brown <pbrown@redhat.com>
- 1.2.9

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Thu Jun 15 2000 Preston Brown <pbrown@redhat.com>
- 1.2.7

* Tue May 23 2000 Preston Brown <pbrown@redhat.com> 
- adopted for Winston

* Fri May 12 2000 Kenneth Porter <shiva@well.com>
- 1.2.6
- Fixed 'eepos' stuff to use | rather than || (whoops!)
- Accept a 4-byte element descriptor for the robot arm for certain older
- autochangers. 

* Mon May 8 2000 Kenneth Porter <shiva@well.com>
- Spell sourceforge right so the link at rpmfind.net will work.

* Thu May 4 2000 Kenneth Porter <shiva@well.com>
- 1.2.5

* Thu Oct 29 1998  Ian Macdonald <ianmacd@xs4all.nl>
- moved mtx from /sbin to /bin, seeing as mt is also located there

* Fri Oct 23 1998  Ian Macdonald <ianmacd@xs4all.nl>
- first RPM release
