Name:		sprng
Version:	5.0
Release:	1
Group:		Sciences/Mathematics
License:	GPL
Summary:	Scalable Parallel Pseudo Random Number Generators Library
Source0:	http://sprng.cs.fsu.edu/Version2.0/sprng2.0b.tar.gz
URL:		https://sprng.cs.fsu.edu/
BuildRequires:	openmpi
BuildRequires:	gmp-devel
Requires:	sprng-devel
Patch0:		sprng2.0b-build.patch

%description
Scalable Parallel Pseudo Random Number Generators Library.

M. Mascagni and A. Srinivasan (2000), "Algorithm 806: SPRNG: A Scalable
Library for Pseudorandom Number Generation," ACM Transactions on
Mathematical Software, 26: 436-461.

%files

#-----------------------------------------------------------------------
%package	devel
Summary:	Scalable Parallel Pseudo Random Number Generators Library
Group:		Development/Other

%description	devel
Scalable Parallel Pseudo Random Number Generators Library.

M. Mascagni and A. Srinivasan (2000), "Algorithm 806: SPRNG: A Scalable
Library for Pseudorandom Number Generation," ACM Transactions on
Mathematical Software, 26: 436-461.

%files		devel
%{_includedir}/sprng
%{_libdir}/*.a

#-----------------------------------------------------------------------
%prep
%setup -q -n sprng2.0
%patch0 -p1
perl -pi -e 's|^(F77 = )|${1}gfortran|;'			\
	 -e "s|^#(MPIDIR = ).*|\$1`mpic++ --showme:compile`|;"	\
	 -e "s|^#(MPILIB = ).*|\$1`mpic++ --showme:link`|;"	\
	 -e 's|(CFLAGS = .*)|$1 %{optflags}|;'			\
	 -e 's|(FFLAGS = .*)|$1 %{optflags}|;'			\
	SRC/make.INTEL

#-----------------------------------------------------------------------
%build
make

#-----------------------------------------------------------------------
%install
mkdir -p %{buildroot}{%{_includedir}/sprng,%{_libdir}}
install -m 644 include/*.h %{buildroot}%{_includedir}/sprng
install -m 644 lib/*.a %{buildroot}%{_libdir}


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0b-1
+ Revision: 774611
- Import sprng 2.0
- Import sprng 2.0

