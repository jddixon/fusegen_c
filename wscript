# fusegen_c/wscript
   
BASENAME = 'fusegen'
LIBNAME  = BASENAME + 'Lib'

# waf combines these two to get the archive name
APPNAME = BASENAME + '_c'
VERSION = '0.1.0'

top     = '.'
out     = "build"

def options(ctx):
    ctx.load('compiler_c')
    ctx.add_option('--shared', action='store_true', 
        help='build static library')
    ctx.add_option('--static', action='store_true', 
        help='build static library')

def configure(ctx):
    ctx.load('compiler_c')
    # ctx.env.append_value('CFLAGS', ['-g'])

def build(ctx):
    if ctx.options.shared:
        ctx.env.append_value('LINKFLAGS', ['-Lbuild/libLIBNAME.so'])
        # this isn't found with or without the .so  XXX 
        ctx.env.append_value('LIB', ['libLIBNAME.so'])
        ctx.shlib(source='src/version.c', target='LIBNAME', 
            includes=['include'], cxxflags='-g -Wall -O0')
    else:
        # build a static library by default
        ctx.stlib(source='src/version.c', target='LIBNAME', 
            includes=['include'], cxxflags='-g -Wall -O0')

    ctx.program(source='src/main.c', target=APPNAME, includes='include',
        use='LIBNAME')
