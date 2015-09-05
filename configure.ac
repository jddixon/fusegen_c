#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.69])
AC_INIT([fusegen], [0.0.2], [jddixon at gmail dot com])
AC_CONFIG_MACRO_DIR([m4])
AC_CONFIG_AUX_DIR([config])
LT_INIT
AM_INIT_AUTOMAKE
AC_CONFIG_SRCDIR([src/fusegen.c])
AC_CONFIG_HEADERS([src/config.h])

# Programs
AC_PROG_CC

# Header files.
AC_CHECK_HEADERS([fcntl.h limits.h stdlib.h string.h sys/statvfs.h unistd.h utime.h sys/xattr.h])

# FUSE development environment
PKG_CHECK_MODULES(FUSE, fuse)

# Necessary typedefs and structures
AC_TYPE_MODE_T
AC_TYPE_OFF_T
AC_TYPE_PID_T
AC_TYPE_SIZE_T
AC_TYPE_UID_T
AC_TYPE_UINT64_T
AC_STRUCT_ST_BLOCKS
AC_CHECK_MEMBERS([struct stat.st_blksize])
AC_CHECK_MEMBERS([struct stat.st_rdev])

# Necessary library functions.
AC_FUNC_CHOWN
AC_FUNC_LSTAT_FOLLOWS_SLASHED_SYMLINK
AC_FUNC_MALLOC

AC_CHECK_FUNCS([fdatasync ftruncate mkdir mkfifo realpath rmdir strerror utimensat])
AC_CHECK_FUNCS([posix_fallocate])

AC_CONFIG_FILES([Makefile src/Makefile])
AC_OUTPUT
