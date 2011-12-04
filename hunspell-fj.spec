Name: hunspell-fj
Summary: Fijian hunspell dictionaries
%define upstreamid 20050811
Version: 0.%{upstreamid}
Release: 4.1%{?dist}
Group: Applications/Text
Source0: http://www.iosn.net/pacific-islands/usp-microgrants/fijian-spellchecker/README_fj_FJ.txt
Source1: http://www.iosn.net/pacific-islands/usp-microgrants/fijian-spellchecker/fj_FJ.dic
Source2: http://www.iosn.net/pacific-islands/usp-microgrants/fijian-spellchecker/fj_FJ.aff
URL: http://www.iosn.net/pacific-islands/usp-microgrants/fijian-spellchecker
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch
BuildRequires: hunspell-devel

Requires: hunspell

%description
Fijian hunspell dictionaries.

%prep
%setup -q -T -c
cp -p %{SOURCE0} %{SOURCE1} %{SOURCE2} .

%build
for i in README_fj_FJ.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p fj_FJ.* $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_fj_FJ.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20050811-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050811-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20050811-3
- tidy spec

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050811-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 01 2008 Caolan McNamara <caolanm@redhat.com> - 0.20050811-1
- initial version
