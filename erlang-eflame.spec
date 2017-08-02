%global realname eflame
%global upstream slfritchie
# Technically, we're noarch; but erlang whose directories we install into is not.
%global debug_package %{nil}


Name:		erlang-%{realname}
Version:	0
Release:	%mkrel 0.2.gita085181.1
Summary:	Flame Graph profiler for Erlang
Group:		Development/Erlang
License:	MIT
URL:		https://github.com/%{upstream}/%{realname}
%if 0%{?el7}%{?fedora}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
%endif
#Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Source0:	https://github.com/%{upstream}/%{realname}/archive/a08518142126f5fc541a3a3c4a04c27f24448bae/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar


%description
Flame Graph profiler for Erlang.


%prep
%setup -q -n %{realname}-a08518142126f5fc541a3a3c4a04c27f24448bae


%build
%{erlang_compile}


%install
%{erlang_install}

install -D -p -m 0755 flamegraph.pl %{buildroot}%{erlang_appdir}/bin/flamegraph.pl
install -D -p -m 0755 flamegraph.riak-color.pl %{buildroot}%{erlang_appdir}/bin/flamegraph.riak-color.pl


%check
%{erlang_test}


%files
%license LICENSE
%doc README.md README-Riak-Example.md
%{erlang_appdir}/




%changelog
* Thu Nov 17 2016 neoclust <neoclust> 0-0.2.gita085181.1.mga6
+ Revision: 1067922
- imported package erlang-eflame

