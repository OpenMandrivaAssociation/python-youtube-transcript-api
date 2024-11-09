%define module youtube-transcript-api
Summary:	Python API which allows you to retrieve the transcript/subtitles for a given YouTube video.
Name:		python-youtube-transcript-api
Version:	0.6.2
Release:	1
Url:		https://github.com/jdepoix/youtube-transcript-api
Source0:	https://files.pythonhosted.org/packages/source/y/youtube_transcript_api/youtube_transcript_api-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Provides:	%{module}
BuildRequires:	pkgconfig(python)
BuildArch:	noarch

Requires:  python-requests
Requires:  python-coverage
#Requires:  python-coveralls
Requires:  python-httpretty
Requires:  python-mock

%description
This is a python API which allows you to retrieve the transcript/subtitles for a given YouTube video. 
It also works for automatically generated subtitles, supports translating subtitles and it does not require a headless browser, like other selenium based solutions do!

#--------------------------------------------------------------------

%files
%{_bindir}/youtube_transcript_api
%{python_sitelib}/youtube_transcript_api-%{version}-py*.*.egg-info
%{python_sitelib}/youtube_transcript_api/
#--------------------------------------------------------------------

%prep
%autosetup -n youtube_transcript_api-%{version} -p1

%build
%py_build

%install
%py_install
