%define module youtube-transcript-api
%define oname youtube_transcript_api
Summary:	Python API which allows you to retrieve the transcript/subtitles for a given YouTube video.
Name:		python-youtube-transcript-api
Version:	1.2.3
Release:	1
Url:		https://github.com/jdepoix/youtube-transcript-api
Source0:	https://files.pythonhosted.org/packages/source/y/%{oname}/%{oname}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
BuildArch:	noarch
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(requests)
# BuildRequires:	python%{pyver}dist(defusedxml)
# BuildRequires:	python%{pyver}dist(coverage)
# BuildRequires:	python%{pyver}dist(httpretty)
# BuildRequires:	python%{pyver}dist(mock)

Provides:	%{module}

%description
This is a python API which allows you to retrieve the transcript/subtitles for a given YouTube video. 
It also works for automatically generated subtitles, supports translating subtitles and it does not require a headless browser, like other selenium based solutions do!

#--------------------------------------------------------------------

%files
%{_bindir}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
%{python_sitelib}/%{oname}/
#--------------------------------------------------------------------

%prep
%autosetup -n %{oname}-%{version} -p1

%build
%py_build

%install
%py_install
