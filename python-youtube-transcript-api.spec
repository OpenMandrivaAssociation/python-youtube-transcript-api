%define module youtube-transcript-api
%define oname youtube_transcript_api

Name:		python-youtube-transcript-api
Summary:	Python API which retrieves transcripts/subtitles for YouTube videos
Version:	1.2.4
Release:	1
Url:		https://github.com/jdepoix/youtube-transcript-api
Source0:	https://files.pythonhosted.org/packages/source/y/%{oname}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(requests)
BuildRequires:	python%{pyver}dist(defusedxml)
BuildRequires:	python%{pyver}dist(wheel)
Provides:	%{module}

%description
This is a python API which allows you to retrieve the transcript/subtitles for
a given YouTube video.

It also works for automatically generated subtitles, supports translating
subtitles and it does not require a headless browser, like other selenium
based solutions do!

%files
%{_bindir}/%{oname}
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
